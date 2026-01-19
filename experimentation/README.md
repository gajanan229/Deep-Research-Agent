# Experimentation Phase: Deep Research Agent

This folder contains the experimental validation work for testing architectural paradigms in deep research agents.

## Overview

The experimentation phase focuses on empirical validation. Each architectural paradigm defined in the planning phase is implemented and tested in isolation to measure its actual impact on accuracy, cost, and reliability. The goal is to generate quantitative performance data before writing production code.

## Experimental Framework

### Baseline Agents

Two baseline implementations serve as control groups:

- **Baseline A:** Single-agent architecture with basic research capabilities
- **Baseline B:** Multi-agent supervisor architecture for comparison

### Evaluation Methodology

All experiments use a standardized evaluation harness that measures:

- **Fact Recall:** Percentage of verifiable facts correctly stated
- **Citation Precision:** Accuracy and relevance of source citations
- **Token Efficiency:** Cost-effectiveness of each approach
- **Hallucination Rate:** Instances of fabricated information

### Success Criteria

A paradigm is validated only if it demonstrates:

- At least +10% improvement in Fact Recall over baseline
- At least -15% reduction in Hallucination Rate
- Token cost multiplier under 3x

## Notebook Sequence

```
Phase 1: Foundation
    01_Baseline_A.ipynb          <- Single-agent baseline
    02_Baseline_B.ipynb          <- Multi-agent baseline

Phase 2: Tier 1 Paradigms
    03_Agile_Sprints.ipynb
    04_Quality_Gates.ipynb
    05_Iterative_Refinement.ipynb

Phase 3: Tier 1 Synthesis
    06_Tier1_Combined.ipynb

Phase 4: Tier 2 Paradigms
    07_GNWT_Router.ipynb
    08_Neuro_Symbolic_Lite.ipynb

Phase 5: Final Integration
    09_Full_Stack.ipynb
```

## Folder Structure

```
experimentation/
|-- README.md                   <- This file
|-- requirements.txt            <- Python dependencies
|-- .env                        <- Environment variables
|
|-- notebooks/                  <- Jupyter notebook experiments
|-- evaluation/                 <- Evaluation harness and metrics
|-- data/                       <- Test datasets
|-- results/                    <- Experiment outputs and analysis
```

## Related Documents

The planning documents that define the paradigms and validation methodology are located in the `/planning` folder:

- [Research_Paradigms.md](../planning/Research_Paradigms.md)
- [Paradigm_Feasibility_Report.md](../planning/Paradigm_Feasibility_Report.md)
- [Experimental_Roadmap.md](../planning/Experimental_Roadmap.md)

## Current Status

The experimentation phase is in progress. Refer to the notebooks folder for completed experiments and the results folder for performance data.

