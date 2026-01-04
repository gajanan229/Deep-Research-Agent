"""
LLM-as-judge evaluators for qualitative assessment of research outputs.

These evaluators use gpt-5-mini-2025-08-07 as the judge model and implement
the scoring rubric from Experimental Roadmap Section 3.2.

Each dimension is scored 1-10:
- Coherence: Logical structure and flow
- Depth: Analysis beyond surface-level
- Relevance: Directly addresses the question
- Focus: Stays on topic
- Conciseness: Efficient writing
"""

import json
from functools import lru_cache
from typing import Callable

from langchain_openai import ChatOpenAI


# Judge model - different from the agent being tested
JUDGE_MODEL = "gpt-5-mini-2025-08-07"


@lru_cache(maxsize=1)
def _get_judge_llm() -> ChatOpenAI:
    """Get the cached judge LLM instance."""
    return ChatOpenAI(model=JUDGE_MODEL, temperature=0)


def _create_judge_prompt(dimension: str, rubric: str) -> str:
    """Create the system prompt for an LLM judge."""
    return f"""You are an expert evaluator assessing research reports. 

Your task is to score the {dimension.upper()} of a research report on a scale of 1-10.

SCORING RUBRIC FOR {dimension.upper()}:
{rubric}

OUTPUT FORMAT:
Respond with ONLY a JSON object in this exact format:
{{"score": <integer 1-10>, "reasoning": "<brief explanation>"}}

Be rigorous and fair. A score of 7+ should be reserved for genuinely excellent work.
"""


def _run_judge(
    dimension: str,
    rubric: str,
    inputs: dict,
    outputs: dict,
) -> dict:
    """Run an LLM judge evaluation."""
    llm = _get_judge_llm()
    
    question = inputs.get("question", "")
    agent_output = outputs.get("output", "")
    
    system_prompt = _create_judge_prompt(dimension, rubric)
    
    user_message = f"""ORIGINAL QUESTION:
{question}

RESEARCH REPORT TO EVALUATE:
{agent_output}

Score the {dimension} of this report (1-10):"""
    
    try:
        response = llm.invoke([
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message},
        ])
        
        # Parse JSON response
        content = response.content.strip()
        # Handle markdown code blocks if present
        if content.startswith("```"):
            content = content.split("```")[1]
            if content.startswith("json"):
                content = content[4:]
        
        result = json.loads(content)
        score = int(result.get("score", 5))
        reasoning = result.get("reasoning", "")
        
        return {
            "key": dimension,
            "score": score / 10.0,  # Normalize to 0-1 for LangSmith
            "comment": f"Score: {score}/10 - {reasoning}",
        }
        
    except Exception as e:
        return {
            "key": dimension,
            "score": 0.5,  # Default middle score on error
            "comment": f"Judge error: {str(e)}",
        }


# Rubrics from Experimental Roadmap Section 3.2

COHERENCE_RUBRIC = """1-3: Disjointed, random jumps between topics
4-6: Some structure but inconsistent
7-10: Clear logical progression, paragraphs flow naturally"""

DEPTH_RUBRIC = """1-3: Only restates obvious facts
4-6: Some analysis but shallow
7-10: Provides genuine insight and synthesis, goes beyond surface-level information"""

RELEVANCE_RUBRIC = """1-3: Off-topic or tangential
4-6: Partially addresses the question
7-10: Directly and completely addresses the question"""

FOCUS_RUBRIC = """1-3: Spent significant space on irrelevant tangents
4-6: Some wandering but mostly focused
7-10: Tight focus throughout, every section contributes to answering the question"""

CONCISENESS_RUBRIC = """1-3: Excessive filler, repetition, or unnecessary verbosity
4-6: Some padding but mostly efficient
7-10: Every sentence adds value, no wasted words

IMPORTANT: Penalize reports that pad length with repetitive information or filler phrases."""


def coherence_judge(inputs: dict, outputs: dict) -> dict:
    """
    Evaluate the logical structure and flow of the research report.
    
    Args:
        inputs: {"question": str, ...}
        outputs: {"output": str, ...}
        
    Returns:
        {"key": "coherence", "score": float (0-1), "comment": str}
    """
    return _run_judge("coherence", COHERENCE_RUBRIC, inputs, outputs)


def depth_judge(inputs: dict, outputs: dict) -> dict:
    """
    Evaluate whether the report goes beyond surface-level information.
    
    Args:
        inputs: {"question": str, ...}
        outputs: {"output": str, ...}
        
    Returns:
        {"key": "depth", "score": float (0-1), "comment": str}
    """
    return _run_judge("depth", DEPTH_RUBRIC, inputs, outputs)


def relevance_judge(inputs: dict, outputs: dict) -> dict:
    """
    Evaluate whether the report directly addresses the question.
    
    Args:
        inputs: {"question": str, ...}
        outputs: {"output": str, ...}
        
    Returns:
        {"key": "relevance", "score": float (0-1), "comment": str}
    """
    return _run_judge("relevance", RELEVANCE_RUBRIC, inputs, outputs)


def focus_judge(inputs: dict, outputs: dict) -> dict:
    """
    Evaluate whether the report stays focused or wanders into tangents.
    
    Args:
        inputs: {"question": str, ...}
        outputs: {"output": str, ...}
        
    Returns:
        {"key": "focus", "score": float (0-1), "comment": str}
    """
    return _run_judge("focus", FOCUS_RUBRIC, inputs, outputs)


def conciseness_judge(inputs: dict, outputs: dict) -> dict:
    """
    Evaluate whether the report is appropriately concise.
    
    Args:
        inputs: {"question": str, ...}
        outputs: {"output": str, ...}
        
    Returns:
        {"key": "conciseness", "score": float (0-1), "comment": str}
    """
    return _run_judge("conciseness", CONCISENESS_RUBRIC, inputs, outputs)


def create_composite_judge(weights: dict[str, float] | None = None) -> Callable:
    """
    Create a composite evaluator that runs all judges and returns weighted average.
    
    Default weights from Roadmap Section 3.4:
    - 30% Fact Recall (handled separately in metrics.py)
    - 25% Citation Precision (handled separately)
    - 20% LLM Judge Average <- this function
    - 15% Token Efficiency (handled separately)
    - 10% Hallucination Avoidance (handled separately)
    
    For the LLM Judge portion, we weight dimensions equally by default.
    
    Args:
        weights: Optional custom weights for each dimension
        
    Returns:
        Evaluator function compatible with LangSmith
    """
    if weights is None:
        weights = {
            "coherence": 0.2,
            "depth": 0.2,
            "relevance": 0.3,  # Slightly higher weight
            "focus": 0.15,
            "conciseness": 0.15,
        }
    
    judges = {
        "coherence": coherence_judge,
        "depth": depth_judge,
        "relevance": relevance_judge,
        "focus": focus_judge,
        "conciseness": conciseness_judge,
    }
    
    def composite_evaluator(inputs: dict, outputs: dict) -> dict:
        """Run all judges and compute weighted average."""
        results = {}
        weighted_sum = 0.0
        total_weight = 0.0
        
        for dimension, judge_fn in judges.items():
            result = judge_fn(inputs, outputs)
            results[dimension] = result
            
            weight = weights.get(dimension, 0.2)
            weighted_sum += result["score"] * weight
            total_weight += weight
        
        composite_score = weighted_sum / total_weight if total_weight > 0 else 0.5
        
        return {
            "key": "llm_judge_composite",
            "score": composite_score,
            "comment": f"Composite: {composite_score:.2f} from {len(results)} dimensions",
        }
    
    return composite_evaluator
