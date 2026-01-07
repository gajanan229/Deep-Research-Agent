"""
Deep Research Agent Evaluation Module

A LangSmith-powered evaluation harness for testing deep research agent paradigms.
Provides quantitative metrics, LLM-as-judge evaluators, and citation validation.

Technology Stack:
- LLM Model: gpt-5-mini-2025-08-07
- Tracing/Eval: LangSmith
- Framework: LangGraph
"""

from .harness import ExperimentHarness
from .metrics import fact_recall, citation_precision, token_efficiency, minimum_sources_check
from .llm_judge import (
    coherence_judge,
    depth_judge,
    relevance_judge,
    focus_judge,
    conciseness_judge,
    create_composite_judge,
)
from .fact_checker import FactChecker

__all__ = [
    "ExperimentHarness",
    "fact_recall",
    "citation_precision",
    "token_efficiency",
    "minimum_sources_check",
    "coherence_judge",
    "depth_judge",
    "relevance_judge",
    "focus_judge",
    "conciseness_judge",
    "create_composite_judge",
    "FactChecker",
]
