# Research Notes: A Comprehensive Survey of Deep Research

**Paper:** A Comprehensive Survey of Deep Research - Systems, Methodologies, and Applications
**Location:** `research/A Comprehensive Survey of Deep Research - Systems, Methodologies, and Applications.pdf`

## Section 2: The Evolution and Technical Framework of Deep Research

This section details the four fundamental technical dimensions that define a Deep Research system. For our project, each dimension represents a core component we must engineer.

### 1. Foundation Models and Reasoning Engines
*   **Definition**: Moving beyond general-purpose LLMs to specialized architectures capable of complex, multi-step reasoning (e.g., OpenAI o3, DeepSeek-R1).
*   **Key Capabilities**:
    *   **Context Management**: Handling massive context windows (200k - 1M tokens) to synthesize results from hundreds of sources.
    *   **Advanced Reasoning**: Utilizing **Chain-of-Thought (CoT)**, **Tree-of-Thought (ToT)**, and self-critique mechanisms to navigate complex research problems without getting lost.
*   **Project Consideration**: We need to decide whether to use a single powerful model (like GPT-4o) or a specialized reasoning model. Implementing *long-context handling* strategies (like summarization or RAG) is critical to avoid token limits when processing many documents.

### 2. Tool Utilization and Environmental Interaction
*   **Definition**: The system's ability to "act" in the digital world to gather data.
*   **Key Capabilities**:
    *   **Web Interaction**: From simple API calls to full headless browsing (handling dynamic JS content, infinite scrolls).
    *   **Content Processing**: Parsing diverse formats (PDFs, Charts, Data Tables) into structured text.
*   **Project Consideration**: Our agent needs a robust **Web Browser Tool** (not just a search API) to read actual page content. We also need reliable **PDF parsing** (specifically for academic papers) and logic to extract tabular data.

### 3. Task Planning and Execution Control
*   **Definition**: How the system breaks down a vague user goal into executable steps.
*   **Key Capabilities**:
    *   **Hierarchical Planning**: Decomposing a high-level goal ("Research capabilities of Agent X") into sub-tasks ("Search for X", "Find documentation", "Compare with Y").
    *   **Execution Monitoring**: Self-correction loops detecting when a search path is dead and automatically trying a different query.
*   **Project Consideration**: We should implement a **Planning Phase** where the agent generates a checklist *before* browsing. The system must support **iterative execution** (retrying failed steps) rather than a linear "one-shot" attempt.

### 4. Knowledge Synthesis and Output Generation
*   **Definition**: Aggregating gathered information into a final, truthful product.
*   **Key Capabilities**:
    *   **Information Evaluation**: Assessing source credibility and detecting contradictions between sources.
    *   **Structured Reporting**: generating outputs with clear hierarchy, citations, and evidence linkage.
*   **Project Consideration**: Our final output cannot just be a text blob. It needs to be a **structured report** (Markdown) with explicit **citations/links** to the sources found. We need logic to flag conflicting information.

## Section 4: Implementation Technologies and Challenges

### Architectural Patterns
The paper outlines four primary architectures for building these systems. We need to choose the best fit:

1.  **Monolithic Architecture** (e.g., OpenAI/DeepResearch):
    *   **Description**: A centralized "Brain" (LLM) controls all tools directly. Shared memory state.
    *   **Pros**: strong coherence, simpler state management.
    *   **Cons**: Hard to scale, potential for context overload.
2.  **Pipeline-Based Architecture** (e.g., n8n):
    *   **Description**: Sequential, pre-defined stages (Search -> Scrape -> Summarize -> Write).
    *   **Pros**: Modular, predictable, easier to debug.
    *   **Cons**: Rigid; struggles with dynamic problems requiring "backtracking".
3.  **Multi-Agent Architecture** (e.g., smolagents, TARS):
    *   **Description**: Specialized agents (SEARCHER, REVIEWER, WRITER) collaborate.
    *   **Pros**: Scalable, allows specialization (e.g., a "Critic" agent).
    *   **Cons**: Complex to coordinate, risk of infinite loops between agents.
4.  **Hybrid Architecture**:
    *   **Description**: Combines tailored pipelines for routine tasks with agents for complex reasoning.

### Key Challenges
*   **Hallucination Control**: The biggest risk. *Solution*: **Source Grounding** (every claim must have a URL citation) and **Contradiction Detection** (explicitly checking if Source A disagrees with Source B).
*   **Privacy & Security**: *Solution*: **Query Isolation** (ensure user A's data doesn't leak into User B's context) and respecting `robots.txt` or terms of service during scraping.
*   **Explainability**: Users need to trust the research. *Solution*: Provide a **"Reasoning Trace"** (logs showing "I am searching for X because Y...") alongside the final report.

## Section 5: Evaluation Methodologies and Benchmarks

We cannot improve what we cannot measure. This section provides a roadmap for testing our agent.

### Functional Verification
*   **Task Completion**: Can the agent successfully answer a complex question? (Benchmark: **WebArena**, **GAIA**).
*   **Information Retrieval**:
    *   **Recall**: Did it find *all* relevant key facts?
    *   **Precision**: Did it avoid irrelevant noise?
    *   **Source Diversity**: Did it use varied sources (e.g., not just Wikipedia, but also academic papers and news)?
*   **Synthesis Quality**:
    *   **Factuality**: Checking claims against a "Gold Standard".
    *   **coherence**: Is the report logically structured?

### Evaluation Benchmarks & Applicability
We should use these standard benchmarks to validate our system:

| Benchmark | Focus | Applicability to Our Project |
| :--- | :--- | :--- |
| **SimpleQA** | Factual accuracy (short answers) | **High**: Good for regression testing basic fact retrieval. |
| **GAIA** | General Assistant tasks | **Medium**: Tests tool usage and multi-step reasoning. |
| **Humanity's Last Exam (HLE)** | Advanced reasoning | **Low/Medium**: Good for "stress testing" complex logic, but maybe overkill for MVP. |
| **TruthfulQA** | Hallucination detection | **High**: Critical for ensuring our agent doesn't lie. |

**Project Recommendation**: Start with a small **"Golden Set"** of 10-20 complex questions with known answers. Evaluate our agent on:
1.  **Fact Retrieval Rate**: % of key facts found.
2.  **Citation Accuracy**: Are the links correct and relevant?
3.  **Cost**: Token usage per research report.

## Section 8: Future Research Directions

Future development of the Deep Research Agent should consider aligned improvements in these key areas:

1.  **Advanced Reasoning Architectures**: 
    *   Context window optimization.
    *   Hybrid symbolic-neural approaches (combining LLMs with formal logic).
    *   Enhanced causal reasoning and uncertainty representation.
2.  **Multi-Modal Deep Research**:
    *   Integrating visual information (charts, scientific images).
    *   Analyzing video and audio content as research sources.
    *   Cross-modal reasoning and consistency verification.
3.  **Domain-Specific Optimization**:
    *   Adaptations for specific fields like Science, Law, and Medicine.
    *   Integration with specialized scientific workflows.
4.  **Human-AI Collaboration and Standardization**:
    *   Interactive workflows (human-in-the-loop query refinement).
    *   Standardized protocols for agent interoperability.
    *   Collaborative knowledge creation (mixed-initiative research).

---

# Research Notes: Deep Research Survey (Paper 2)

**Paper:** Deep Research: A Survey of Autonomous Research Agents
**Location:** `research/Deep Research - A Survey of Autonomous Research Agents.pdf`

## Core Components (Sections 2-4)

The paper breaks down the Deep Research agent into modular components. Here is how they work and what we should implement:

### 1. Planning (Section 2)
*   **Role**: Translates a broad user intent into a structured "Research Plan" (e.g., specific sub-goals) *before* acting.
*   **Key Patterns**:
    *   **Structured World Knowledge**: Using "mental simulations" or global graphs to plan ahead (e.g., *Simulate Before Act*).
    *   **Learnable Planning**: Agents that improve their planning strategy over time via feedback (RL) or large-scale training.
*   **Takeaway**: We must implement an **explicit planning stage**. The agent should output a list of sub-questions before searching.

### 2. Question Developing (Section 3)
*   **Role**: Converting a sub-goal from the plan into specific, diverse search queries.
*   **Approaches**:
    *   **Reward-Optimized**: Learning to ask better questions based on search success (e.g., did the query find the answer?).
    *   **Supervision-Driven**: Using rule-based logic or "Planner" agents to decompose questions deterministically.
*   **Takeaway**: Avoid simple keyword extraction. Use a dedicated prompt or sub-agent to generate **multiple, varied queries** for each sub-topic to maximize coverage.

### 3. Web Exploration (Section 4)
*   **Role**: The actual retrieval of information.
*   **Two Choices**:
    *   **Web Retrieval Agents** (Browser-based): Navigate pages, click links, handle JS. Good for deep digging but slow/expensive.
    *   **API-Based Systems** (Google/Bing API): Fast, reliable, but limited to indexed surface content.
*   **Takeaway**: A **Hybrid Approach** is best. Use APIs for broad "surface" facts, and a Browser Tool for "deep" reading of specific pages/PDFs.

## Report Generation (Section 5)
*   **Structure Control**: Generating long reports requires maintaining global coherence (e.g., using an outline) rather than just streaming text.
*   **Factual Integrity**: Critical need for **conflict resolution** (what if two sites disagree?) and **grounding** (every claim must link to a source).

## Actionable Insights & Future Directions (Sections 6-8)

### Optimization Strategies (Section 6)
*   **Workflow**: **Multi-agent** systems (specialized Planner, Searcher, Writer) generally outperform Monolithic ones for complex research.
*   **Training**: **Reinforcement Learning (RL)** is key for optimizing the "Search -> Read -> Refine" loop.

### Evaluation & Benchmarks (Section 7)
Use these benchmarks to test specific modules:
*   **WebArena**: Identifying if the agent can successfully navigate websites.
*   **DeepResearch Bench / GAIA**: Testing the full pipeline (from question to report).
*   **GPQA**: Testing expert-level reasoning capabilities.

### Limitations & Future Goals (Section 8)
*   **Multi-Tool Integration**: Don't limit the agent to just "Search". Give it tools to **parse code, read charts, and query databases**.
*   **Factuality**: Implement **Post-hoc Verification** (a separate step that reads the final report and checks every link).
*   **Personalization**: The agent should learn the user's preferred report style over time.

---

# Research Notes: Deep Research Agents - Roadmap (Paper 3)

**Paper:** Deep Research Agents: A Systematic Examination And Roadmap (Huang et al.)
**Source:** `pdf_content_new.txt` (Deep Research Agents Roadmap)

## Section 3: Deep Research Components (Detailed Analysis)

This section provides a granular look at the components required to build a state-of-the-art agent.

### 3.1 Search Engine: API vs. Browser
The paper explicitly compares these two paradigms, suggesting a hybrid is best.
*   **API-Based (Fast & Scalable)**:
    *   **Usage**: Interacting with structured data (Google/Bing APIs, arXiv).
    *   **Pros**: Low latency, high throughput, structured results.
    *   **Cons**: Cannot access "deep web" (JS content), expensive at scale.
    *   **Examples**: *Gemini DR* (uses Google Search), *Agent Laboratory* (uses arXiv API).
*   **Browser-Based (Deep & Dynamic)**:
    *   **Usage**: Simulating human interaction (headless Chromium).
    *   **Capabilities**: Handling dynamic JS, infinite scrolling, filling forms, downloading PDFs.
    *   **Cons**: High latency, resource-intensive, fragile (anti-bot defenses).
    *   **Examples**: *Manus AI* (sandboxed browser), *AutoGLM* (reads/clicks like a human).

### 3.2 Tool Use: Empowering Functionalities
Beyond search, agents must "act" on data.
*   **Code Interpreter**: Essential for data analysis (Python/Pandas) and simulation. Almost all top agents (OpenAI DR, The AI Scientist) integrate this.
*   **Multimodal Processing**: Using Vision models to "read" charts, diagrams, and PDFs. *Groq DeepSearch* and *Gemini* lead here.
*   **Computer Use**: Direct interaction with OS/GUI (e.g., *AutoGLM Rumination*).
*   **Model Context Protocol (MCP)**: The standard for extending agent tools. Allows "plug-and-play" of new capabilities without retraining.

### 3.3 Architecture & Workflow
*   **Planning Strategies**:
    1.  **Planning-Only**: Agent makes a plan immediately (e.g., *Manus*).
    2.  **Intent-to-Plan**: Agent asks user qualifying questions *before* planning (*OpenAI DR*).
    3.  **Unified**: Agent drafts a plan and asks user to confirm/edit (*Gemini DR*). **Recommendation: Use Unified.**
*   **Single vs. Multi-Agent**:
    *   **Single-Agent**: Easier to train end-to-end with RL. Good for coherence.
    *   **Multi-Agent**: Planner -> Searcher -> Writer. Harder to coordinate but scales better for complex tasks.
*   **Memory**:
    *   **Context Window**: Brute force (1M tokens).
    *   **Compression**: Summarizing steps to save tokens (*AI Scientist*).
    *   **External Storage**: Storing findings in a Vector DB or Knowledge Graph (*Agentic Reasoning*).

### 3.4 Tuning Strategies ("Beyond Prompting")
Prompting is not enough for an expert agent.
*   **SFT (Supervised Fine-Tuning)**:
    *   *Open-RAG*: Adversarial training to help agent ignore irrelevant retrieval results.
    *   *Auto-RAG*: Training agents to *ask* questions, not just answer them.
*   **Reinforcement Learning (RL)**:
    *   **GRPO (Group Relative Policy Optimization)**: Preferred over PPO. Used by *Agent-R1*. Reduces variance by comparing a group of outputs rather than a value function.
    *   **Tool-Integrated Reasoning (TIR)**: Rewarding the model not just for the answer, but for *choosing the right tool* (e.g., using Python for math instead of guessing).

### 3.5 Non-Parametric Continual Learning
How the agent improves *without* retraining weights.
*   **Case-Based Reasoning (CBR)**: Saving successful "search trajectories" (plans) to a database. When a new task comes in, find a similar past plan and reuse it (*AgentRxiv*).
*   **Workflow Evolution**: Dynamically instantiating new MCP servers based on task needs (*Alita*).

## Section 6: Challenges & Future Directions (Actionable Insights)

### 1. Broaden Information Sources (Beyond Web)
*   **Constraint**: Search engines only see the "surface web".
*   **Action**: Integrate **MCP** to access proprietary databases (SQL, internal docs, Bloomberg Terminal).
*   **AI-Native Browsers**: Use tools like **Browserbase** or **Perplexity Comet** instead of standard Selenium. They offer structured DOMs and anti-bot handling out of the box.

### 2. Fact Checking & "Rumination"
*   **Action**: Implement a **"Rumination Loop"**. After generating an answer, the agent should:
    1.  Pause.
    2.  Search for *contradictory* evidence.
    3.  Rate source credibility.
    4.  Only then finalize the output.
*   **Goal**: Reduce hallucination by actively trying to disprove itself.

### 3. Asynchronous Parallel Execution
*   **Action**: Move away from linear "Step 1 -> Step 2". Use a **DAG (Directed Acyclic Graph)** scheduler.
*   **Benefit**: If searching for "Data A" and "Data B" are independent, run them in parallel to cut latency by 50%.

### 4. Benchmark Misalignment
*   **Insight**: Don't trust *SimpleQA* or static benchmarks (models memorize them).
*   **Action**: Test on **BrowserComp** or **FreshWiki** (real-time, open-web tasks) to measure true research capability.

---

# Research Notes: DeepResearcher (Paper 4)

**Paper:** DeepResearcher: Scaling Deep Research via Reinforcement Learning in Real-world Environments
**Source:** `pdf_content_new.txt` (DeepResearcher PDF)

## Section 2: Related Work & Training Environments
This section contrasts "DeepResearcher" with existing methods.
*   **Prompt-Based Agents**: (e.g., OpenResearcher, Search-o1). Rely on manual prompts. *Limitation*: Brittle, rigid behavior patterns.
*   **Training-Based Agents**:
    *   **SFT (Supervised Fine-Tuning)**: (e.g., CoRAG). Uses MCTS to select documents. *Limitation*: High compute cost, weak generalization.
    *   **Reinforcement Learning (RL)**: (e.g., Search-R1). The preferred approach.
*   **Environments**:
    *   **Local RAG**: Training on fixed corpora (Wikipedia). *Problem*: Information decay, poor domain adaptability.
    *   **Real-World Web**: Training on the *live internet*. This is the core innovation of DeepResearcher. It forces the agent to handle API rate limits, latency, and anti-bot defenses during training.

## Section 3: Methodology (The "Deep Researcher Trajectory")
The paper proposes a specific lifecycle for handling a research task:
1.  **Reasoning (<think>)**: The agent *must* output a thought block before acting.
2.  **Web Search Tool**: Generates a JSON request (`web_search(query)`).
3.  **Browsing Agent (Key Component)**:
    *   Maintains **Short-Term Memory** for the current query.
    *   Reads the *first segment* of a URL.
    *   Decides: **Continue Reading** OR **Stop & Summarize**.
    *   This "Browsing Agent" is a separate module that feeds info back to the main "DeepResearcher" system.
4.  **Answering**: outputs `<answer>` only when sufficient info is gathered.

### Handling Real-World Challenges
*   **High Concurrency**: Uses a distributed cluster (50 nodes) to handle 4096 parallel browser requests during RL training (!).
*   **Anti-Crawling/Rate Limits**: Implements a **Robust Retry Mechanism** and **7-Day Cache** to avoid hitting API limits repeatedly.
*   **Multi-Agent Extraction**: A dedicated "Reading Agent" scans long pages segment-by-segment to determine if they are worth processing, saving tokens.

## Section 4: Training with "Search-Dependent" Data
*   **Data Contamination**: A huge risk. Large models already "know" the answers to famous questions (e.g., "Capital of France") without searching.
*   **Solution**:
    *   **Filtering**: Remove time-sensitive or subjective questions ("Best smartphone?").
    *   **Contamination Check**: Ask the base model the question *without* tools. If it answers correctly, **exclude it from training**. We want the model to learn *how to search*, not just recite facts.

## Section 5: Experiments & Results
*   **Benchmarks Used**: NQ, TriviaQA (Simple), HotpotQA, 2Wiki (Multi-hop), Bamboogle (Out-of-domain).
*   **Key Finding**: DeepResearcher outperforms RAG-based agents (like Search-r1-base) significantly on **Out-of-Domain** tasks (Bamboogle), proving that training on the live web creates better generalists than training on Wikipedia.

## Section 6: Emerging Cognitive Behaviors (Analysis)
End-to-end RL training produced four distinct "emergent" behaviors without explicit programming:
1.  **Dynamic Planning**: Merging steps or changing plans mid-stream when a search fails.
2.  **Cross-Validation**: Finding an answer in Step 1, but *continuing to search* to verify it against a second source.
3.  **Reflection**: Detecting when search results don't match the user intent and refining the query.
4.  **Honesty**: Recognizing when the answer *cannot* be found and explicitly stating "I don't know" or "Significant portion (but exact number unknown)" instead of hallucinating.

---

## Project Applicability: DeepResearcher for Deep-Research-Agent

### Feasibility & Complexity
*   **High Complexity**: Implementing the full "DeepResearcher" pipeline is **extremely ambitious**. It requires:
    *   **Distributed Infrastructure**: The paper used 50 nodes just for browsing. We likely cannot replicate this scale on a local desktop.
    *   **RL Training Pipeline**: Requires `verl` framework, GRPO, and a massive curated dataset.
    *   **Cost**: Live web-browsing during training is very expensive (API costs).

### Pros (What we should adopt)
1.  **The "Browsing Agent" Logic**: The idea of a specialized sub-agent that reads a URL segment-by-segment and decides "Continue?" or "Stop?" is **highly applicable** and implementable without RL. We should steal this logic for our `read_url` tool to handle long pages.
2.  **Contamination Detection**: When testing our agent, we must ensure we aren't just testing its internal memory. We should pick questions that *require* live data (e.g., "Events from last week").
3.  **Cross-Validation Loop**: We can hard-code a "Reflection Step" (as seen in Behavior #2) where the agent is forced to double-check its answer before finishing.

### Cons (What we should avoid)
1.  **End-to-End RL Training**: We likely don't have the compute to *train* our own 7B model from scratch using RL on the open web. We should rely on **Prompt Engineering** and **In-Context Learning** (few-shot prompting) to mimic the behaviors DeepResearcher learned (Planning, Reflection, Honesty) rather than training for them.

### Final Verdict
**Adopt the Architecture, Skip the Training.** We can build a "DeepResearcher-Lite" by using a smart "Planner-Browser-Reflector" workflow prompted with LLMs like GPT-4o or DeepSeek-R1, which already have some reasoning capabilities, rather than fine-tuning a Qwen-7B model from scratch.

---

# Research Notes: Benchmark Analysis

## Comparative Overview of Benchmarks

We have analyzed five key benchmarks to understand how to evaluate our Deep Research Agent. Each benchmark targets a different aspect of the research pipeline, from retrieval accuracy to reasoning depth and report quality.

### Comparison Table

| Benchmark | Task Type | Key Focus | Evaluation Metric | Applicability |
| :--- | :--- | :--- | :--- | :--- |
| **DeepResearch Bench** | Long-form Reports | Quality of synthesized reports | RACE (Rubrics) & FACT (Citation checks) | **Very High**: Matches our goal of generating full research reports. |
| **DeepSearchQA** | Multi-hop QA | Comprehensiveness (finding *all* answers) | Recall, F1-Score, QA Categorization | **High**: Critical for ensuring our agent doesn't miss key facts. |
| **ResearchRubrics** | Open-Ended Research | Subjective quality & adherence to constraints | Rubric Adherence Score | **High**: Excellent for evaluating the final report's tone and structure. |
| **BrowseComp-Plus** | Web Retrieval | Retrieval fairness & Reproducibility | Recall@K, End-to-End Accuracy | **Medium**: Useful for tuning the search/browser tool specifically. |
| **Humanity's Last Exam** | Closed-Ended QA | Extreme difficulty / Reasoning limits | Accuracy (Exact Match) | **Low**: Good for stress-testing, but less relevant for open-ended research. |

## Detailed Benchmark Summaries

### 1. DeepResearch Bench: A Comprehensive Benchmark
*   **Paper**: DeepResearch Bench: A Comprehensive Benchmark for Deep Research Agents
*   **Source**: `research/DeepResearch Bench - A Comprehensive Benchmark for Deep Research Agents.pdf`
*   **Core Problem**: Evaluating full reports is subjective. We need a standard way to grade "PhD-level" output.
*   **Methodology**:
    *   **Task**: 100 complex research tasks across 22 domains.
    *   **RACE Framework**: Evaluates Report Quality based on **Relevance**, **Accuracy**, **Completeness**, and **Expertise**.
    *   **FACT Framework**: Automatically verifies citations to ensure they exist and support the claim.
*   **Key Capability Needed**: We should implement the **FACT** logic: a post-processing step that clicks every link in the final report to verify it works and contains the cited info.

### 2. DeepSearchQA: Bridging the Comprehensiveness Gap
*   **Paper**: DeepSearchQA: Bridging the Comprehensiveness Gap for Deep Research Agents
*   **Source**: `research/DeepSearchQA_benchmark_paper.pdf`
*   **Core Problem**: Standard RAG systems are "lazy" - they find *one* answer and stop. Real research requires finding *all* possible answers (e.g., "List all side effects of Drug X").
*   **Methodology**:
    *   Introduces **"Comprehensiveness"** as a primary metric.
    *   Uses a **900-query dataset** across 17 diverse fields.
    *   **Evaluation**: An LLM-as-a-Judge pipeline compares the agent's answer list against a Golden Set.
*   **Key Capability Needed**: Our agent must implement **Iterative Search** with a "Stopping Condition" that asks "Did I find everything?" rather than "Did I find something?".

### 3. ResearchRubrics: Evaluating Open-Ended Queries
*   **Paper**: ResearchRubrics - A Benchmark of Prompts and Rubrics
*   **Source**: `research/ResearchRubrics - A Benchmark of Prompts and Rubrics For Evaluating Deep Research Agents.pdf`
*   **Core Problem**: "Correctness" isn't enough. Research must also follow constraints (e.g., "Use a professional tone", "Include 3 case studies").
*   **Methodology**:
    *   Created **2,500+ detailed rubrics** for open-ended queries.
    *   Evaluates based on **Constraint Satisfaction** (did the agent follow instructions?) rather than just fact retrieval.
*   **Key Capability Needed**: Our "Planner" module should parse the user's prompt to extract **Constraints** (formatting, tone, length) and convert them into a self-grading rubric for the agent to use before submitting.

### 4. BrowseComp-Plus: Fair & Transparent Evaluation
*   **Paper**: BrowseComp-Plus - A More Fair and Transparent Evaluation Benchmark
*   **Source**: `research/BrowseComp-Plus - A More Fair and Transparent Evaluation Benchmark of Deep-Research Agent.pdf`
*   **Core Problem**: When an agent fails, is it because the *search engine* was bad, or the *agent* was bad? Most benchmarks conflate the two.
*   **Methodology**:
    *   Provides a **Fixed Corpus** (cached webpages) to ensure reproducibility.
    *   Separately measures **Retriever Performance** (did the search tool find the page?) and **Agent Performance** (did the agent answer correctly given the page?).
*   **Key Capability Needed**: We should support **"Cached Mode"** in our agent for debugging, allowing us to replay a research session with fixed search results to tune the reasoning logic.

### 5. Humanity's Last Exam (HLE)
*   **Paper**: Humanity's Last Exam
*   **Source**: `research/Humanity's Last Exam.pdf`
*   **Core Problem**: LLMs are saturating current benchmarks (MMLU). We need a test they *fail*.
*   **Methodology**:
    *   A dataset of **3,000 extreme-difficulty questions** (math, abstract reasoning) where SOTA models score <5%.
    *   Multimodal (includes images/diagrams).
    *   **Strictly Closed-Ended**: Answers are verified by exact string match or multiple choice.
*   **Key Capability Needed**: While we aren't building a math solver, this benchmark highlights the need for **Multimodal Processing** (reading charts/graphs) to handle complex queries.
