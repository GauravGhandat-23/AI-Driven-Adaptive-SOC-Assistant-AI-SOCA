import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables from .env if available
load_dotenv()

# -----------------------------
# Groq API Wrapper
# -----------------------------
def query_groq(prompt):
    from groq import Groq

    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY not found in environment variables.")

    client = Groq(api_key=api_key)

    completion = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4,
        max_completion_tokens=1024,
        top_p=0.9,
        stream=True,
    )

    result = ""
    for chunk in completion:
        result += chunk.choices[0].delta.content or ""

    return result


# -----------------------------
# Streamlit Page
# -----------------------------
st.set_page_config(
    page_title="AI-SOCA",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -----------------------------
# Hacker UI CSS (Advanced)
# -----------------------------
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700;900&family=Share+Tech+Mono&display=swap');

:root{
    --neon:#00ff9c;
    --neon-dim:#00ff9c55;
    --neon-soft:#66ffcc;
    --bg-black:#020403;
}

html, body, [class*="css"]{
    background:var(--bg-black);
    color:var(--neon);
    font-family:'Share Tech Mono', monospace;
}

/* Animated matrix-grid background */
.stApp{
    background:
        linear-gradient(rgba(0,255,156,0.035) 1px, transparent 1px),
        linear-gradient(90deg, rgba(0,255,156,0.035) 1px, transparent 1px),
        radial-gradient(circle at top,#07160f 0%,#020403 55%,#000000 100%);
    background-size: 38px 38px, 38px 38px, cover;
    animation: gridShift 14s linear infinite;
}

@keyframes gridShift{
    0%{ background-position: 0 0, 0 0, 0 0; }
    100%{ background-position: 38px 38px, 38px 38px, 0 0; }
}

/* CRT scanline overlay */
.stApp::before{
    content:"";
    position:fixed;
    top:0; left:0; right:0; bottom:0;
    pointer-events:none;
    z-index:9999;
    background:repeating-linear-gradient(
        to bottom,
        rgba(0,255,156,0.03) 0px,
        rgba(0,255,156,0.03) 1px,
        transparent 2px,
        transparent 4px
    );
    mix-blend-mode: overlay;
}

/* Flicker vignette */
.stApp::after{
    content:"";
    position:fixed;
    top:0; left:0; right:0; bottom:0;
    pointer-events:none;
    z-index:9998;
    box-shadow: inset 0 0 180px rgba(0,0,0,0.85);
    animation: flicker 6s infinite;
}

@keyframes flicker{
    0%,19%,21%,23%,25%,54%,56%,100%{ opacity:1; }
    20%,24%,55%{ opacity:0.92; }
}

/* Hide Streamlit Branding */
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

/* Sidebar */
section[data-testid="stSidebar"]{
    background:linear-gradient(180deg,#060a07 0%,#020403 100%);
    border-right:1px solid var(--neon-dim);
    box-shadow: 4px 0 25px rgba(0,255,156,0.08);
}

section[data-testid="stSidebar"] h2{
    font-family:'Orbitron', sans-serif;
    letter-spacing:1px;
    border-bottom:1px dashed var(--neon-dim);
    padding-bottom:10px;
}

/* Title with glitch effect */
.title-wrap{
    position:relative;
    text-align:center;
    margin-bottom:2px;
}

.title{
    font-family:'Orbitron', sans-serif;
    font-weight:900;
    text-align:center;
    font-size:3.4rem;
    letter-spacing:4px;
    color:var(--neon);
    text-shadow:
        0 0 10px var(--neon),
        0 0 20px var(--neon),
        0 0 40px var(--neon);
    position:relative;
    display:inline-block;
    animation: pulseGlow 3s ease-in-out infinite;
}

@keyframes pulseGlow{
    0%,100%{ text-shadow:0 0 10px var(--neon),0 0 20px var(--neon),0 0 40px var(--neon); }
    50%{ text-shadow:0 0 4px var(--neon),0 0 10px var(--neon),0 0 22px var(--neon); }
}

.title::before,
.title::after{
    content:"AI-SOCA";
    position:absolute;
    left:0; top:0;
    width:100%;
    overflow:hidden;
    background:transparent;
}

.title::before{
    color:#ff2b6d;
    left:2px;
    text-shadow:none;
    clip-path: inset(0 0 55% 0);
    animation: glitchTop 3.2s infinite linear alternate-reverse;
}

.title::after{
    color:#00e5ff;
    left:-2px;
    text-shadow:none;
    clip-path: inset(55% 0 0 0);
    animation: glitchBottom 2.6s infinite linear alternate-reverse;
}

@keyframes glitchTop{
    0%{ transform:translate(0,0); }
    20%{ transform:translate(-2px,-1px); }
    40%{ transform:translate(2px,1px); }
    60%{ transform:translate(-1px,0); }
    80%{ transform:translate(1px,-1px); }
    100%{ transform:translate(0,0); }
}

@keyframes glitchBottom{
    0%{ transform:translate(0,0); }
    25%{ transform:translate(2px,1px); }
    50%{ transform:translate(-2px,-1px); }
    75%{ transform:translate(1px,1px); }
    100%{ transform:translate(0,0); }
}

.subtitle{
    text-align:center;
    color:var(--neon-soft);
    font-size:15px;
    letter-spacing:2px;
    margin-bottom:6px;
}

.subtitle::after{
    content:"_";
    animation: blink 1s steps(1) infinite;
}

@keyframes blink{
    0%,49%{ opacity:1; }
    50%,100%{ opacity:0; }
}

.status-bar{
    text-align:center;
    font-size:12px;
    color:var(--neon-dim);
    letter-spacing:3px;
    margin-bottom:22px;
    text-transform:uppercase;
}

.status-bar span{
    color:var(--neon);
    margin:0 6px;
}

/* Cards */
.card{
    background:rgba(0,20,10,.45);
    border:1px solid var(--neon-dim);
    border-radius:14px;
    padding:20px;
    box-shadow:
        0 0 18px rgba(0,255,156,.18),
        inset 0 0 30px rgba(0,255,156,.04);
    backdrop-filter:blur(8px);
    position:relative;
    overflow:hidden;
}

.card::before{
    content:"";
    position:absolute;
    top:-2px; left:-2px; right:-2px; bottom:-2px;
    border-radius:14px;
    padding:1px;
    background:linear-gradient(120deg, transparent, var(--neon), transparent);
    background-size:200% 200%;
    animation: borderSweep 5s linear infinite;
    -webkit-mask:
        linear-gradient(#fff 0 0) content-box,
        linear-gradient(#fff 0 0);
    -webkit-mask-composite: xor;
    mask-composite: exclude;
    pointer-events:none;
    opacity:.6;
}

@keyframes borderSweep{
    0%{ background-position:0% 50%; }
    100%{ background-position:200% 50%; }
}

/* Buttons */
.stButton>button{
    width:100%;
    background:linear-gradient(135deg,#00ff9c,#00cf82);
    color:black;
    border:none;
    border-radius:10px;
    padding:12px;
    font-weight:bold;
    letter-spacing:1px;
    transition:.25s;
    font-family:'Orbitron';
    box-shadow:0 0 12px rgba(0,255,156,.35);
}

.stButton>button:hover{
    background:linear-gradient(135deg,#00ffaa,#00e69a);
    transform:scale(1.02);
    box-shadow:0 0 30px var(--neon), 0 0 60px rgba(0,255,156,.25);
}

.stButton>button:active{
    transform:scale(0.98);
}

/* Inputs */
textarea,
input,
.stTextInput input{
    background:#08120d !important;
    color:var(--neon) !important;
    border:1px solid var(--neon-dim) !important;
    border-radius:8px !important;
    font-family:'Share Tech Mono', monospace !important;
}

textarea:focus,
input:focus{
    border:1px solid var(--neon) !important;
    box-shadow:0 0 14px rgba(0,255,156,.35) !important;
}

.stSelectbox div[data-baseweb="select"]{
    background:#08120d;
    color:var(--neon);
    border:1px solid var(--neon-dim);
    border-radius:8px;
}

/* Expanders */
.streamlit-expanderHeader{
    color:var(--neon);
    font-weight:bold;
    background:rgba(0,255,156,0.04);
    border:1px solid var(--neon-dim);
    border-radius:8px;
}

/* Result Box */
.result{
    background:#06110c;
    border-left:5px solid var(--neon);
    border-radius:10px;
    padding:18px;
    box-shadow:0 0 18px rgba(0,255,156,.18);
    position:relative;
}

.result::before{
    content:"root@ai-soca:~$ output";
    display:block;
    font-family:'Orbitron', sans-serif;
    font-size:11px;
    letter-spacing:2px;
    color:var(--neon-dim);
    margin-bottom:10px;
    text-transform:uppercase;
}

/* Scrollbar */
::-webkit-scrollbar{
    width:8px;
}

::-webkit-scrollbar-thumb{
    background:var(--neon);
    border-radius:10px;
    box-shadow:0 0 8px var(--neon);
}

::-webkit-scrollbar-track{
    background:#020403;
}

/* Footer */
.footer-line{
    text-align:center;
    color:var(--neon);
    font-family:'Orbitron', sans-serif;
    font-size:12px;
    letter-spacing:1px;
    opacity:.85;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Header
# -----------------------------
st.markdown(
    """
    <div class="title-wrap">
        <div class="title" data-text="AI-SOCA">AI-SOCA</div>
    </div>
    <div class="subtitle">
        AI-Driven Security Operations Center Assistant
    </div>
    <div class="status-bar">
        [ SYSTEM <span>ONLINE</span> ] &nbsp;|&nbsp; [ THREAT FEED <span>ACTIVE</span> ] &nbsp;|&nbsp; [ MODEL <span>gpt-oss-120b</span> ]
    </div>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.markdown("## ⚡ AI-SOCA Control Panel")

input_type = st.sidebar.selectbox(
    "Select Analysis Type",
    [
        "Summarize Logs",
        "Recommend Playbook",
        "Contextualize CVE",
    ],
)

user_input = st.sidebar.text_area(
    "Paste your SIEM Log / Alert / CVE",
    height=250,
)

submit = st.sidebar.button("🚀 ANALYZE")

# -----------------------------
# Main Area
# -----------------------------
st.markdown('<div class="card">', unsafe_allow_html=True)

st.markdown(
    """
### 🛡 Security Intelligence

Analyze SIEM alerts, summarize security logs, recommend response playbooks,
and contextualize CVEs using AI.
"""
)

st.markdown("</div>", unsafe_allow_html=True)

st.write("")

# -----------------------------
# Analysis
# -----------------------------
if submit and user_input:

    with st.spinner("Analyzing..."):

        if input_type == "Summarize Logs":

            prompt = f"""You are an expert SOC analyst.
Summarize the following SIEM logs and highlight anomalies or incidents in concise natural language.
Do not include phrases like 'I think' or 'it seems'.

{user_input}
"""

        elif input_type == "Recommend Playbook":

            prompt = f"""You are a cybersecurity expert.
Based on the following incident details recommend an incident response playbook using MITRE ATT&CK.
Avoid uncertain language.

{user_input}
"""

        elif input_type == "Contextualize CVE":

            prompt = f"""Provide factual threat intelligence and impact analysis for the following CVE.
Avoid speculation.

{user_input}
"""

        else:
            prompt = user_input

        result = query_groq(prompt)

        st.markdown("## 🔍 AI-SOCA Result")

        st.markdown(
            f"""
<div class="result">

{result}

</div>
""",
            unsafe_allow_html=True,
        )

# -----------------------------
# Chat Section
# -----------------------------
with st.expander("💬 AI-SOCA Chat"):

    chat_input = st.text_input(
        "Ask a question about your SOC environment"
    )

    if st.button("Send") and chat_input:

        response = query_groq(chat_input)

        st.markdown(
            f"""
<div class="result">

{response}

</div>
""",
            unsafe_allow_html=True,
        )

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")

st.markdown(
    """
<div class="footer-line">
Built By Gaurav Ghandat using Python, Streamlit, and Groq API (openai/gpt-oss-120b)
</div>
""",
    unsafe_allow_html=True,
)