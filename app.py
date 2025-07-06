import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables from .env if available
load_dotenv()

# Sample Groq API Wrapper (Replace with actual Groq Python SDK if available)
def query_groq(prompt):
    from groq import Groq  # Assuming the user has the correct SDK installed
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY not found in environment variables.")

    client = Groq(api_key=api_key)
    completion = client.chat.completions.create(
        model="qwen-qwq-32b",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.6,
        max_completion_tokens=4096,
        top_p=0.95,
        stream=True,
        stop=None,
    )
    result = ""
    for chunk in completion:
        result += chunk.choices[0].delta.content or ""
    return result

# Streamlit UI
st.set_page_config(page_title="AI-SOCA", layout="wide")
st.title("🧠 AI-SOCA: AI-Driven SOC Assistant")
st.image("logo.png", width=500)
st.markdown("Use this tool to analyze alerts, summarize logs, recommend playbooks and contextualize CVEs.")

# Sidebar
st.sidebar.header("Inputs")
input_type = st.sidebar.selectbox("Select Analysis Type", ["Summarize Logs", "Recommend Playbook", "Contextualize CVE"])
user_input = st.sidebar.text_area("Paste your SIEM log, alert, or CVE ID:")
submit = st.sidebar.button("Analyze with AI-SOCA")

if submit and user_input:
    with st.spinner("Querying AI-SOCA (Qwen-32B via Groq)..."):
        if input_type == "Summarize Logs":
            prompt = f"You are an expert SOC analyst. Summarize the following SIEM logs and highlight any anomalies or incidents in concise natural language. Do not include phrases like 'I think' or 'it seems':\n{user_input}"
        elif input_type == "Recommend Playbook":
            prompt = f"You are a cybersecurity expert. Based on the following incident/alert details, recommend an appropriate incident response playbook using MITRE ATT&CK framework. Avoid uncertain language like 'I believe' or 'possibly'. Do not include phrases like 'I think' or 'it seems':\n{user_input}"
        elif input_type == "Contextualize CVE":
            prompt = f"Provide factual threat intelligence and impact analysis on the following CVE ID. Exclude speculative or vague statements . Do not include phrases like 'I think' or 'it seems':\n{user_input}"
        else:
            prompt = user_input

        result = query_groq(prompt)
        st.subheader("🔍 AI-SOCA Result")
        st.write(result)

# Optional voice/chat UI
with st.expander("💬 Chat with AI-SOCA"):
    chat_input = st.text_input("Ask a question about your SOC environment")
    if st.button("Chat") and chat_input:
        response = query_groq(chat_input)
        st.write(response)

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Python, Streamlit, and Groq API (Qwen-32B)")