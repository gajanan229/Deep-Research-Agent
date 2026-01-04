"""
Quantitative evaluation metrics for deep research agents.

These functions are compatible with LangSmith evaluate() and follow
the evaluator function signature: (outputs, reference_outputs) -> float | dict

Metrics from Experimental Roadmap Section 3.1:
- Fact Recall: % of required facts found
- Citation Precision: % of citations that are valid and relevant
- Token Efficiency: Facts per 1000 tokens
"""

import re
from difflib import SequenceMatcher
from typing import Any


def _normalize_text(text: str) -> str:
    """Normalize text for comparison (lowercase, remove extra whitespace)."""
    return " ".join(text.lower().split())


def _fuzzy_match(fact: str, text: str, threshold: float = 0.6) -> bool:
    """
    Check if a fact is present in text using fuzzy string matching.
    
    Args:
        fact: The required fact to find
        text: The text to search in
        threshold: Minimum similarity ratio (0.0 to 1.0)
        
    Returns:
        True if fact is found with similarity >= threshold
    """
    fact_normalized = _normalize_text(fact)
    text_normalized = _normalize_text(text)
    
    # Direct substring check first
    if fact_normalized in text_normalized:
        return True
    
    # Extract key numbers/percentages from the fact
    fact_numbers = set(re.findall(r'\d+\.?\d*%?', fact))
    
    # For facts with specific numbers, check if those numbers appear
    if fact_numbers:
        text_numbers = set(re.findall(r'\d+\.?\d*%?', text))
        # If key numbers from fact aren't in text, likely not a match
        if not fact_numbers.intersection(text_numbers):
            return False
    
    # Sliding window fuzzy match for longer facts
    fact_words = fact_normalized.split()
    text_words = text_normalized.split()
    window_size = len(fact_words)
    
    for i in range(max(0, len(text_words) - window_size + 1)):
        window = " ".join(text_words[i:i + window_size])
        ratio = SequenceMatcher(None, fact_normalized, window).ratio()
        if ratio >= threshold:
            return True
    
    return False


def fact_recall(outputs: dict, reference_outputs: dict) -> dict:
    """
    Calculate the percentage of required facts found in the agent output.
    
    Args:
        outputs: Agent output containing {"output": str, ...}
        reference_outputs: Golden data containing {"required_facts": list[str], ...}
        
    Returns:
        {"key": "fact_recall", "score": float} where score is 0.0 to 1.0
    """
    agent_output = outputs.get("output", "")
    required_facts = reference_outputs.get("required_facts", [])
    
    if not required_facts:
        return {"key": "fact_recall", "score": 1.0}
    
    found_count = 0
    for fact in required_facts:
        if _fuzzy_match(fact, agent_output):
            found_count += 1
    
    score = found_count / len(required_facts)
    
    return {
        "key": "fact_recall",
        "score": score,
        "comment": f"Found {found_count}/{len(required_facts)} required facts",
    }


def citation_precision(outputs: dict, reference_outputs: dict) -> dict:
    """
    Calculate the percentage of citations that are valid URLs.
    
    This is a basic validation that checks URL format. For full FACT-Lite
    validation (checking if cited page supports the claim), use FactChecker.
    
    Args:
        outputs: Agent output containing {"output": str, ...}
        reference_outputs: Golden data (unused for this metric)
        
    Returns:
        {"key": "citation_precision", "score": float} where score is 0.0 to 1.0
    """
    agent_output = outputs.get("output", "")
    
    # Extract URLs from output
    url_pattern = r'https?://[^\s\)\]\}\>\"\']+'
    urls = re.findall(url_pattern, agent_output)
    
    if not urls:
        # No citations to evaluate
        return {
            "key": "citation_precision",
            "score": 0.0,
            "comment": "No URLs found in output",
        }
    
    # Basic URL validation (format check only)
    valid_count = 0
    for url in urls:
        # Check for common valid URL patterns
        if re.match(r'^https?://[a-zA-Z0-9]', url):
            valid_count += 1
    
    score = valid_count / len(urls) if urls else 0.0
    
    return {
        "key": "citation_precision",
        "score": score,
        "comment": f"Found {valid_count}/{len(urls)} valid URL citations",
    }


def token_efficiency(outputs: dict, reference_outputs: dict) -> dict:
    """
    Calculate facts found per 1000 tokens in the output.
    
    Higher scores indicate more efficient research (more facts with fewer tokens).
    
    Args:
        outputs: Agent output containing {"output": str, "token_count": int (optional), ...}
        reference_outputs: Golden data containing {"required_facts": list[str], ...}
        
    Returns:
        {"key": "token_efficiency", "score": float}
    """
    agent_output = outputs.get("output", "")
    required_facts = reference_outputs.get("required_facts", [])
    
    # Estimate token count (rough approximation: ~4 chars per token)
    # Use actual count if provided
    token_count = outputs.get("token_count", len(agent_output) // 4)
    
    if token_count == 0:
        return {"key": "token_efficiency", "score": 0.0}
    
    # Count found facts
    found_count = 0
    for fact in required_facts:
        if _fuzzy_match(fact, agent_output):
            found_count += 1
    
    # Calculate facts per 1000 tokens
    score = (found_count / token_count) * 1000
    
    return {
        "key": "token_efficiency",
        "score": score,
        "comment": f"{found_count} facts in ~{token_count} tokens = {score:.2f} facts/1K tokens",
    }


def minimum_sources_check(outputs: dict, reference_outputs: dict) -> dict:
    """
    Check if the output contains at least the minimum required sources.
    
    Args:
        outputs: Agent output containing {"output": str, ...}
        reference_outputs: Golden data containing {"minimum_sources": int, ...}
        
    Returns:
        {"key": "minimum_sources", "score": float} where 1.0 = met requirement
    """
    agent_output = outputs.get("output", "")
    minimum_sources = reference_outputs.get("minimum_sources", 10)
    
    # Count unique URLs
    url_pattern = r'https?://[^\s\)\]\}\>\"\']+'
    urls = set(re.findall(url_pattern, agent_output))
    
    # Also count numbered references like [1], [2], etc.
    numbered_refs = set(re.findall(r'\[\d+\]', agent_output))
    
    total_sources = max(len(urls), len(numbered_refs))
    
    score = min(1.0, total_sources / minimum_sources) if minimum_sources > 0 else 1.0
    
    return {
        "key": "minimum_sources",
        "score": score,
        "comment": f"Found {total_sources}/{minimum_sources} minimum sources",
    }
