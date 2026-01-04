"""
LangSmith-powered evaluation harness for deep research experiments.

This module provides:
- Dataset loading from YAML test files
- LangSmith dataset synchronization
- Evaluation orchestration with Monte Carlo runs
- Result aggregation across runs
"""

import os
import yaml
import statistics
from pathlib import Path
from typing import Callable, Any
from dataclasses import dataclass, field

from langsmith import Client
from dotenv import load_dotenv


@dataclass
class EvaluationResult:
    """Aggregated results from an evaluation run."""
    experiment_name: str
    num_questions: int
    num_runs: int
    metrics: dict[str, float] = field(default_factory=dict)
    per_question_results: list[dict] = field(default_factory=list)
    raw_results: list[Any] = field(default_factory=list)


class ExperimentHarness:
    """
    LangSmith-powered evaluation harness for deep research experiments.
    
    Usage:
        harness = ExperimentHarness("data/deep_research_agent_test_dataset.yaml")
        harness.sync_to_langsmith()
        
        results = harness.run_evaluation(
            agent_fn=my_agent,
            evaluators=[fact_recall, coherence_judge],
            experiment_name="baseline_a_v1"
        )
    """
    
    def __init__(
        self,
        dataset_path: str,
        langsmith_dataset_name: str = "deep-research-golden-v2",
        env_path: str | None = None,
    ):
        """
        Initialize the evaluation harness.
        
        Args:
            dataset_path: Path to the YAML test dataset file
            langsmith_dataset_name: Name for the LangSmith dataset
            env_path: Optional path to .env file (defaults to experimentation/.env)
        """
        # Load environment variables
        if env_path is None:
            env_path = Path(__file__).parent.parent / ".env"
        load_dotenv(env_path)
        
        self.dataset_path = Path(dataset_path)
        self.langsmith_dataset_name = langsmith_dataset_name
        self.client = Client()
        self._dataset_cache: list[dict] | None = None
        
    def load_dataset(self) -> list[dict]:
        """
        Load and parse the YAML test dataset.
        
        Returns:
            List of question dictionaries with all metadata
        """
        if self._dataset_cache is not None:
            return self._dataset_cache
            
        with open(self.dataset_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        
        self._dataset_cache = data.get("questions", [])
        return self._dataset_cache
    
    def sync_to_langsmith(self, overwrite: bool = False) -> None:
        """
        Create or update the LangSmith dataset with test examples.
        
        Args:
            overwrite: If True, delete existing dataset and recreate
        """
        questions = self.load_dataset()
        
        # Check if dataset exists
        existing_datasets = list(self.client.list_datasets(dataset_name=self.langsmith_dataset_name))
        
        if existing_datasets and overwrite:
            self.client.delete_dataset(dataset_name=self.langsmith_dataset_name)
            existing_datasets = []
        
        if not existing_datasets:
            dataset = self.client.create_dataset(
                dataset_name=self.langsmith_dataset_name,
                description="Golden test dataset for Deep Research Agent experimentation (V2.0)",
            )
        else:
            dataset = existing_datasets[0]
        
        # Create examples
        for q in questions:
            inputs = {
                "question": q["question"],
                "question_id": q["question_id"],
                "difficulty": q["difficulty"],
                "category": q["category"],
            }
            
            # Reference outputs contain the golden data for evaluation
            reference_outputs = {
                "required_facts": q.get("required_facts", []),
                "acceptable_structures": q.get("acceptable_structures", []),
                "common_errors": q.get("common_errors", []),
                "minimum_sources": q.get("minimum_sources", 10),
                "paradigms_tested": q.get("paradigms_tested", []),
            }
            
            self.client.create_example(
                inputs=inputs,
                outputs=reference_outputs,
                dataset_id=dataset.id,
                metadata={
                    "difficulty": q["difficulty"],
                    "category": q["category"],
                    "notes": q.get("notes", ""),
                },
            )
        
        print(f"Synced {len(questions)} examples to LangSmith dataset: {self.langsmith_dataset_name}")
    
    def run_evaluation(
        self,
        agent_fn: Callable[[dict], dict],
        evaluators: list[Callable],
        experiment_name: str,
        monte_carlo_runs: int = 3,
        max_concurrency: int = 4,
        description: str | None = None,
    ) -> EvaluationResult:
        """
        Run evaluation against the golden dataset with Monte Carlo runs.
        
        Args:
            agent_fn: Function that takes inputs dict and returns outputs dict.
                      Expected signature: ({"question": str, ...}) -> {"output": str, ...}
            evaluators: List of evaluator functions compatible with LangSmith
            experiment_name: Prefix for the experiment name in LangSmith
            monte_carlo_runs: Number of runs per question for statistical validity
            max_concurrency: Maximum concurrent evaluations
            description: Optional description for the experiment
            
        Returns:
            EvaluationResult with aggregated metrics
        """
        all_run_results = []
        
        for run_idx in range(monte_carlo_runs):
            run_name = f"{experiment_name}_run{run_idx + 1}"
            
            results = self.client.evaluate(
                agent_fn,
                data=self.langsmith_dataset_name,
                evaluators=evaluators,
                experiment_prefix=run_name,
                description=description or f"Monte Carlo run {run_idx + 1} of {monte_carlo_runs}",
                max_concurrency=max_concurrency,
            )
            
            all_run_results.append(results)
        
        # Aggregate results across runs
        return self._aggregate_results(
            experiment_name=experiment_name,
            run_results=all_run_results,
            monte_carlo_runs=monte_carlo_runs,
        )
    
    def _aggregate_results(
        self,
        experiment_name: str,
        run_results: list,
        monte_carlo_runs: int,
    ) -> EvaluationResult:
        """Aggregate results across Monte Carlo runs."""
        # Collect all metric values by name
        metric_values: dict[str, list[float]] = {}
        per_question: dict[str, list[dict]] = {}
        
        for run_result in run_results:
            for result in run_result:
                question_id = result.get("inputs", {}).get("question_id", "unknown")
                
                if question_id not in per_question:
                    per_question[question_id] = []
                per_question[question_id].append(result)
                
                # Collect metrics
                eval_results = result.get("evaluation_results", {})
                for metric_name, metric_value in eval_results.items():
                    if isinstance(metric_value, (int, float)):
                        if metric_name not in metric_values:
                            metric_values[metric_name] = []
                        metric_values[metric_name].append(float(metric_value))
        
        # Calculate aggregated statistics
        aggregated_metrics = {}
        for metric_name, values in metric_values.items():
            if values:
                aggregated_metrics[f"{metric_name}_mean"] = statistics.mean(values)
                aggregated_metrics[f"{metric_name}_std"] = (
                    statistics.stdev(values) if len(values) > 1 else 0.0
                )
        
        # Calculate per-question averages
        per_question_results = []
        for question_id, results in per_question.items():
            q_result = {
                "question_id": question_id,
                "num_runs": len(results),
                "metrics": {},
            }
            
            q_metrics: dict[str, list[float]] = {}
            for result in results:
                for metric_name, metric_value in result.get("evaluation_results", {}).items():
                    if isinstance(metric_value, (int, float)):
                        if metric_name not in q_metrics:
                            q_metrics[metric_name] = []
                        q_metrics[metric_name].append(float(metric_value))
            
            for metric_name, values in q_metrics.items():
                if values:
                    q_result["metrics"][metric_name] = statistics.mean(values)
            
            per_question_results.append(q_result)
        
        return EvaluationResult(
            experiment_name=experiment_name,
            num_questions=len(per_question),
            num_runs=monte_carlo_runs,
            metrics=aggregated_metrics,
            per_question_results=per_question_results,
            raw_results=run_results,
        )
    
    def get_questions_by_difficulty(self, difficulty: str) -> list[dict]:
        """Filter questions by difficulty tier."""
        return [q for q in self.load_dataset() if q.get("difficulty") == difficulty]
    
    def get_questions_by_category(self, category: str) -> list[dict]:
        """Filter questions by category."""
        return [q for q in self.load_dataset() if q.get("category") == category]
