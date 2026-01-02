# Experimentation Phase: Deep Research Agent Paradigms

This folder contains the planning and validation work for new architectural paradigms in deep research agents.

## Overview

The goal of this phase is to move beyond theoretical proposals to empirical validation. Before writing production code, each architectural paradigm is tested in isolation to measure its actual impact on accuracy, cost, and reliability.

## Completed Work

### 1. Paradigm Design

**File:** `Research_Paradigms.md`

Eleven architectural paradigms were designed to address key challenges in deep research agents:

| # | Paradigm | Description |
|---|----------|-------------|
| 1 | Neuro-Symbolic | Knowledge graph state with entity resolution |
| 2 | Diffusion-Based | Iterative refinement through critique loops |
| 3 | Active Inference | Bayesian information-gain-driven search |
| 4 | Epistemic Market | Adversarial verification with market dynamics |
| 5 | Stream Processing | Event-driven continuous research updates |
| 6 | Stigmergy | Swarm-based distributed exploration |
| 7 | Global Workspace | Dynamic specialist routing via salience |
| 8 | Agile ResearchOps | Sprint-based execution with retrospectives |
| 9 | Immunological | Runtime error detection and self-healing |
| 10 | Industrial Control | Quality gates and feedback loops |
| 11 | Self-Organizing | Dynamic graph generation at runtime |

### 2. Feasibility Analysis

**File:** `Paradigm_Feasibility_Report.md`

Each paradigm was evaluated across six dimensions:
- Effectiveness
- Implementation complexity
- Token cost vs. accuracy gain
- Problem importance
- Infrastructure requirements
- Debuggability

A rigorous critique identified over-engineered proposals and distinguished genuinely useful ideas from impractical designs.

**Final Tier Recommendations:**

| Tier | Paradigms | Status |
|------|-----------|--------|
| Tier 1 | Agile, Industrial Control, Iterative Refinement, Stream Processing | Implement now |
| Tier 2 | Neuro-Symbolic, GNWT Router, Immunological, Active Inference | Consider with caution |
| Tier 3 | Latent Diffusion, Epistemic Market, Stigmergy, Self-Organizing | Avoid |

## Upcoming Work

### 3. Experimental Validation

**File:** `Experimental_Roadmap.md`

The next phase involves building Jupyter Notebook experiments to generate quantitative performance data. The roadmap defines:

- **Baseline Agent:** A minimal control group with no advanced paradigms
- **Golden Dataset:** 20 questions across 4 difficulty tiers with verified answers
- **Metrics Framework:** Fact recall, citation precision, token efficiency, hallucination rate
- **LLM-as-Judge:** Automated qualitative scoring for coherence, depth, and focus
- **FACT-Lite:** Automated citation verification by fetching and validating URLs

### Notebook Sequence

```
Phase 1: Foundation
    01_Baseline_Agent.ipynb
    02_Evaluation_Harness.ipynb

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

### Success Criteria

A paradigm is validated only if it demonstrates:
- At least +10% improvement in Fact Recall over baseline
- At least -15% reduction in Hallucination Rate
- Token cost multiplier under 3x

## Folder Structure

```
experimentation/
|-- README.md                          <- This file
|-- Research_Paradigms.md              <- Paradigm definitions and details
|-- Paradigm_Feasibility_Report.md     <- Analysis and tier recommendations
|-- Experimental_Roadmap.md            <- Validation methodology
|
|-- notebooks/                         <- (To be created)
|-- evaluation/                        <- (To be created)
|-- data/                              <- (To be created)
|-- results/                           <- (To be created)
```

## Key Documents

| Document | Purpose |
|----------|---------|
| [Research_Paradigms.md](./Research_Paradigms.md) | Detailed paradigm descriptions |
| [Paradigm_Feasibility_Report.md](./Paradigm_Feasibility_Report.md) | Engineering analysis and recommendations |
| [Experimental_Roadmap.md](./Experimental_Roadmap.md) | Validation methodology and notebook specifications |

## Next Steps

1. Create the golden question dataset using the Silver Dataset method
2. Build the evaluation harness (Notebook 02)
3. Establish baseline performance (Notebook 01)
4. Execute Tier 1 experiments sequentially
5. Decide whether to proceed with Tier 2 based on results
