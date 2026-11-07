import streamlit as st
import os
import time
from groq import Groq
from dotenv import load_dotenv

# ==========================================
# 1. INITIALIZATION & CONFIGURATION
# ==========================================
load_dotenv()

try:
    groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))
except Exception as e:
    st.error("Critical: Failed to initialize Groq client. Check .env file.")

# Official recommended working model for the hackathon
MODEL = "openai/gpt-oss-120b" 

# ==========================================
# 2. ENHANCED HINDSIGHT MEMORY ENGINE
# ==========================================
class HindsightMemoryEngine:
    """
    Production-grade simulation of the Vectorize Hindsight API.
    Contains diverse, real-world DevOps scenarios.
    """
    def __init__(self):
        self.memory_bank = {
            "redis": """
            [Hindsight ID: INC-892 | Date: 2026-10-28 | Severity: P1]
            Symptom: Redis OOM (Out of Memory) Error on Primary API Cluster.
            Root Cause: Stale session keys failed to expire due to a misconfigured TTL policy.
            Resolution: Executed `redis-cli FLUSHALL ASYNC`. Scaled ElastiCache node to r6g.2xlarge.
            Post-Mortem: The FLUSHALL command caused a 12-second latency spike. Route traffic to standby cluster before flushing next time.
            """,
            "postgres": """
            [Hindsight ID: INC-904 | Date: 2026-11-02 | Severity: P1]
            Symptom: PostgreSQL Deadlocks on Checkout DB.
            Root Cause: Concurrent batch updates locking the `orders` table during peak traffic.
            Resolution: Identified blocking PID using `pg_stat_activity`. Terminated via `SELECT pg_terminate_backend(pid)`. 
            Post-Mortem: Implement application-level retry logic with exponential backoff for batch updates.
            """,
            "kubernetes": """
            [Hindsight ID: INC-911 | Date: 2026-11-05 | Severity: P2]
            Symptom: Kubernetes Pods in CrashLoopBackOff (Payment Service).
            Root Cause: Liveness probe failing due to connection timeout to third-party payment gateway.
            Resolution: Increased liveness probe timeout from 3s to 10s in `deployment.yaml`. Applied via `kubectl apply -f`.
            Post-Mortem: Do not fail liveness probes on external API latency; use readiness probes for external dependencies.
            """
        }

    def recall(self, query):
        query = query.lower()
        if "redis" in query or "oom" in query: return self.memory_bank["redis"]
        if "postgres" in query or "deadlock" in query: return self.memory_bank["postgres"]
        if "kubernetes" in query or "crashloop" in query or "pod" in query: return self.memory_bank["kubernetes"]
        return None

memory_engine = HindsightMemoryEngine()

# ==========================================
# 3. ENTERPRISE DASHBOARD UI
# ==========================================
st.set_page_config(page_title="NerveCenter | SRE Agent", page_icon="⚡", layout="wide")

st.title("⚡ NerveCenter: Command Dashboard")
st.markdown("Automated P1/P2 Incident Resolution via **Hindsight Agentic Memory**.")

# Telemetry Metrics Layer
col1, col2, col3, col4 = st.columns(4)
col1.metric("System Status", "Degraded", "-1 Cluster")
col2.metric("Active Alerts", "1", "P1 Severity")
col3.metric("Hindsight DB", "Connected", "32ms ping")
col4.metric("Agent Model", MODEL, "Active")
st.markdown("---")

st.sidebar.header("⚙️ Agent Settings")
use_hindsight = st.sidebar.toggle("🧠 Enable Hindsight Memory", value=True)

if use_hindsight:
    st.sidebar.success("Vectorize Hindsight Layer: ACTIVE")
else:
    st.sidebar.warning("Vectorize Hindsight Layer: DISABLED")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ==========================================
# 4. AGENTIC ROUTING & RESPONSE
# ==========================================
user_input = st.chat_input("Enter production alert (e.g., 'Postgres Deadlock', 'Kubernetes Pod Crash')...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    system_prompt = (
        "You are an elite Site Reliability Engineer (SRE) AI. "
        "Provide exact terminal commands, root cause analysis, and post-mortem advice for server outages. "
        "Structure your response with clear markdown headings."
    )
    
    if use_hindsight:
        with st.spinner("Querying Hindsight Vector DB..."):
            time.sleep(0.8) # Simulate realistic network latency for the DB call
            retrieved_context = memory_engine.recall(user_input)
        
        if retrieved_context:
            with st.expander("🔍 View Retrieved Hindsight Memory Log", expanded=True):
                st.code(retrieved_context.strip(), language="log")
            
            system_prompt += (
                f"\n\nCRITICAL HINDSIGHT MEMORY:\n"
                f"You MUST base your solution strictly on this past incident memory. "
                f"Quote the specific commands used and highlight the post-mortem warnings:\n"
                f"{retrieved_context}"
            )
        else:
            st.info("No historical incidents found in Hindsight for this alert.")

    messages_for_llm = [{"role": "system", "content": system_prompt}]
    for m in st.session_state.messages:
        messages_for_llm.append({"role": m["role"], "content": m["content"]})

    with st.chat_message("assistant"):
        try:
            completion = groq_client.chat.completions.create(
                model=MODEL,
                messages=messages_for_llm,
                temperature=0.1, 
                max_tokens=800
            )
            response_text = completion.choices[0].message.content
            st.markdown(response_text)
            st.session_state.messages.append({"role": "assistant", "content": response_text})
        except Exception as e:
            st.error(f"API Error: {e}")