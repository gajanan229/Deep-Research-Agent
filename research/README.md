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
