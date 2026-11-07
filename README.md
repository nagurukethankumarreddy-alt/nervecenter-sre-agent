# ⚡ NerveCenter: SRE Memory Agent

![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32+-red.svg)
![Groq](https://img.shields.io/badge/Groq-Inference-orange.svg)
![Vectorize](https://img.shields.io/badge/Vectorize-Hindsight-green.svg)
![License](https://img.shields.io/badge/License-MIT-purple.svg)

**NerveCenter** is an enterprise-grade Site Reliability Engineering (SRE) command agent designed to instantly resolve P1/P2 production outages. By augmenting Large Language Models (LLMs) with a dynamic vector memory layer, NerveCenter replaces generic, hallucinated troubleshooting advice with hyper-specific, historically grounded incident runbooks.

---

## 📑 Table of Contents
1. [The Problem](#-the-problem)
2. [The Solution](#-the-solution)
3. [System Architecture](#-system-architecture)
4. [Core Features](#-core-features)
5. [Installation & Setup](#-installation--setup)
6. [Demo Scenarios](#-demo-scenarios)
7. [Team sync4ce](#-team-sync4ce)

---

## 🚨 The Problem
During a P1 outage, every minute of downtime costs an enterprise thousands of dollars. Standard AI assistants fail in these scenarios because they lack organizational context. They provide generic textbook advice (e.g., "Check your database connection") and frequently hallucinate destructive CLI commands that can worsen the outage. 

## 💡 The Solution
NerveCenter integrates **Vectorize Hindsight Memory** to give the AI institutional knowledge. When an alert fires, NerveCenter queries the vector database for similar past incidents in your specific environment, retrieves the exact commands used to fix it, and reads the post-mortem notes to prevent engineers from repeating past mistakes.

---

## 🏗️ System Architecture

*   **Frontend / UI:** [Streamlit](https://streamlit.io/) - Provides a rapid, responsive Command Dashboard with live telemetry and system metrics.
*   **Agentic Core:** [Groq Inference Engine](https://groq.com/) - Utilizes the massive `openai/gpt-oss-120b` model to generate complex terminal commands and runbooks at ultra-low latency.
*   **Memory Layer:** [Vectorize Hindsight](https://vectorize.io/) (Simulated via HindsightMemoryEngine) - Acts as the agent's long-term memory, injecting historical incident data directly into the active LLM context window.

---

## 🚀 Core Features

*   **Contextual Hindsight Retrieval:** Stops AI hallucinations by grounding responses strictly in your organization's real incident history.
*   **Transparent Execution Logs:** Exposes the raw retrieved JSON logs in the UI so engineers can verify the data the AI is basing its decisions on.
*   **Terminal Command Generation:** Outputs precise, copy-pasteable CLI commands to triage degraded clusters immediately.
*   **Post-Mortem Safeguards:** Actively warns engineers of secondary consequences (e.g., latency spikes, dropped packets) caused by remediation steps during past outages.

---

## ⚙️ Installation & Setup

### Prerequisites
*   Python 3.10+
*   Groq API Key

### Local Deployment
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/nagurukethankumarreddy-alt/nervecenter-sre-agent.git](https://github.com/nagurukethankumarreddy-alt/nervecenter-sre-agent.git)
   cd nervecenter-sre-agent
   ```
2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   # On Windows use: venv\Scripts\activate
   source venv/bin/activate  
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Configure Environment Variables:**
   Create a `.env` file in the root directory and add your key:
   ```env
   GROQ_API_KEY="your_groq_api_key_here"
   ```
5. **Run the Application:**
   ```bash
   python -m streamlit run app.py
   ```

---

## 🧪 Demo Scenarios

To see the power of Hindsight Memory, toggle the Memory Layer to **ACTIVE** in the sidebar and test these real-world production prompts:

1. **Scenario 1: Redis Crash**
   * *Prompt:* `Redis OOM Error`
   * *Agent Action:* Retrieves INC-892, outputs the `FLUSHALL ASYNC` command, and warns about latency spikes.
2. **Scenario 2: Database Lockup**
   * *Prompt:* `Postgres Deadlock detected on the checkout database`
   * *Agent Action:* Retrieves INC-904, advises terminating the PID, and suggests exponential backoff.
3. **Scenario 3: Container Failure**
   * *Prompt:* `Kubernetes pods failing with CrashLoopBackOff`
   * *Agent Action:* Retrieves INC-911, diagnoses a liveness probe timeout, and provides the `kubectl` fix.

---

## 👥 Team sync4ce
Built collaboratively by:
*   **Naguru Kethan Kumar Reddy** (Team Leader)
*   **Namita Sherakhane** 
*   **Manya Agarwal** 
*   **Joshika Kuntimaddi** 

*Developed as a proof-of-concept for intelligent, memory-augmented DevOps automation.*
