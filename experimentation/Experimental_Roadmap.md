# Experimental Roadmap: Validating Deep Research Paradigms

**Date:** January 2, 2026  
**Document Type:** Experimentation Strategy  
**Phase:** Proof-of-Concept Validation

---

## Executive Summary

This document outlines a systematic experimental strategy to validate the Tier 1 and Tier 2 architectural paradigms from our Feasibility Report. The goal is to transform qualitative assumptions ("this should improve accuracy") into quantitative evidence ("this improves citation accuracy by X% at Y% token cost increase").

**Core Principle:** We are not testing whether LLMs are intelligent. We are testing whether our architectural decisions improve outcomes beyond what a naive implementation achieves.

**Scope:** 9 Jupyter Notebook experiments targeting less than $80 in API costs total.

---

## Part I: The Scientific Method

### 1.1 The Fundamental Question

We must isolate **architecture** from **model capability**. A common mistake is attributing improvements to clever design when the real cause is simply using more tokens or a better model.

**The Null Hypothesis:** "Adding architectural complexity does not improve outcomes enough to justify the additional token cost."

Our experiments must disprove this hypothesis for each paradigm, or accept that the paradigm is not worth implementing.

### 1.2 The Control Group (Baseline Agent)

The Baseline Agent is a **minimal viable research agent** with no advanced paradigms. Every experiment compares against this control.

**Baseline Agent Definition:**

```
User Query
    |
    v
[Single LLM Call: Generate 3 search queries]
    |
    v
[Execute searches in parallel]
    |
    v
[Single LLM Call: Read all results, write report with citations]
    |
    v
Output
```

**Baseline Properties:**
- No planning phase
- No iteration or refinement
- No quality gates
- No retrospective
- Single-pass generation

**Why This Baseline:** It represents the "naive implementation" that a developer might build in an afternoon. If our paradigms cannot beat this significantly, they are not worth the complexity.

### 1.3 Variable Isolation Strategy

For each experiment, we change **exactly one variable** from the baseline:

| Experiment | Variable Changed | Everything Else |
|------------|------------------|-----------------|
| 01_Baseline | None (control) | N/A |
| 02_Agile | Add sprint loop with retrospective | Same prompts, same model, same queries |
| 03_Quality_Gates | Add quality checks between phases | Same prompts, same model, same queries |
| 04_Iterative_Refinement | Add critique-revise loop | Same prompts, same model, same queries |
| 05_Combined_Tier1 | Combine all Tier 1 paradigms | Same prompts, same model, same queries |
| 06_GNWT_Router | Add dynamic specialist routing | Same prompts, same model, same queries |
| 07_Neuro_Symbolic_Lite | Add basic entity extraction and KG | Same prompts, same model, same queries |
| 08_Full_Stack | Combine Tier 1 + selected Tier 2 | Same prompts, same model, same queries |

### 1.4 Controlling for Model Intelligence

**The Contamination Problem:** If we ask "What is the capital of France?", the model answers from memory, not from research capability.

**Solution: Use Questions Requiring External Data**
- Time-sensitive questions ("What was the closing price of NVIDIA stock on December 30, 2025?")
- Multi-source synthesis ("Compare the AI governance policies of the EU AI Act vs. the US Executive Order on AI")
- Obscure domain facts ("What is the maximum occupancy of the Gund Hall auditorium at Harvard GSD?")

**Solution: Contamination Check**
Before including any question in our test set, we ask the base model (without tools) to answer it. If it answers correctly with high confidence, we exclude that question. We want questions that **require** research to answer.

---

## Part II: Test Data Design

### 2.1 Question Taxonomy

We need questions that stress-test different aspects of our paradigms:

| Category | Tests | Example Question | Paradigms Stressed |
|----------|-------|------------------|-------------------|
| **Simple Fact** | Basic retrieval | "What is the population of Iceland as of 2024?" | Baseline sufficiency |
| **Multi-hop Reasoning** | Connecting disparate facts | "What university did the CEO of the company that acquired Twitter attend?" | Neuro-Symbolic, GNWT |
| **Comprehensive List** | Finding all answers, not just one | "List all countries that have banned TikTok as of 2025" | Agile (iterative search) |
| **Synthesis/Comparison** | Aggregating multiple perspectives | "Compare the battery technology of Tesla Model 3 vs. BYD Seal" | Quality Gates, Iterative Refinement |
| **Temporal Reasoning** | Handling time-sensitive data | "How has the Federal Reserve interest rate changed in the last 6 months?" | Stream Processing (if applicable) |
| **Constraint Satisfaction** | Following specific instructions | "Write a 500-word analysis of X using exactly 3 academic sources" | Industrial Control |

### 2.2 Golden Dataset Construction

**Size:** 20 questions total (5 per difficulty tier)

This is deliberately small to minimize API costs while providing statistical signal.

**Statistical Validity via Monte Carlo Runs:**
With only 20 questions, a single API timeout or bad LLM roll would skew results by 5%. To smooth out variance, each question is run **3 times per configuration** (Monte Carlo method). We report the **average** of these 3 runs, not any single run. This gives us 60 data points per experiment, providing reasonable statistical confidence without excessive cost.

**Difficulty Tiers:**

| Tier | Questions | Expected Baseline Performance |
|------|-----------|------------------------------|
| **Easy** | 5 | 80-90% correct |
| **Medium** | 5 | 50-70% correct |
| **Hard** | 5 | 20-40% correct |
| **Adversarial** | 5 | 0-20% correct |

**Adversarial Questions:** Designed to expose specific failure modes:
- Questions with common misconceptions (tests hallucination resistance)
- Questions requiring information from paywalled sources (tests graceful failure)
- Questions with contradictory sources online (tests conflict resolution)
- Questions requiring multi-hop chains of 3+ steps

### 2.3 Golden Answer Construction (Silver Dataset Method)

Writing golden answers from scratch is tedious and error-prone. We use a **Silver Dataset** approach:

1. **LLM Draft:** Use a high-end model (Claude 3.5 Sonnet or GPT-4) to generate initial golden answers and required facts
2. **Human Verification:** Manually verify each LLM-generated answer against authoritative sources
3. **Correction:** Fix any errors the LLM made
4. **Lock:** Finalize the verified dataset

This cuts golden dataset creation time significantly while maintaining accuracy.

**Per-Question Structure:**

**Example Entry:**

```yaml
question_id: Q07
question: "What university did the CEO of the company that acquired Twitter attend?"
difficulty: hard
category: multi_hop
required_facts:
  - "Elon Musk is the CEO of X (formerly Twitter)"
  - "Elon Musk attended Queen's University (briefly)"
  - "Elon Musk attended University of Pennsylvania (Wharton)"
  - "The acquisition occurred in October 2022"
acceptable_answers:
  - "Queen's University and University of Pennsylvania"
  - "UPenn and Queen's University"
common_errors:
  - "Stanford" (he was accepted but never attended)
  - "Tesla" (company confusion)
minimum_sources: 2
notes: "Tests multi-hop: Twitter acquisition -> CEO identification -> education lookup"
```

### 2.4 Dataset Sources

We will draw from and adapt existing benchmarks:

| Source | Questions to Extract | Adaptation Needed |
|--------|---------------------|-------------------|
| **HotpotQA** | Multi-hop reasoning questions | Update to 2024-2025 facts |
| **DeepSearchQA** | Comprehensiveness-focused questions | Select subset, add golden answers |
| **Custom** | Time-sensitive and adversarial | Create from scratch |
| **ResearchRubrics** | Constraint-satisfaction questions | Simplify rubrics for automated scoring |

---

## Part III: Metrics and Evaluation

### 3.1 Quantitative Metrics

| Metric | Definition | Calculation | Target |
|--------|------------|-------------|--------|
| **Fact Recall** | % of required facts found | (Facts Found / Total Required Facts) * 100 | Higher is better |
| **Citation Precision** | % of citations that are valid and relevant | (Valid Citations / Total Citations) * 100 | Higher is better |
| **Token Efficiency** | Facts per 1000 tokens | Facts Found / (Tokens Used / 1000) | Higher is better |
| **Latency** | Wall-clock time to completion | End Time - Start Time | Lower is better |
| **Cost Efficiency** | Accuracy per dollar | Fact Recall / API Cost | Higher is better |
| **Hallucination Rate** | % of claims not supported by sources | (Unsupported Claims / Total Claims) * 100 | Lower is better |

### 3.2 Qualitative Metrics (LLM-as-Judge)

For subjective quality, we use a separate LLM (different from the agent) as an automated judge.

**Judge Prompt Template:**

```
You are evaluating a research report. Score each dimension from 1-10.

REPORT TO EVALUATE:
{agent_output}

ORIGINAL QUESTION:
{question}

SCORING RUBRIC:

1. COHERENCE (1-10): Is the report logically structured? Do paragraphs flow naturally?
   - 1-3: Disjointed, random jumps between topics
   - 4-6: Some structure but inconsistent
   - 7-10: Clear logical progression

2. DEPTH (1-10): Does the report go beyond surface-level information?
   - 1-3: Only restates obvious facts
   - 4-6: Some analysis but shallow
   - 7-10: Provides genuine insight and synthesis

3. RELEVANCE (1-10): Does the report answer the actual question asked?
   - 1-3: Off-topic or tangential
   - 4-6: Partially addresses the question
   - 7-10: Directly and completely addresses the question

4. FOCUS (1-10): Did the report stay focused or get lost in irrelevant details?
   - 1-3: Spent significant space on irrelevant tangents
   - 4-6: Some wandering but mostly focused
   - 7-10: Tight focus throughout

5. CONCISENESS (1-10): Is the report appropriately concise?
   - 1-3: Excessive filler, repetition, or unnecessary verbosity
   - 4-6: Some padding but mostly efficient
   - 7-10: Every sentence adds value, no wasted words
   - IMPORTANT: Penalize reports that pad length with repetitive information or filler phrases.

Output your scores as JSON:
{"coherence": X, "depth": X, "relevance": X, "focus": X, "conciseness": X}
```

### 3.3 The FACT-Lite Framework

Inspired by DeepResearch Bench's FACT framework, we implement automated citation verification:

**FACT-Lite Steps:**
1. Extract all URLs from the agent's output
2. For each URL:
   - Attempt to fetch the page (check if link is valid)
   - Extract the claim the citation supposedly supports
   - Ask an LLM: "Does this page content support the claim: '{claim}'? Yes/No"
3. Calculate Citation Validity Rate = Valid Citations / Total Citations

### 3.4 Metric Aggregation

For each experiment configuration, we compute:

```
COMPOSITE_SCORE = (
    0.30 * Fact_Recall +
    0.25 * Citation_Precision +
    0.20 * LLM_Judge_Average +
    0.15 * Token_Efficiency_Normalized +
    0.10 * Hallucination_Avoidance
)
```

The weights prioritize correctness over efficiency, but efficiency remains a factor.

---

## Part IV: The Notebook Sequence

### 4.1 Logical Order and Dependencies

```
Phase 1: Foundation (Must complete first)
    |
    +-- 01_Baseline_Agent.ipynb
    |       |
    |       v
    +-- 02_Evaluation_Harness.ipynb (builds the testing infrastructure)
    
Phase 2: Tier 1 Paradigms (Can run in parallel)
    |
    +-- 03_Agile_Sprints.ipynb
    +-- 04_Quality_Gates.ipynb
    +-- 05_Iterative_Refinement.ipynb
    
Phase 3: Tier 1 Synthesis
    |
    +-- 06_Tier1_Combined.ipynb (combines best elements from Phase 2)
    
Phase 4: Tier 2 Paradigms (After Tier 1 baseline established)
    |
    +-- 07_GNWT_Router.ipynb
    +-- 08_Neuro_Symbolic_Lite.ipynb
    
Phase 5: Final Integration
    |
    +-- 09_Full_Stack.ipynb
```

### 4.2 Notebook Specifications

#### Notebook 01: Baseline Agent
**Purpose:** Establish the control group performance  
**API Cost:** ~$5

**Contents:**
- Minimal agent implementation (3 LLM calls total)
- Run against all 20 golden questions (3 runs each = 60 runs)
- Record raw outputs, tokens, latency
- No optimizations

**Output:**
- `baseline_results.json`: Raw performance data
- `baseline_summary.md`: Statistical summary

---

#### Notebook 02: Evaluation Harness
**Purpose:** Build reusable testing infrastructure  
**API Cost:** ~$3 (testing the judge)

**Contents:**
- `QuestionLoader`: Loads golden dataset
- `AgentRunner`: Standardized interface for running any agent config
- `MetricsCalculator`: Computes all quantitative metrics
- `LLMJudge`: Runs qualitative evaluation
- `FACTLiteChecker`: Validates citations
- `ReportGenerator`: Creates comparison tables and charts

**Output:**
- `evaluation/` module with reusable components
- Validated that the harness works on baseline results

---

#### Notebook 03: Agile Sprints
**Purpose:** Test the impact of time-boxed iteration with retrospectives  
**API Cost:** ~$8

**Contents:**
- Implement sprint loop (3 sprints of 5 iterations each)
- Add retrospective node that re-prioritizes questions
- Compare: Baseline vs. 1 Sprint vs. 3 Sprints
- Measure: Does iteration improve recall? At what cost?

**Hypothesis:** Agile sprints will improve Fact Recall by 15-25% at 1.5x token cost.

**Output:**
- `agile_results.json`
- Chart: Fact Recall vs. Number of Sprints
- Chart: Token Cost vs. Number of Sprints

---

#### Notebook 04: Quality Gates
**Purpose:** Test the impact of explicit quality checkpoints  
**API Cost:** ~$6

**Contents:**
- Implement quality gate between search and synthesis
- Gate criteria: Minimum 3 sources, source diversity check
- If gate fails: retry search with modified query
- Compare: Baseline vs. Quality Gated

**Hypothesis:** Quality gates will reduce Hallucination Rate by 20-30% with minimal token overhead.

**Output:**
- `quality_gate_results.json`
- Chart: Hallucination Rate comparison
- Analysis: How often do gates trigger? What do they catch?

---

#### Notebook 05: Iterative Refinement
**Purpose:** Test the Generate-Critique-Fix loop  
**API Cost:** ~$10

**Contents:**
- Implement critique node that identifies weak claims
- Implement revision node that fixes identified issues
- Compare: 0 revisions vs. 1 revision vs. 2 revisions vs. 3 revisions
- Find the point of diminishing returns

**Hypothesis:** 2 revision passes will improve Coherence score by 20% and Citation Precision by 15%. 3+ passes show diminishing returns.

**Output:**
- `refinement_results.json`
- Chart: Quality Metrics vs. Revision Count
- Chart: Token Cost vs. Revision Count
- Recommendation: Optimal number of revisions

---

#### Notebook 06: Tier 1 Combined
**Purpose:** Test all Tier 1 paradigms together  
**API Cost:** ~$8

**Contents:**
- Combine: Agile (3 sprints) + Quality Gates + Iterative Refinement (2 passes)
- Run against full golden dataset
- Compare against baseline and individual paradigms

**Key Question:** Do the paradigms compound positively, or do they interfere?

**Hypothesis:** Combined Tier 1 will achieve 40%+ improvement over baseline at 2.5-3x token cost.

**Output:**
- `tier1_combined_results.json`
- Comprehensive comparison table
- Interaction analysis: Which paradigms help each other?

---

#### Notebook 07: GNWT Router
**Purpose:** Test dynamic specialist routing  
**API Cost:** ~$10

**Contents:**
- Implement lightweight router that selects among specialists:
  - Searcher (web search focus)
  - Analyzer (data analysis focus)
  - Synthesizer (writing focus)
- Router decides which specialist to invoke based on current state
- Compare: Fixed pipeline vs. GNWT routing

**Hypothesis:** GNWT will improve performance on Hard/Adversarial questions by 15-20% by enabling mid-task pivots.

**Output:**
- `gnwt_results.json`
- Analysis: When does routing help? When does it hurt?
- Chart: Performance by question difficulty tier

---

#### Notebook 08: Neuro-Symbolic Lite
**Purpose:** Test basic knowledge graph integration  
**API Cost:** ~$12

**Contents:**
- Implement simple entity extraction (no external graph DB)
- Store entities and relationships in Python dict
- Use entity graph to guide multi-hop searches
- Compare: Standard RAG vs. Neuro-Symbolic Lite

**Hypothesis:** Neuro-Symbolic will improve Multi-hop Question performance by 25-35% but show minimal improvement on Simple Fact questions.

**Output:**
- `neuro_symbolic_results.json`
- Analysis: Performance by question category
- Entity graph visualizations for sample questions

---

#### Notebook 09: Full Stack Integration
**Purpose:** Combine best elements from all experiments  
**API Cost:** ~$10

**Contents:**
- Take winning configurations from each experiment
- Build the "Champion Agent" configuration
- Run comprehensive evaluation
- Performance ceiling analysis

**Output:**
- `full_stack_results.json`
- Final comparison: Baseline vs. Champion
- Recommended configuration for production
- Cost-benefit analysis

---

### 4.3 Estimated Totals

| Metric | Estimate |
|--------|----------|
| **Notebooks** | 9 |
| **Total API Cost** | $70-80 |
| **Questions** | 20 |
| **Runs per Question** | 3 (Monte Carlo) |
| **Total Agent Runs** | ~540 |

---

## Part V: Iteration Strategy

### 5.1 Learning Loop

Each experiment informs the next through a structured feedback loop:

```
Experiment A
    |
    v
[Run Experiment]
    |
    v
[Analyze Results]
    |
    +-- If hypothesis confirmed:
    |       -> Lock in configuration
    |       -> Proceed to next experiment
    |
    +-- If hypothesis rejected:
    |       -> Analyze failure mode
    |       -> Adjust parameters (not paradigm)
    |       -> Re-run with fewer samples
    |       -> If still fails: Downgrade paradigm priority
    |
    +-- If results ambiguous:
            -> Increase sample size for this experiment
            -> Add targeted questions that stress-test the paradigm
```

### 5.2 Parameter Tuning Protocol

When an experiment shows promise but underperforms expectations:

1. **Identify the bottleneck:** Is it the prompts? The loop count? The threshold values?
2. **Run micro-experiments:** Test 3-4 parameter variations on 5 questions (not full dataset)
3. **Select best variant:** Based on micro-experiment results
4. **Re-run full experiment:** With optimized parameters
5. **Document the tuning:** Record what changed and why

### 5.3 Cross-Experiment Insights

After each phase, we create a "Lessons Learned" document:

**Phase 2 Retrospective (After Tier 1 Paradigms):**
- Which paradigm had the best ROI?
- Any surprises in the data?
- Should any Tier 2 paradigm be promoted or demoted?
- What prompting patterns worked best?

**Phase 4 Retrospective (After Tier 2 Paradigms):**
- Did Tier 2 justify the added complexity?
- Which combinations should we test in Phase 5?
- Any paradigms that should be abandoned?

### 5.4 Failure Mode Documentation

For every experiment, we document:

| Failure Mode | Example | Paradigm Affected | Mitigation |
|--------------|---------|------------------|------------|
| Query drift | Agent searches for tangent topics | Agile | Tighter retrospective prompts |
| Over-refinement | Revision removes correct content | Iterative Refinement | Cap at 2 revisions |
| Router oscillation | GNWT switches specialists too often | GNWT | Add hysteresis/cooldown |
| Entity explosion | KG grows too large to be useful | Neuro-Symbolic | Prune low-confidence entities |

---

## Part VI: Success Criteria and Go/No-Go Gates

### 6.1 Minimum Viable Improvement

For a paradigm to be considered "validated," it must demonstrate:

| Metric | Minimum Improvement Over Baseline |
|--------|-----------------------------------|
| Fact Recall | +10% absolute |
| Hallucination Rate | -15% relative |
| Composite Score | +0.05 points |

AND

| Metric | Maximum Acceptable Cost |
|--------|------------------------|
| Token Multiplier | Less than 3x baseline |
| Latency Multiplier | Less than 4x baseline |

### 6.2 Go/No-Go Decision Matrix

After Phase 3 (Tier 1 Combined), we decide whether to proceed with Tier 2:

| Tier 1 Combined Result | Decision |
|------------------------|----------|
| Composite Score +20% or better | Proceed to Tier 2 |
| Composite Score +10-20% | Proceed cautiously, limit Tier 2 scope |
| Composite Score less than +10% | Stop. Re-examine paradigms before continuing |
| Composite Score negative | Abort. Paradigms are counterproductive |

### 6.3 Final Deliverables

At the end of experimentation, we produce:

1. **Results Summary:** Single-page executive summary with key findings
2. **Recommended Configuration:** Exact settings for production agent
3. **Trade-off Analysis:** Cost vs. accuracy curves for different configurations
4. **Known Limitations:** What the experiments did not test
5. **Next Steps:** What to experiment with next (if any)

---

## Part VII: Cost Optimization Strategies

### 7.1 Minimizing API Spend

| Strategy | Implementation |
|----------|---------------|
| **Caching** | Cache all search results and LLM responses. Never pay twice for the same query |
| **Staged rollout** | Run each experiment on 5 questions first. Only expand to full 20 if promising |
| **Smaller models for utilities** | Use GPT-3.5-turbo for the LLM Judge (cheaper, sufficient for rubric scoring) |
| **Abort early** | If first 5 questions show clear failure, stop the experiment |
| **Batch processing** | Group related LLM calls to minimize round-trips |

### 7.2 Development Efficiency

| Strategy | Implementation |
|----------|---------------|
| **Modular notebooks** | Each notebook imports from shared `evaluation/` module |
| **Config files** | All parameters in YAML, not hardcoded |
| **Checkpoint saves** | Save results after each question to resume after failures |
| **Parallel development** | Phase 2 notebooks can be developed simultaneously |

---

## Appendix A: Folder Structure

```
experimentation/
|-- notebooks/
|   |-- 01_Baseline_Agent.ipynb
|   |-- 02_Evaluation_Harness.ipynb
|   |-- 03_Agile_Sprints.ipynb
|   |-- 04_Quality_Gates.ipynb
|   |-- 05_Iterative_Refinement.ipynb
|   |-- 06_Tier1_Combined.ipynb
|   |-- 07_GNWT_Router.ipynb
|   |-- 08_Neuro_Symbolic_Lite.ipynb
|   |-- 09_Full_Stack.ipynb
|
|-- evaluation/
|   |-- __init__.py
|   |-- question_loader.py
|   |-- agent_runner.py
|   |-- metrics.py
|   |-- llm_judge.py
|   |-- fact_checker.py
|   |-- report_generator.py
|
|-- data/
|   |-- golden_questions.yaml
|   |-- golden_answers.yaml
|
|-- results/
|   |-- baseline_results.json
|   |-- agile_results.json
|   |-- ...
|
|-- reports/
|   |-- phase2_retrospective.md
|   |-- final_summary.md
```

---

## Appendix B: Golden Dataset Template

```yaml
# golden_questions.yaml

questions:
  - id: Q01
    text: "What is the current population of Iceland according to the most recent data?"
    category: simple_fact
    difficulty: easy
    required_facts:
      - "Population is approximately 380,000-390,000"
      - "Data is from 2024 or later"
    minimum_sources: 1
    notes: "Tests basic retrieval. Baseline should pass."

  - id: Q02
    text: "List all countries that have completely banned TikTok for all citizens as of January 2025"
    category: comprehensive_list
    difficulty: medium
    required_facts:
      - "India"
      - "Afghanistan"
      - "Pakistan (partial)"
    minimum_sources: 2
    notes: "Tests comprehensiveness. Agent should find ALL bans, not just first result."

  # ... continue for all 20 questions
```

---

*End of Experimental Roadmap*
