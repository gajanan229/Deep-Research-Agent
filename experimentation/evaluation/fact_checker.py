"""
FACT-Lite citation validation system.

Implements automated citation verification inspired by DeepResearch Bench's FACT framework:
1. Extract all URLs from agent output
2. Fetch page content for each URL
3. Verify that cited claims are actually supported by the page content

This provides the Citation Validity Rate metric.
"""

import re
import json
from dataclasses import dataclass
from typing import Any
from concurrent.futures import ThreadPoolExecutor, as_completed

import httpx
from langchain_openai import ChatOpenAI


VERIFIER_MODEL = "gpt-5-mini-2025-08-07"


@dataclass
class CitationResult:
    """Result of validating a single citation."""
    url: str
    claim: str
    is_valid: bool | None  # None if couldn't verify (fetch failed)
    reason: str


@dataclass
class ValidationReport:
    """Full validation report for an agent output."""
    total_citations: int
    valid_citations: int
    invalid_citations: int
    failed_fetches: int
    precision: float
    results: list[CitationResult]


class FactChecker:
    """
    FACT-Lite implementation for citation validation.
    
    Usage:
        checker = FactChecker()
        report = checker.validate_citations(agent_output)
        print(f"Citation precision: {report.precision:.2%}")
    """
    
    def __init__(
        self,
        timeout: float = 10.0,
        max_content_length: int = 10000,
        max_concurrent_fetches: int = 5,
    ):
        """
        Initialize the fact checker.
        
        Args:
            timeout: HTTP request timeout in seconds
            max_content_length: Maximum characters to extract from each page
            max_concurrent_fetches: Maximum concurrent URL fetches
        """
        self.timeout = timeout
        self.max_content_length = max_content_length
        self.max_concurrent_fetches = max_concurrent_fetches
        self._llm = None
    
    @property
    def llm(self) -> ChatOpenAI:
        """Lazy-load the verifier LLM."""
        if self._llm is None:
            self._llm = ChatOpenAI(model=VERIFIER_MODEL, temperature=0)
        return self._llm
    
    def extract_citations(self, text: str) -> list[tuple[str, str]]:
        """
        Extract URLs and their associated claims from text.
        
        Looks for patterns like:
        - "claim text [URL]"
        - "claim text (URL)"
        - Markdown links: [text](URL)
        - Inline URLs following claims
        
        Returns:
            List of (claim, url) tuples
        """
        citations = []
        
        # Pattern 1: Markdown links [text](url)
        markdown_pattern = r'\[([^\]]+)\]\((https?://[^\)]+)\)'
        for match in re.finditer(markdown_pattern, text):
            claim = match.group(1)
            url = match.group(2)
            citations.append((claim, url))
        
        # Pattern 2: Sentence followed by URL in brackets or parentheses
        # Get sentence before [url] or (url)
        bracket_pattern = r'([^.!?\n]+[.!?]?)\s*[\[\(](https?://[^\]\)]+)[\]\)]'
        for match in re.finditer(bracket_pattern, text):
            claim = match.group(1).strip()
            url = match.group(2)
            if claim and len(claim) > 10:  # Filter out very short claims
                citations.append((claim, url))
        
        # Pattern 3: Numbered references like [1] with URL list at end
        # This is more complex and would need the full reference list
        
        # Deduplicate while preserving order
        seen_urls = set()
        unique_citations = []
        for claim, url in citations:
            if url not in seen_urls:
                seen_urls.add(url)
                unique_citations.append((claim, url))
        
        return unique_citations
    
    def extract_urls(self, text: str) -> list[str]:
        """Extract all unique URLs from text."""
        url_pattern = r'https?://[^\s\)\]\}\>\"\']+'
        urls = re.findall(url_pattern, text)
        return list(dict.fromkeys(urls))  # Deduplicate while preserving order
    
    def fetch_url_content(self, url: str) -> str | None:
        """
        Fetch and extract text content from a URL.
        
        Args:
            url: The URL to fetch
            
        Returns:
            Extracted text content, or None if fetch failed
        """
        try:
            with httpx.Client(timeout=self.timeout, follow_redirects=True) as client:
                response = client.get(url, headers={
                    "User-Agent": "Mozilla/5.0 (compatible; DeepResearchBot/1.0)"
                })
                response.raise_for_status()
                
                content = response.text
                
                # Basic HTML to text conversion
                # Remove script and style elements
                content = re.sub(r'<script[^>]*>.*?</script>', '', content, flags=re.DOTALL | re.IGNORECASE)
                content = re.sub(r'<style[^>]*>.*?</style>', '', content, flags=re.DOTALL | re.IGNORECASE)
                
                # Remove HTML tags
                content = re.sub(r'<[^>]+>', ' ', content)
                
                # Decode HTML entities
                content = content.replace('&nbsp;', ' ')
                content = content.replace('&amp;', '&')
                content = content.replace('&lt;', '<')
                content = content.replace('&gt;', '>')
                content = content.replace('&quot;', '"')
                
                # Normalize whitespace
                content = ' '.join(content.split())
                
                # Truncate to max length
                return content[:self.max_content_length]
                
        except Exception as e:
            return None
    
    def verify_claim(self, claim: str, page_content: str) -> tuple[bool, str]:
        """
        Use LLM to verify if a claim is supported by page content.
        
        Args:
            claim: The claim to verify
            page_content: The content from the cited page
            
        Returns:
            Tuple of (is_supported: bool, reasoning: str)
        """
        system_prompt = """You are a fact-checker. Given a claim and page content, determine if the page content supports the claim.

OUTPUT FORMAT:
Respond with ONLY a JSON object:
{"supported": true/false, "reasoning": "<brief explanation>"}

Be rigorous. The claim must be clearly supported by the page content to count as "supported".
If the content is tangentially related but doesn't directly support the specific claim, answer false."""
        
        user_message = f"""CLAIM:
{claim}

PAGE CONTENT:
{page_content[:3000]}

Does the page content support this claim?"""
        
        try:
            response = self.llm.invoke([
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message},
            ])
            
            content = response.content.strip()
            if content.startswith("```"):
                content = content.split("```")[1]
                if content.startswith("json"):
                    content = content[4:]
            
            result = json.loads(content)
            return result.get("supported", False), result.get("reasoning", "")
            
        except Exception as e:
            return False, f"Verification error: {str(e)}"
    
    def validate_citations(self, output: str) -> ValidationReport:
        """
        Validate all citations in an agent output.
        
        Args:
            output: The agent's output text
            
        Returns:
            ValidationReport with precision metrics and per-citation results
        """
        citations = self.extract_citations(output)
        
        if not citations:
            # Fall back to just extracting URLs without claims
            urls = self.extract_urls(output)
            if not urls:
                return ValidationReport(
                    total_citations=0,
                    valid_citations=0,
                    invalid_citations=0,
                    failed_fetches=0,
                    precision=0.0,
                    results=[],
                )
            # Use generic claims for raw URLs
            citations = [(f"Information from {url}", url) for url in urls]
        
        results = []
        
        # Fetch all URLs concurrently
        url_contents = {}
        with ThreadPoolExecutor(max_workers=self.max_concurrent_fetches) as executor:
            future_to_url = {
                executor.submit(self.fetch_url_content, url): url 
                for _, url in citations
            }
            for future in as_completed(future_to_url):
                url = future_to_url[future]
                try:
                    content = future.result()
                    url_contents[url] = content
                except Exception:
                    url_contents[url] = None
        
        # Verify each citation
        valid_count = 0
        invalid_count = 0
        failed_count = 0
        
        for claim, url in citations:
            content = url_contents.get(url)
            
            if content is None:
                results.append(CitationResult(
                    url=url,
                    claim=claim,
                    is_valid=None,
                    reason="Failed to fetch URL",
                ))
                failed_count += 1
            else:
                is_valid, reason = self.verify_claim(claim, content)
                results.append(CitationResult(
                    url=url,
                    claim=claim,
                    is_valid=is_valid,
                    reason=reason,
                ))
                if is_valid:
                    valid_count += 1
                else:
                    invalid_count += 1
        
        total_verifiable = valid_count + invalid_count
        precision = valid_count / total_verifiable if total_verifiable > 0 else 0.0
        
        return ValidationReport(
            total_citations=len(citations),
            valid_citations=valid_count,
            invalid_citations=invalid_count,
            failed_fetches=failed_count,
            precision=precision,
            results=results,
        )


def citation_validity_evaluator(outputs: dict, reference_outputs: dict) -> dict:
    """
    LangSmith-compatible evaluator using FactChecker.
    
    This evaluator performs full FACT-Lite validation including fetching
    cited URLs and verifying claims. Use sparingly due to API/network costs.
    
    Args:
        outputs: Agent output containing {"output": str, ...}
        reference_outputs: Golden data (unused)
        
    Returns:
        {"key": "citation_validity", "score": float}
    """
    checker = FactChecker()
    agent_output = outputs.get("output", "")
    
    report = checker.validate_citations(agent_output)
    
    return {
        "key": "citation_validity",
        "score": report.precision,
        "comment": f"{report.valid_citations}/{report.total_citations} citations verified "
                   f"({report.failed_fetches} fetch failures)",
    }
