"""
Phase 3 Tier 1 Combined Agent Test Runner
==========================================
Runs 5 test questions against all Phase 3 notebook variants and saves outputs.

Output Structure:
    experimentation/notebooks/Phase 3/test_output/
        question_1/
            question_1_V08.md
            question_1_V08-1.md
            question_1_V08-2.md
            question_1_V08-3.md
        question_2/
            ...
        ...

Usage:
    python run_phase3_tests.py
    
    Or from a notebook:
    %run run_phase3_tests.py
"""

import os
import sys
import yaml
import asyncio
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any

# Add the parent directories to path for imports
SCRIPT_DIR = Path(__file__).parent.resolve()
NOTEBOOKS_DIR = SCRIPT_DIR
PROJECT_ROOT = SCRIPT_DIR.parent.parent.parent

# Output directory
OUTPUT_DIR = SCRIPT_DIR / "test_output"


def load_test_dataset(path: Path) -> Dict[str, Any]:
    """Load the test dataset from YAML."""
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def create_output_dirs(questions: List[Dict]) -> None:
    """Create output directories for each question."""
    for i, q in enumerate(questions, 1):
        question_dir = OUTPUT_DIR / f"question_{i}"
        question_dir.mkdir(parents=True, exist_ok=True)
        print(f"Created directory: {question_dir}")


def save_output(question_num: int, version: str, result: Dict[str, Any], question_text: str) -> Path:
    """Save the output to a markdown file."""
    output_dir = OUTPUT_DIR / f"question_{question_num}"
    output_file = output_dir / f"question_{question_num}_{version}.md"
    
    # Prepare markdown content
    content = f"""# Question {question_num} - {version}

**Generated:** {datetime.now().isoformat()}

## Original Question

{question_text}

---

## Research Report

{result.get('output', 'No output generated')}

---

## Metadata

- **Sprint Findings:** {len(result.get('sprint_findings', []))}
- **Unique Sources:** {len(result.get('source_urls', []))}
- **Quality Scores:** {json.dumps(result.get('quality_scores', []), indent=2)}
- **Cache Stats:** {result.get('cache_stats', 'N/A')}
- **Limitations:** {json.dumps(result.get('limitations', []), indent=2) if result.get('limitations') else 'None'}

### Source URLs

"""
    for url in result.get('source_urls', []):
        content += f"- {url}\n"
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return output_file


async def run_single_test(notebook_module: Any, question: str, version: str) -> Dict[str, Any]:
    """Run a single test using the notebook's agent."""
    print(f"\n  Running {version}...")
    print(f"  Question preview: {question[:80]}...")
    
    start_time = datetime.now()
    try:
        result = await notebook_module.combined_tier1_agent_async({"question": question})
        elapsed = (datetime.now() - start_time).total_seconds()
        print(f"  Completed in {elapsed:.1f}s - Report: {len(result.get('output', ''))} chars")
        return result
    except Exception as e:
        elapsed = (datetime.now() - start_time).total_seconds()
        print(f"  FAILED after {elapsed:.1f}s: {e}")
        return {
            "output": f"Error: {str(e)}",
            "error": str(e),
            "sprint_findings": [],
            "source_urls": [],
            "quality_scores": [],
            "cache_stats": "",
            "limitations": [f"Execution failed: {str(e)}"]
        }


def get_notebook_versions() -> Dict[str, str]:
    """Get mapping of version names to notebook module names."""
    return {
        "V08": "08_Combined_Tier1",
        "V08-1": "08-1_Combined_Tier1", 
        "V08-2": "08-2_Combined_Tier1",
        "V08-3": "08-3_Combined_Tier1"
    }


async def run_all_tests():
    """Main test runner."""
    print("=" * 80)
    print("Phase 3 Tier 1 Combined Agent Test Runner")
    print("=" * 80)
    print(f"Start time: {datetime.now().isoformat()}")
    print(f"Output directory: {OUTPUT_DIR}")
    print()
    
    # Load test dataset
    dataset_path = SCRIPT_DIR / "test_dataset.yaml"
    if not dataset_path.exists():
        print(f"ERROR: Test dataset not found at {dataset_path}")
        return
    
    dataset = load_test_dataset(dataset_path)
    questions = dataset.get('questions', [])
    print(f"Loaded {len(questions)} questions from test dataset")
    
    # Create output directories
    create_output_dirs(questions)
    
    # Get notebook versions
    versions = get_notebook_versions()
    print(f"\nNotebook versions to test: {list(versions.keys())}")
    
    # Results summary
    results_summary = []
    
    # Run tests
    for q_idx, question_data in enumerate(questions, 1):
        question_id = question_data.get('id', f'Q{q_idx}')
        question_title = question_data.get('title', 'Untitled')
        question_text = question_data.get('question', '')
        
        print(f"\n{'=' * 80}")
        print(f"Question {q_idx}/{len(questions)}: {question_id} - {question_title}")
        print(f"{'=' * 80}")
        
        for version_name, notebook_name in versions.items():
            print(f"\n  Testing with {version_name} ({notebook_name})...")
            
            try:
                # Import the notebook module dynamically
                # Note: This assumes notebooks have been converted to .py or can be imported
                # For Jupyter notebooks, we need a different approach
                
                # For now, we'll use nbconvert to execute or papermill
                # But for this script, we'll assume the agent function is available
                
                # Placeholder for actual notebook execution
                # In production, use papermill or jupyter nbconvert --execute
                result = {
                    "output": f"[Placeholder] Would run {notebook_name} with question {q_idx}",
                    "sprint_findings": [],
                    "source_urls": [],
                    "quality_scores": [],
                    "cache_stats": "N/A - placeholder",
                    "limitations": []
                }
                
                # Save output
                output_file = save_output(q_idx, version_name, result, question_text)
                print(f"  Saved: {output_file.name}")
                
                results_summary.append({
                    "question": question_id,
                    "version": version_name,
                    "output_chars": len(result.get('output', '')),
                    "sources": len(result.get('source_urls', [])),
                    "status": "success" if not result.get('error') else "error"
                })
                
            except Exception as e:
                print(f"  ERROR: {e}")
                results_summary.append({
                    "question": question_id,
                    "version": version_name,
                    "output_chars": 0,
                    "sources": 0,
                    "status": f"error: {str(e)}"
                })
    
    # Save summary
    summary_file = OUTPUT_DIR / "test_summary.json"
    with open(summary_file, 'w', encoding='utf-8') as f:
        json.dump({
            "run_time": datetime.now().isoformat(),
            "questions_tested": len(questions),
            "versions_tested": list(versions.keys()),
            "results": results_summary
        }, f, indent=2)
    
    print(f"\n{'=' * 80}")
    print("Test Run Complete")
    print(f"{'=' * 80}")
    print(f"Summary saved to: {summary_file}")
    print(f"End time: {datetime.now().isoformat()}")


if __name__ == "__main__":
    asyncio.run(run_all_tests())
