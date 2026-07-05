# 🛡️ AI-SOCA -- AI-Driven Adaptive Security Operations Center Assistant

```{=html}
<p align="center">
```
`<img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python">`{=html}
`<img src="https://img.shields.io/badge/Streamlit-Latest-red?style=for-the-badge&logo=streamlit">`{=html}
`<img src="https://img.shields.io/badge/Groq-LLM-black?style=for-the-badge">`{=html}
`<img src="https://img.shields.io/badge/Cybersecurity-SOC-success?style=for-the-badge">`{=html}
```{=html}
</p>
```
## 🚀 Overview

AI-SOCA is an enterprise-inspired AI Security Operations Center
assistant built with **Python**, **Streamlit**, and the **Groq API**. It
helps SOC analysts triage alerts, summarize logs, contextualize CVEs,
recommend MITRE ATT&CK aligned playbooks, and interact with security
data through a conversational interface.

## ✨ Highlights

-   AI-powered SIEM log analysis
-   Incident severity classification
-   MITRE ATT&CK mapping
-   IOC extraction (IPs, hashes, domains, users, processes)
-   CVE contextualization and risk analysis
-   AI SOC chat assistant
-   Modern cyber-themed Streamlit dashboard
-   Streaming LLM responses via Groq

## 🏗️ Architecture

``` text
SIEM / Logs / CVEs
        │
        ▼
 Streamlit Dashboard
        │
 Prompt Engineering
        │
        ▼
     Groq LLM API
        │
        ▼
 Threat Summary • MITRE Mapping • Recommendations • IOC Extraction
```

## 🧩 Features

  -----------------------------------------------------------------------
  Module                      Description
  --------------------------- -------------------------------------------
  Log Summarization           Converts raw security logs into
                              analyst-friendly summaries

  Playbook Generator          Produces incident response guidance

  CVE Analyzer                Explains impact, exploitation, mitigations

  AI Chat                     Ask security questions in natural language

  IOC Extraction              Detects IPs, hashes, users, processes and
                              domains

  Threat Prioritization       Estimates severity and recommended actions
  -----------------------------------------------------------------------

## 🛠 Technology Stack

-   Python
-   Streamlit
-   Groq API
-   openai/gpt-oss-120b
-   python-dotenv

## 📦 Installation

``` bash
git clone https://github.com/yourusername/AI-SOCA.git
cd AI-SOCA

python -m venv .venv

# Windows
.venv\Scripts\activate

pip install -r requirements.txt
```

Create a `.env`

``` env
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

Run

``` bash
streamlit run app.py
```

## 🧪 Sample Use Cases

-   Windows authentication attacks
-   Linux privilege escalation
-   PowerShell abuse
-   Malware execution
-   Ransomware detection
-   Firewall analysis
-   DNS tunneling
-   Web attacks (SQLi / XSS)
-   Threat hunting
-   SOC reporting

## 📈 Roadmap

-   Threat intelligence integration
-   Sigma rule generation
-   YARA rule suggestions
-   Splunk integration
-   Microsoft Sentinel integration
-   Wazuh integration
-   Elasticsearch support
-   PDF incident reports
-   Multi-user authentication
-   Case management

## 🤝 Contributing

Issues, feature requests, and pull requests are welcome.

## 👨‍💻 Author

**Gaurav Ghandat**

-   Cyber Security & Ethical Hacking
-   SOC Analyst \| Blue Team \| SIEM \| Incident Response

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
