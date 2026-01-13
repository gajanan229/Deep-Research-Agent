# Experimental Roadmap: Validating Deep Research Paradigms

**Date:** January 4, 2026 (Updated)  
**Document Type:** Experimentation Strategy  
**Phase:** Proof-of-Concept Validation  
**Version:** 2.1 (Updated with Dataset V2.0)

---

## Executive Summary

This document outlines a systematic experimental strategy to validate the Tier 1 and Tier 2 architectural paradigms from our Feasibility Report. The goal is to transform qualitative assumptions ("this should improve accuracy") into quantitative evidence ("this improves citation accuracy by X% at Y% token cost increase").

**Core Principle:** We are not testing whether LLMs are intelligent. We are testing whether our architectural decisions improve outcomes beyond what a naive implementation achieves.

**Literature Validation Note:** Following our Feasibility Report V2.0, we prioritize paradigms with strong literature validation:
- **Tier 1 (Validated):** Agile/ReAct, Quality Gates, Iterative Refinement, Experience Store, Knowledge Cache
- **Tier 2 (Partially Validated):** GNWT/OWL Router, Neuro-Symbolic KG Core

**Scope:** 11 Jupyter Notebook experiments (added Experience Store and Knowledge Cache).

### Technology Stack (Locked)

| Component | Specification | Notes |
|-----------|--------------|-------|
| **LLM Model** | `gpt-5-mini-2025-08-07` | Default GPT-5 mini. Used for ALL agents including baselines. |
| **Web Search** | Tavily API | Via `TAVILY_API_KEY` in `experimentation/.env` |
| **Tracing/Eval** | LangSmith | Via `LANGSMITH_API_KEY`, project: `deep_research_new` |
| **Framework** | LangGraph | State machine orchestration |
| **Python** | 3.11+ | Required for LangGraph features |

**Environment Configuration (`experimentation/.env`):**
```
TAVILY_API_KEY=       # Web search API
OPENAI_API_KEY=       # LLM API key (gpt-5-mini-2025-08-07)
LANGSMITH_API_KEY=    # Tracing and evaluation
LANGSMITH_TRACING=true
LANGSMITH_PROJECT=deep_research_new
```

---

## Part I: The Scientific Method

### 1.1 The Fundamental Question

We must isolate **architecture** from **model capability**. A common mistake is attributing improvements to clever design when the real cause is simply using more tokens or a better model.

**The Null Hypothesis:** "Adding architectural complexity does not improve outcomes enough to justify the additional token cost."

Our experiments must disprove this hypothesis for each paradigm, or accept that the paradigm is not worth implementing.

### 1.2 The Control Groups (Dual Baseline Approach)

A single naive baseline would set the bar too low. Improvements over a trivial "search-and-summarize" script prove nothing useful. Instead, we use **two existing baseline agents** of varying complexity, used exactly as they currently work with no modifications.

#### Baseline A: Single-Agent Research Assistant

**Location:** `baseline agent 1/research-assistant.ipynb`

A structured single-agent system with:
- Human-in-the-loop analyst generation
- Multiple analyst personas for different sub-topics
- Expert AI "interviews" for each sub-topic
- Memory and controllability
- Report synthesis from analyst findings

**Complexity Level:** Medium. Has planning and structure but no multi-agent coordination.

#### Baseline B: Multi-Agent Supervisor System

**Location:** `baseline agent 2/5_full_agent.ipynb`

A full multi-agent research system with:
- User clarification and scoping phase
- Research brief generation
- Supervisor agent coordinating multiple researcher agents
- Parallel research execution (up to 3 concurrent researchers)
- Iteration limits (6 max researcher iterations)
- Research compression and synthesis
- Final report generation

**Complexity Level:** High. Represents a well-engineered deep research agent without our experimental paradigms.

#### Why Two Baselines?

Using both baselines answers different questions:

| Comparison | What It Tells Us |
|------------|------------------|
| Paradigm vs. Baseline A | Does the paradigm help a simple agent become competitive? |
| Paradigm vs. Baseline B | Does the paradigm improve an already-sophisticated agent? |
| Baseline A vs. Baseline B | How much does multi-agent coordination alone contribute? |

If a paradigm only beats Baseline A but not Baseline B, it may be redundant with good multi-agent design. If it beats both, it provides genuine architectural value.

**Critical Rule:** These baselines are used exactly as-is. No modifications, no prompt tuning, no optimization. This prevents accidentally degrading their performance and ensures fair comparison.

### 1.3 Variable Isolation Strategy

For each experiment, we compare the paradigm-enhanced agent against both baselines:

| Notebook | What It Tests | Literature Validation | Compared Against |
|----------|---------------|----------------------|------------------|
| evaluation/ | Infrastructure module | LangSmith (offline eval) | N/A |
| 01_Baseline_A | Single-agent baseline | N/A (control) | N/A |
| 02_Baseline_B | Multi-agent baseline | N/A (control) | Baseline A |
| 03_Agile | Sprint loop with retrospective | ✅ ReAct (Search-o1, R1-Searcher) | Baseline A, Baseline B |
| 04_Quality_Gates | Quality checks between phases | ✅ AI Scientist, Agent Laboratory | Baseline A, Baseline B |
| 05_Iterative_Refinement | Critique-revise loop | ✅ WebThinker, LongDPO, CycleResearcher | Baseline A, Baseline B |
| 06_Experience_Store | Case-based reasoning memory | ✅ DS-Agent, Agent K, AgentRxiv | Baseline A, Baseline B |
| 07_Knowledge_Cache | Cascading cache for search optimization | ✅ CKC Architecture | Baseline A, Baseline B |
| 08_Combined_Tier1 | All Tier 1 paradigms together | Combined validation | Baseline A, Baseline B |
| 09_GNWT_Router | Dynamic specialist routing | ⚠️ OWL coordinator pattern | Baseline A, Baseline B |
| 10_Neuro_Symbolic | Entity extraction and knowledge graph | ⚠️ Agent-KB, Agentic Reasoning | Baseline A, Baseline B |
| 11_Full_Stack | Best of Tier 1 + Tier 2 | Combined validation | Baseline A, Baseline B |

**Interpretation Guide:**
- If paradigm beats Baseline A but not B: The paradigm may be redundant with good multi-agent design
- If paradigm beats both baselines: The paradigm provides genuine architectural value
- If paradigm beats Baseline B but not A: Unexpected result requiring investigation
- ✅ = Strong literature validation, ⚠️ = Partial validation (core concept only)

### 1.4 Controlling for Model Intelligence

**The Contamination Problem:** If we ask "What is the capital of France?", the model answers from memory, not from research capability. Even questions like "What was the closing price of NVIDIA stock on December 30, 2025?" can be answered by a small LLM with a single web search API call.

**The Deep Research Threshold (V2.0 - Enhanced):** Questions must require:
- **10-20+ sources** for comprehensive answers (not solvable with 1-3 searches)
- **Multi-step reasoning** in BOTH information gathering AND synthesis/insight discovery
- **Cross-domain synthesis** (combining information across different fields)
- **Causal chain analysis** (tracing impacts across multiple domains)
- **Insight generation** beyond fact compilation

**Contamination Check:**
Before including any question in our test set, we test it against Gemini Flash or GPT-4o-mini with a basic web search tool. If the small model answers correctly with a single search, the question is too easy and must be excluded or made more complex. Google's AI Overview should NOT be able to answer these questions adequately.

---

## Part II: Test Data Design

> **Dataset Version:** 2.0 (January 4, 2026)
> **File:** `data/deep_research_agent_test_dataset.yaml`

### 2.1 Question Taxonomy

Deep research questions must be unsolvable by a simple web search or Google AI Overview. Each question requires **10-20+ sources**, **cross-domain synthesis**, and **multi-step reasoning** in both information gathering and insight discovery.

| Category | Requirements | Minimum Sources | Example Domain |
|----------|--------------|-----------------|----------------|
| **Multi-Hop Causal Chain** | Trace causal chains across 3+ steps with evidence at each step, spanning multiple domains | 12-18 | Pharmaceutical supply chains, shipping disruptions |
| **Trend Synthesis** | Track changes over time across multiple data points, synthesize patterns from diverse sources | 12-14 | Water scarcity, biodiversity loss, grid modernization |
| **Comparative Analysis** | Compare entities across multiple dimensions with cross-domain evidence | 12-16 | Critical minerals policies, CBDC implementations |
| **Causal Investigation** | Identify root causes of phenomena with evidence from multiple fields | 12-15 | Housing affordability, biosecurity risks |
| **Contradiction Resolution** | Find conflicting claims, present evidence, explain why "obvious" answer may be incomplete | 12-14 | Food security paradoxes, AI safety frameworks |
| **Comprehensive Enumeration** | List instances scattered across many sources with synthesis of patterns | 12-14 | AMR mortality projections, space debris statistics |

**Paradigms Stressed by Question Type:**

| Question Type | Primary Paradigms Tested |
|---------------|-------------------------|
| Multi-Hop Causal Chain | GNWT Router (pivoting), Neuro-Symbolic (entity tracking), Agile Sprints |
| Trend Synthesis | Agile Sprints (iterative data gathering), Quality Gates |
| Comparative Analysis | Quality Gates, Iterative Refinement, Agile Sprints |
| Causal Investigation | GNWT Router, Quality Gates, Neuro-Symbolic |
| Contradiction Resolution | Quality Gates, Iterative Refinement |
| Comprehensive Enumeration | Agile Sprints (completeness checking), Quality Gates |

### 2.2 Golden Dataset Construction (V2.0)

**Size:** 20 questions total (5 per difficulty tier)

This is deliberately small to minimize API costs while providing statistical signal.

**Statistical Validity via Monte Carlo Runs:**
With only 20 questions, a single API timeout or bad LLM roll would skew results by 5%. To smooth out variance, each question is run **3 times per configuration** (Monte Carlo method). We report the **average** of these 3 runs, not any single run. This gives us 60 data points per experiment, providing reasonable statistical confidence without excessive cost.

**Difficulty Tiers (Updated for V2.0):**

| Tier | Questions | Expected Baseline Performance | Min Sources |
|------|-----------|------------------------------|-------------|
| **Easy** | 5 | 60-80% correct | 10-12 |
| **Medium** | 5 | 45-65% correct | 12-14 |
| **Hard** | 5 | 25-45% correct | 14-16 |
| **Adversarial** | 5 | 10-30% correct | 12-14 |

> **Note:** Expected baseline performance is LOWER than V1.0 because questions now require 10-20+ sources and cross-domain synthesis. "Easy" in V2.0 would be "Hard" in typical benchmarks.

**Adversarial Questions:** Designed to expose specific failure modes:
- Questions where the "obvious" answer is incomplete (explicit `adversarial_trap` field)
- Questions testing whether policies match outcomes (not just policy announcements)
- Questions with actively contradictory narratives that require resolution
- Questions requiring systems-level thinking across interconnected crises

### 2.3 Golden Answer Construction (Silver Dataset Method)

Writing golden answers from scratch is tedious and error-prone. We use a **Silver Dataset** approach:

1. **LLM Draft:** Use a high-end model (Claude 4.5 Sonnet or GPT-5) to generate initial golden answers and required facts
2. **Human Verification:** Manually verify each LLM-generated answer against authoritative sources
3. **Correction:** Fix any errors the LLM made
4. **Lock:** Finalize the verified dataset

This cuts golden dataset creation time significantly while maintaining accuracy.

**Per-Question Structure (V2.0):**

```yaml
question_id: "E01"
question: |
  The global pharmaceutical supply chain experienced significant stress in 2024-2025, 
  with persistent drug shortages affecting multiple countries. Analyze the interconnected 
  causes of these shortages by examining:
  
  1. The geographic concentration of Active Pharmaceutical Ingredient (API) manufacturing 
  2. How geopolitical tensions and trade policies affected specific drug categories
  3. The role of climate events in disrupting production
  4. Why generic injectable drugs and antibiotics are disproportionately affected
  5. What structural economic factors discourage pharmaceutical companies from investing 
     in robust supply chains for essential medicines
difficulty: easy
category: multi_hop_causal_chain
paradigms_tested:
  - gnwt_router
  - neuro_symbolic
  - agile_sprints
required_facts:
  - "65-70% of APIs globally sourced from China and India as of 2025"
  - "India holds 48% of active API Drug Master Files (DMFs) in 2023"
  - "270 active drug shortages in US as of April 2025"
  - "Hurricanes destroyed 37% of Puerto Rico's pharmaceutical output in 2024"
  - "US-China biotech decoupling banned 48 critical excipients from Chinese suppliers"
  - "Sterile injectables particularly vulnerable due to complex manufacturing and low profitability"
acceptable_structures:
  - "Causal chain analysis linking geographic concentration → policy impacts → climate vulnerability → structural economics"
  - "Multi-factor analysis with quantified impacts for each contributing cause"
common_errors:
  - "Treating shortages as simple supply-demand mismatch without analyzing structural causes"
  - "Missing the interaction between geopolitical and climate factors"
  - "Not distinguishing between different drug categories and their unique vulnerabilities"
minimum_sources: 12
notes: "Tests multi-hop causal reasoning across geopolitics, climate, and economics."
```

### 2.4 Topic Diversity Matrix (V2.0)

The V2.0 dataset deliberately avoids topic concentration. Previous versions over-indexed on AI and battery technology. The new dataset covers 11 distinct domains with minimal overlap:

| Domain | Questions | Example Topics |
|--------|-----------|----------------|
| **Pharmaceuticals/Health** | E01, E05, H04 | API supply chains, drug shortages, AMR |
| **Water/Climate** | E02, M04 | Groundwater depletion, agricultural water, conflict |
| **Critical Minerals** | E03, H05 | Rare earths, processing concentration, energy transition |
| **Shipping/Logistics** | E04 | Red Sea crisis, Panama Canal, freight rates |
| **Energy/Grid** | M01, H05 | Grid modernization, data centers, renewables |
| **Biodiversity** | M02 | Wildlife decline, pollinators, ecosystem tipping points |
| **Housing/Urban** | M03 | Affordability, construction costs, zoning |
| **Food Security** | M04, A04 | Grain exports, fertilizer prices, famine |
| **Space/Technology** | M05, A03 | Orbital debris, Kessler syndrome, satellite constellations |
| **Biosecurity** | H01 | Synthetic biology, AI convergence, DNA synthesis |
| **Digital Finance** | H02, A02 | CBDCs, cross-border payments, financial inclusion |
| **Systems Integration** | H03 | Interconnected crises, feedback loops |
| **AI Governance** | A05 | Safety frameworks, commitment tracking |

### 2.5 Dataset Sources

> **Scientific Rigor Note:** We deliberately avoid using existing benchmarks (HotpotQA, GAIA, etc.) during experimentation. These benchmarks may be contaminated in LLM training data, and optimizing for them would violate train/test separation principles. Standard benchmarks are reserved for final product evaluation only.

**Experimentation Phase: Custom Questions Only**

| Source | Purpose | Rationale |
|--------|---------|-----------|
| **Custom Time-Sensitive** | Questions about recent events (2024-2026) | Cannot be memorized; forces real retrieval |
| **Custom Cross-Domain** | Questions requiring 10-20+ source synthesis | Tests architecture, not model memory |
| **Custom Adversarial** | Questions with explicit "traps" | Tests resistance to obvious-but-incomplete answers |
| **Custom Systems-Level** | Questions connecting multiple domains | Tests ability to trace cascading impacts |

**Final Product Validation (Held-Out):**

| Benchmark | When to Use | Purpose |
|-----------|-------------|---------|
| **GAIA** | Final product only | Standardized comparison to literature |
| **HotpotQA** | Final product only | Multi-hop reasoning benchmark |
| **HLE (Humanity's Last Exam)** | Final product only | Frontier capability testing |
| **SimpleQA** | Final product only | Factual accuracy benchmark |

**Why This Matters:**
- During experimentation, we test whether *our architecture* improves outcomes
- During final validation, we test whether *our product* compares favorably to published systems
- Mixing these phases leads to benchmark overfitting and inflated claims

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
Phase 0: Infrastructure (Must complete first)
    |
    +-- evaluation/           [Python module, NOT a notebook]
            ├── __init__.py
            ├── harness.py    (LangSmith integration)
            ├── metrics.py
            ├── llm_judge.py
            └── fact_checker.py
    
Phase 1: Baseline Establishment (Depends on Phase 0)
    |
    +-- 01_Baseline_A.ipynb   (Single-Agent - rewritten clean)
    +-- 02_Baseline_B.ipynb   (Multi-Agent - rewritten clean)
    
Phase 2: Tier 1 Paradigms (Can run in parallel - ALL VALIDATED)
    |
    +-- 03_Agile_Sprints.ipynb         [Validated: ReAct framework]
    +-- 04_Quality_Gates.ipynb          [Validated: AI Scientist]
    +-- 05_Iterative_Refinement.ipynb   [Validated: WebThinker, LongDPO]
    +-- 06_Experience_Store.ipynb       [Validated: DS-Agent, Agent K]
    +-- 07_Knowledge_Cache.ipynb        [Validated: CKC Architecture]

Phase 3: Tier 1 Synthesis
    |
    +-- 08_Tier1_Combined.ipynb (combines best elements from Phase 2)
    
Phase 4: Tier 2 Paradigms (Partially Validated)
    |
    +-- 09_GNWT_Router.ipynb            [Validated: OWL coordinator pattern]
    +-- 10_Neuro_Symbolic_Lite.ipynb    [Validated: Agent-KB, Agentic Reasoning]

Phase 5: Final Integration
    |
    +-- 11_Full_Stack.ipynb
```

**Key Changes from Previous Version:**
- **Evaluation harness is a Python module** (not a notebook) so notebooks can import it
- **LangSmith** powers the evaluation infrastructure (datasets, experiments, tracing)
- **Baselines split into separate notebooks** for cleaner rewriting

### 4.2 Module & Notebook Specifications

---

#### Module: `evaluation/` (Python Package)
**Purpose:** Reusable testing infrastructure built on LangSmith

> **Why a module, not a notebook?** Notebooks are for exploration. The evaluation harness is *infrastructure* that every experiment imports. Defining it in a notebook would require copy-pasting or messy `%run` magic.

**LangSmith Integration:**

LangSmith provides two evaluation modes:

| Mode | Use Case | Our Application |
|------|----------|-----------------|
| **Offline Evaluation** | Test against datasets with reference outputs | Experimentation (custom golden questions) |
| **Online Evaluation** | Monitor production traces | Final product monitoring |

**Core Components:**

```python
# evaluation/harness.py
from langsmith import Client, evaluate

class ExperimentHarness:
    """LangSmith-powered evaluation harness."""
    
    def __init__(self, dataset_name: str):
        self.client = Client()
        self.dataset_name = dataset_name
    
    def run_evaluation(self, agent_fn, evaluators: list, experiment_name: str):
        """Run offline evaluation against golden dataset."""
        return self.client.evaluate(
            agent_fn,
            data=self.dataset_name,
            evaluators=evaluators,
            experiment_prefix=experiment_name,
        )
```

**Evaluator Functions:**

```python
# evaluation/metrics.py
def fact_recall(outputs: dict, reference_outputs: dict) -> float:
    """Calculate % of required facts found."""
    required = set(reference_outputs.get("required_facts", []))
    found = set(outputs.get("extracted_facts", []))
    return len(required & found) / len(required) if required else 0.0

# evaluation/llm_judge.py  
def coherence_judge(inputs: dict, outputs: dict) -> int:
    """LLM-as-judge for report coherence (1-10 scale)."""
    pass
```

**Output:**
- `evaluation/` Python package (importable by all notebooks)
- LangSmith dataset: `deep-research-golden-v1`

---

#### Notebook 01: Baseline A (Single-Agent)
**Purpose:** Rewrite and evaluate the single-agent research assistant

**Why Rewrite?**
The existing notebooks in `baseline agent 1/` are messy with excessive comments. This notebook produces:
- **Clean implementation** of the single-agent baseline
- **Standardized interface** compatible with evaluation harness

**Contents:**
- Import `evaluation.harness`
- Rewrite research assistant from `baseline agent 1/research-assistant.ipynb`
- Strip tutorial comments; keep only production code
- Run against golden dataset using LangSmith (3 Monte Carlo runs)

**Output:**
- Clean agent code
- `baseline_a_results` experiment in LangSmith

---

#### Notebook 02: Baseline B (Multi-Agent)
**Purpose:** Rewrite and evaluate the multi-agent supervisor system

**Why Rewrite?**
The existing notebooks in `baseline agent 2/` contain scattered implementations. This notebook produces:
- **Clean implementation** of the multi-agent baseline
- **Standardized interface** compatible with evaluation harness

**Contents:**
- Import `evaluation.harness`
- Rewrite from `baseline agent 2/5_full_agent.ipynb`
- Strip tutorial comments; consolidate to single implementation
- Run against golden dataset using LangSmith (3 Monte Carlo runs)

**Output:**
- Clean agent code
- `baseline_b_results` experiment in LangSmith
- Comparison report: Baseline A vs. Baseline B

---

#### Notebook 03: Agile Sprints
**Purpose:** Test the impact of time-boxed iteration with retrospectives

**Contents:**
- Implement sprint loop
- Add retrospective node that re-prioritizes questions
- Compare: Baseline A vs. Baseline B vs. Agile-enhanced
- Measure: Does iteration improve recall? At what cost?

**Hypothesis:** Agile sprints will improve Fact Recall by 15-25% at 1.5x token cost.

**Output:**
- `agile_results.json`
- Chart: Fact Recall vs. Number of Sprints
- Chart: Token Cost vs. Number of Sprints

---

#### Notebook 04: Quality Gates
**Purpose:** Test the impact of explicit quality checkpoints

**Contents:**
- Implement quality gate between search and synthesis
- Gate criteria: Minimum 3 sources, source diversity check
- If gate fails: retry search with modified query
- Compare: Baseline A vs. Baseline B vs. Quality-Gated

**Hypothesis:** Quality gates will reduce Hallucination Rate by 20-30% with minimal token overhead.

**Output:**
- `quality_gate_results.json`
- Chart: Hallucination Rate comparison
- Analysis: How often do gates trigger? What do they catch?

---

#### Notebook 05: Iterative Refinement
**Purpose:** Test the Generate-Critique-Fix loop

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

#### Notebook 06: Experience Store (NEW)
**Purpose:** Test case-based reasoning for non-parametric learning

**Literature Validation:**
> "DS-Agent introduced CBR into automated data science workflows... Agent K advances this paradigm with dynamic external case retrieval and reuse guided by a reward-based memory policy." —[Survey-3]

**Contents:**
- Implement case storage (vector DB or simple dict for MVP)
- Store successful research trajectories and outcomes
- On new query, retrieve similar past cases
- Use retrieved cases to inform planning/search strategy
- Compare: No memory vs. Experience Store

**Hypothesis:** Experience Store will improve Fact Recall by 10-20% on similar question types after 10+ prior runs, with minimal token overhead (1.2x).

**Output:**
- `experience_store_results.json`
- Chart: Performance vs. Number of Prior Cases
- Analysis: Which question types benefit most from case reuse?

---

#### Notebook 07: Knowledge Cache
**Purpose:** Test within-session search optimization through cascading cache

**Literature Validation:**
> Session-scoped caching reduces redundant API calls, semantic similarity enables paraphrase detection, and LLM judgment handles ambiguous cases. The three-layer cascade (deterministic, semantic, LLM) is inspired by CPU cache hierarchies.

**Contents:**
- Implement 3-layer cascade (deterministic, semantic, LLM)
  - Layer 1: URL registry + query normalization (exact matching)
  - Layer 2: Vector embeddings + multi-signal confidence scoring
  - Layer 3: LLM judgment with gap analysis and query refinement
- Multi-signal confidence: top score + score gap + term overlap
- Query specificity adjustment (raise thresholds for high-precision queries)
- Temporal intent recognition (bypass cache for time-sensitive queries)
- Gap analysis: LLM identifies missing info and generates targeted searches
- Compare: Standard search vs. Cached search

**Hypothesis:** Knowledge Cache will reduce web searches by 30-50% with <5% quality degradation, improving both cost efficiency (fewer API calls) and latency (cache hits bypass network).

**Output:**
- `knowledge_cache_results.json`
- Cache hit rate by layer (L1, L2, L3 distribution)
- Quality comparison vs. baselines
- Cost/latency savings analysis
- Cache decision trace (full observability)

---

#### Notebook 08: Tier 1 Combined
**Purpose:** Test all Tier 1 paradigms together

**Contents:**
- Combine: Agile (3 sprints) + Quality Gates + Iterative Refinement (2 passes) + Experience Store + Knowledge Cache
- Run against full golden dataset
- Compare against baseline and individual paradigms

**Key Question:** Do the paradigms compound positively, or do they interfere?

**Hypothesis:** Combined Tier 1 will achieve 40%+ improvement over baseline at 2.5-3x token cost. Knowledge Cache should reduce overall search costs by 30-40%.

**Output:**
- `tier1_combined_results.json`
- Comprehensive comparison table
- Interaction analysis: Which paradigms help each other?

---

#### Notebook 09: GNWT/OWL Router (Tier 2)
**Purpose:** Test dynamic specialist routing (OWL coordinator pattern)

**Literature Validation:**
> "OWL [12] includes a workforce-oriented model, utilising a central manager agent to orchestrate task distribution among specialised execution agents." —[Survey-3]

**Note:** The GNWT terminology is a rebrand; the validated pattern is OWL's central manager + specialists.

**Contents:**
- Implement lightweight router (OWL-style) that selects among specialists:
  - Searcher (web search focus)
  - Analyzer (data analysis focus)
  - Synthesizer (writing focus)
- Router decides which specialist to invoke based on current state
- Compare: Fixed pipeline vs. OWL-style routing

**Hypothesis:** Dynamic routing will improve performance on Hard/Adversarial questions by 10-15% by enabling mid-task pivots. (Reduced from 15-20% based on literature showing simpler OWL approach works.)

**Output:**
- `gnwt_results.json`
- Analysis: When does routing help? When does it hurt?
- Chart: Performance by question difficulty tier

---

#### Notebook 10: Neuro-Symbolic Lite (Tier 2)
**Purpose:** Test basic knowledge graph integration

**Literature Validation:**
> "Agent-KB [103] introduces a KB-driven framework for cross-domain experience transfer... Agentic Reasoning [122] employ knowledge graphs to capture intermediate reasoning processes." —[Survey-3]

**Contents:**
- Implement simple entity extraction (no external graph DB)
- Store entities and relationships in Python dict
- Use entity graph to guide multi-hop searches
- Compare: Standard RAG vs. Neuro-Symbolic Lite

**Hypothesis:** Neuro-Symbolic will improve Causal Chain and Multi-Hop questions by 20-30% but show minimal improvement on simpler question types. (Adjusted based on literature validation.)

**Output:**
- `neuro_symbolic_results.json`
- Analysis: Performance by question category
- Entity graph visualizations for sample questions

---

#### Notebook 11: Full Stack Integration
**Purpose:** Combine best elements from all experiments

**Contents:**
- Take winning configurations from each experiment
- Build the "Champion Agent" configuration based on literature-validated patterns:
  - ReAct-style sprints (Agile)
  - AI Scientist-style quality gates
  - WebThinker-style critique-revise
  - Agent K-style experience store
  - CKC-style cascading cache (Knowledge Cache)
  - OWL-style coordinator routing
  - Agent-KB-style entity tracking (if multi-hop benefits confirmed)
- Run comprehensive evaluation
- Performance ceiling analysis

**Output:**
- `full_stack_results.json`
- Final comparison: Baseline A vs. Baseline B vs. Champion
- Recommended configuration for production
- Cost-benefit analysis
- Comparison to literature benchmarks (GAIA, HotpotQA scores if applicable)

---

### 4.3 Estimated Totals

| Metric | Estimate |
|--------|----------|
| **Notebooks** | 11 (added Experience Store and Knowledge Cache) |
| **Questions** | 20 |
| **Runs per Question** | 3 (Monte Carlo) |
| **Baselines** | 2 (A and B) |
| **Total Baseline Runs** | 120 (20 x 3 x 2) |
| **Total Paradigm Runs** | ~540 (increased due to Experience Store and Knowledge Cache) |

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
|-- evaluation/                          # Phase 0: Infrastructure (Python module)
|   |-- __init__.py
|   |-- harness.py                       # LangSmith integration
|   |-- metrics.py                       # Fact recall, citation precision
|   |-- llm_judge.py                     # Coherence, depth, relevance
|   |-- fact_checker.py                  # FACT-Lite citation validation
|   |-- experience_store.py              # CBR implementation
|
|-- notebooks/
|   |-- 01_Baseline_A.ipynb              # Phase 1: Single-agent (rewritten clean)
|   |-- 02_Baseline_B.ipynb              # Phase 1: Multi-agent (rewritten clean)
|   |-- 03_Agile_Sprints.ipynb           # Phase 2: ReAct validation
|   |-- 04_Quality_Gates.ipynb           # Phase 2: AI Scientist validation
|   |-- 05_Iterative_Refinement.ipynb    # Phase 2: WebThinker validation
|   |-- 06_Experience_Store.ipynb        # Phase 2: DS-Agent validation
|   |-- 07_Knowledge_Cache.ipynb         # Phase 2: CKC Architecture validation
|   |-- 08_Tier1_Combined.ipynb          # Phase 3: Synthesis
|   |-- 09_GNWT_Router.ipynb             # Phase 4: OWL validation
|   |-- 10_Neuro_Symbolic_Lite.ipynb     # Phase 4: Agent-KB validation
|   |-- 11_Full_Stack.ipynb              # Phase 5: Final integration
|
|-- data/
|   |-- deep_research_agent_test_dataset.yaml  # V2.0 unified dataset (questions + answers + evaluation criteria)
|   |-- case_bank/
|   |   |-- cases.json
|
|-- results/                             # LangSmith experiment results cached
|   |-- baseline_a_results.json
|   |-- baseline_b_results.json
|   |-- agile_results.json
|   |-- ...
|
|-- reports/
|   |-- phase2_retrospective.md
|   |-- final_summary.md
```

---

## Appendix B: Golden Dataset Examples (V2.0)

The V2.0 dataset is located at `data/deep_research_agent_test_dataset.yaml`. Below are representative examples from each difficulty tier:

**Easy Tier Example:** (Requires 12+ sources)
```yaml
question_id: "E01"
question: |
  The global pharmaceutical supply chain experienced significant stress in 2024-2025. 
  Analyze the interconnected causes by examining:
  1. Geographic concentration of API manufacturing (quantify China/India shares)
  2. How geopolitical tensions affected specific drug categories
  3. The role of climate events in disrupting production
  4. Why generic injectables are disproportionately affected
  5. Structural economic factors discouraging supply chain investment
difficulty: easy
category: multi_hop_causal_chain
minimum_sources: 12
notes: "Tests multi-hop causal reasoning across geopolitics, climate, and economics."
```

**Adversarial Tier Example:** (Tests for "obvious but wrong" answers)
```yaml
question_id: "A04"
question: |
  Global food commodity markets are projected to be stable in 2024/25 with adequate 
  supplies. Yet acute food insecurity is at record levels. Analyze this disconnect:
  1. The difference between global aggregate supply and regional/local access
  2. How commodity price stability can coexist with food insecurity increases
  3. Why famine conditions exist in places where food is available nearby
  4. The limitations of market-based approaches to food security
difficulty: adversarial
category: contradiction_resolution
minimum_sources: 12
adversarial_trap: "The framing of 'stable markets' creates false reassurance while 
                   access-based food insecurity worsens"
notes: "Tests critical evaluation of market-based food security assumptions."
```

> **Key V2.0 Changes:**
> - All questions require 10-20+ sources (vs. 3-4 in V1.0)
> - Topics diversified across 11 domains (vs. AI/battery concentration in V1.0)
> - Adversarial questions include explicit `adversarial_trap` fields
> - Added `insight_generation` evaluation criterion (10% weight)
> - Adjusted difficulty expectations to reflect increased complexity

---

*End of Experimental Roadmap*
