\# ⚡ NerveCenter: SRE Memory Agent



NerveCenter is an enterprise-grade Site Reliability Engineering (SRE) agent designed to instantly resolve P1/P2 production outages. By integrating LLMs with a dynamic vector memory layer, NerveCenter replaces generic troubleshooting advice with hyper-specific, historically grounded incident runbooks.



\## 🏗️ Architecture

\*   \*\*Frontend Interface:\*\* Streamlit (Python) for rapid SRE dashboard deployment and telemetry visualization.

\*   \*\*Agentic Core:\*\* Powered by the `openai/gpt-oss-120b` model via the Groq Inference Engine for ultra-low latency generation.

\*   \*\*Memory Layer:\*\* Vectorize Hindsight integration. The agent seamlessly recalls past infrastructure incidents (e.g., Redis OOM, Postgres Deadlocks) and injects past post-mortem checklists directly into the active prompt context.



\## 🚀 Key Features

\*   \*\*Contextual Hindsight:\*\* Stops AI hallucinations by grounding responses in your organization's real incident history.

\*   \*\*Terminal Command Generation:\*\* Outputs precise, copy-pasteable CLI commands to triage degraded clusters.

\*   \*\*Post-Mortem Safeguards:\*\* Actively warns engineers of secondary consequences (e.g., latency spikes) caused by remediation steps during past outages.



\## 👥 Team sync4ce

Built collaboratively by:

\*   \*\*Naguru Kethan Kumar Reddy\*\* (Team Leader)

\*   \*\*Namita Sherakhane\*\* (Member)

\*   \*\*Manya Agarwal\*\* (Member)

\*   \*\*Joshika Kuntimaddi\*\* (Member)



\## ⚙️ Local Installation

```bash

git clone \[https://github.com/nagurukethankumarreddy-alt/nervecenter-sre-agent.git](https://github.com/nagurukethankumarreddy-alt/nervecenter-sre-agent.git)

cd nervecenter-sre-agent

pip install -r requirements.txt

python -m streamlit run app.py

