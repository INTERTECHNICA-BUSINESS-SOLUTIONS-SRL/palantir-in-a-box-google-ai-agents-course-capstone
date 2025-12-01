# 🔮PALANTIR IN A BOX 
**Using Agentic AI for Intelligence Analysis Operations**

**Palantir in a Box** is a sophisticated, production-oriented intelligence analysis system driven by a coordinated network of specialized AI agents. 
Built as a capstone project for the **Google AI Agents Course**, it demonstrates how structured Agentic AI can autonomously execute complex analytical workflows 
using the **Analysis of Competing Hypotheses (ACH)**—a proven methodology for reducing analytical bias.

Beyond simple automation, this project showcases **enterprise-grade patterns** for multi-agent orchestration, intelligent tool integration and automated report generation. 
It transforms the abstract concept of "AI Agents" into a deployable, audit-ready architecture capable of rigorous strategic reasoning.

## ⚡ Quickstart

**Prerequisite:** Python **3.12.2** or higher is required.

1.  **Configure Environment**
    Create a `.env` file in the root directory using the structure provided in the `.env.example` file.
    *   *Provide your `GOOGLE_API_KEY` to enable model access.*

2.  **Initialize Virtual Environment**
    Create and activate a Python virtual environment to manage dependencies in isolation.

3.  **Run the Analysis**
    Launch and execute the `intelligence_analyst.ipynb` notebook.
    *   *This will automatically install all the necessary dependencies and execute the full analysis workflow.*

> **ℹ️ Stability Note:** Due to the stochastic nature of Agentic AI and high computational load, the workflow may occasionally fail to retrieve evidence or complete execution. If this occurs, **restarting the notebook usually resolves the issue**. Basic retry mechanisms are implemented, and advanced guardrails may be planned for future releases.

## 🔎 Core Intelligence Analysis Workflow

The system follows a structured, 7-phase analytical process designed to mirror professional intelligence tradecraft. Each phase is executed by a dedicated Agent Factory, ensuring strict separation of concerns:

<img width="2660" height="1560" alt="competing_hypothesis_analysis_workflow" src="https://github.com/user-attachments/assets/863dbb91-4a20-4b9b-aaa0-dd7b7249fc0f" />

| Phase | Agent Implementation | Responsibility |
| :--- | :--- | :--- |
| **1. Hypothesis Formulation** | `Hypotheses Extraction Agent` | Parses analyst queries to structure mutually exclusive competing scenarios. |
| **2. Source Curation** | `Web Information Agent` | Retrieves targeted, primary source data from the curated source registry. |
| **3. Evidence Collection** | `Evidence Structuring Agent` | Transforms raw content into machine-interpretable JSON with full metadata. |
| **4. Evidence Analysis** | `Evidence Detailed Analysis Agent` | Vets evidence for relevance, reliability, and diagnostic value (QA). |
| **5. ACH Evaluation** | `Competing Hypotheses Matrix Agent` | Systematically scores evidence consistency against hypotheses using the ACH matrix. |
| **6. Executive Assessment** | `Executive Review Agent` | Synthesizes matrix data into confidence-weighted judgments and eliminates weak theories. |
| **7. Actionable Intelligence** | `Actionable Information Agent` | Derives specific, time-bound operational recommendations and next steps. |

**Result:** The system delivers a complete, auditable intelligence product—featuring ranked hypotheses, evidence traceability, and actionable recommendations—produced entirely through autonomous, bias-resistant intelligence analysis.

## 📑 Content Curation & Processing

To ensure the integrity of the analysis, the system employs a dedicated **Content Processing Sub-Workflow**. This nested pipeline acts as a comprehensive data refinery, progressively transforming raw web data into structured analytical assets.

<img width="2660" height="1300" alt="document_content_assembling_workflow" src="https://github.com/user-attachments/assets/40b73498-59fb-4e5a-ba13-bf9b2e42e8c4" />

| Phase | Agent Implementation | Responsibility |
| :--- | :--- | :--- |
| **1. Content Retrieval** | `Content Retrieval Agent` | Fetches raw HTML/text from vetted web sources. |
| **2. Title Extraction** | `Content Title Extraction Agent` | Extracts and normalizes the document title. |
| **3. Author Identification** | `Content Authors Extraction Agent` | Identifies and structures author information. |
| **4. Sanitization** | `Content Cleanup Agent` | Sanitizes and removes noise (ads, scripts, formatting artifacts). |
| **5. Summarization** | `Content Summarization Agent` | Generates a concise summary of the cleaned content. |
| **6. Keyword Extraction** | `Content Keywords Extraction Agent` | Identifies key topics and entities. |
| **7. Assembly** | `Document Information Assembling Agent` | Aggregates all extracted metadata into a unified, structured document object. |

**Result:** Downstream analysis agents receive only fully enriched, normalized, and structured data, eliminating the noise and context pollution common in standard LLM chat usage.

## 🛠️ Technology Stack

This stack prioritizes **modularity, safety, reproducibility, and cost-efficiency** while maintaining the integrity required for audit-grade intelligence analysis.

| Technology | Justification |
| :--- | :--- |
| **Python 3** | Primary language for cross-platform, readable agent and workflow implementation. |
| **Google ADK** | Provides the agentic framework with `Agent` and `SequentialAgent` for modular, composable multi-agent orchestration. |
| **Google Gemini 2.5 Flash Lite** | Lightweight LLM optimized for cost-efficiency and speed while maintaining reasoning capability for structured analysis tasks. |
| **TinyDB** | Embedded, file-based JSON database for persistent caching of raw and curated content, reducing redundant API calls. |
| **Pydantic** | Enforces strict data validation and structured schema definitions for agent outputs, ensuring type safety and reproducibility. |
| **Jinja2** | Templating engine for generating professional, dynamic report content with consistent formatting and data binding. |
| **xhtml2pdf** | Converts structured HTML reports into production-grade PDF documents with proper typography and layout control. |
| **Markdownify** | Converts raw HTML content into clean Markdown for normalized, machine-interpretable text processing. |
| **Mistletoe** | Markdown parser for rendering and processing markdown content during report generation and dissemination. |
| **AsyncIO & nest_asyncio** | Enables non-blocking, concurrent agent execution for efficiency and asynchronous I/O handling in nested event loops. |
| **Python-dotenv** | Manages environment variables (API keys, configuration) securely without hardcoding sensitive data. |

## 📂 Project Structure

The repository is organized into modular directories to support the agentic pipeline's distinct responsibilities:

| Directory | Purpose |
| :--- | :--- |
| **`agents/`** | Contains all agent factory classes that implement specialized analytical tasks (hypotheses extraction, evidence analysis, ACH evaluation, etc.). |
| **`workflows/`** | Orchestrates agent execution flow, manages context, and implements the main intelligence pipeline (`run_workflow_analysis_of_competing_hypotheses`). |
| **`tools/`** | Utility modules for content retrieval, prompt engineering, reporting, and helper functions supporting agents across the pipeline. |
| **`content/`** | Content provider implementations for web source integration, caching layers, and data retrieval strategies. |
| **`agent_runners/`** | Agent execution engines handling asynchronous/synchronous modes, event loop management, and runtime orchestration. |
| **`0_0_1_data_sources/`** | Registry of curated, pre-vetted web sources used for evidence retrieval; ensures data governance and source reliability. |
| **`0_0_2_cache/`** | Runtime cache storage for raw and processed content, enabling persistent storage of intermediate results. |
| **`0_0_3_templates/`** | Report generation templates (HTML, Markdown, Jinja2) and CSS styling for professional document rendering. |
| **`0_0_4_reports/`** | Output directory for generated intelligence reports (PDFs, metadata files) produced by the workflow execution. |

### 📄 Key Project Files

| File | Purpose |
| :--- | :--- |
| **`intelligence_analyst.ipynb`** | **Primary Demo Interface.** Interactive Jupyter notebook demonstrating the complete workflow. Users can execute ACH analysis, inspect intermediate reasoning, and visualize final markdown reports. |
| **`setup.py`** | Environment initialization module. Configures the runtime, initializes Google Gemini API keys, sets up logging, and prepares dependencies for agentic execution. |
| **`.env.example`** | Template for system configuration. Defines the necessary credentials for Google AI services and specifies the target Language Model baseline for the agent fleet. |





