# <p align="center"> 🛡️ AI-SOCA -- AI-Driven Adaptive Security Operations Center Assistant </p>

<p align="center">

<img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python">
<img src="https://img.shields.io/badge/Streamlit-Latest-red?style=for-the-badge&logo=streamlit">
<img src="https://img.shields.io/badge/Groq-LLM-black?style=for-the-badge">
<img src="https://img.shields.io/badge/Cybersecurity-SOC-success?style=for-the-badge">

</p>

## 🚀 Overview

AI-SOCA is an enterprise-inspired AI Security Operations Center
assistant built with **Python**, **Streamlit**, and the **Groq API**. It
helps SOC analysts triage alerts, summarize logs, contextualize CVEs,
recommend MITRE ATT&CK aligned playbooks, and interact with security
data through a conversational interface.

<img width="1912" height="1075" alt="1" src="https://github.com/user-attachments/assets/7ed22089-a35b-4207-b34b-cf35c589fa8b" />
<img width="1919" height="1077" alt="2 Password Spray Attack" src="https://github.com/user-attachments/assets/4b119615-680b-4533-8adc-8ba576191e69" />
<img width="1905" height="1069" alt="3 Successful Compromise" src="https://github.com/user-attachments/assets/c5ac65ce-0a7e-4483-b4ae-47bf9d602693" />
<img width="1918" height="1075" alt="4 Sysmon Malware Execution" src="https://github.com/user-attachments/assets/d8a53e0c-7dee-482a-bed7-4a2f474ffb8e" />



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

## ✨ Features

AI-SOCA is designed to assist Security Operations Center (SOC) analysts by automating threat analysis, incident triage, and security intelligence generation using Large Language Models (LLMs).

| 🚀 Module | 📖 Description |
|------------|---------------|
| **🔍 SIEM Log Summarization** | Converts raw Windows, Linux, Firewall, Sysmon, EDR, IDS/IPS, and SIEM logs into concise, analyst-friendly incident summaries. |
| **🛡️ AI Incident Response Playbooks** | Generates MITRE ATT&CK aligned incident response playbooks with containment, eradication, recovery, and post-incident recommendations. |
| **⚠️ CVE Intelligence & Risk Analysis** | Provides vulnerability context, CVSS score interpretation, exploitation techniques, affected products, business impact, and mitigation guidance. |
| **💬 AI Security Assistant** | Interactive cybersecurity chatbot for SOC analysts, threat hunters, blue teams, and security engineers. |
| **🎯 IOC Extraction** | Automatically extracts IP addresses, domains, URLs, file hashes (MD5/SHA1/SHA256), usernames, hostnames, processes, registry keys, and suspicious commands. |
| **🔥 Threat Severity Assessment** | Classifies incidents into Critical, High, Medium, Low, or Informational severity based on observed Indicators of Compromise (IOCs). |
| **🧠 MITRE ATT&CK Mapping** | Maps attacker behavior to MITRE ATT&CK tactics, techniques, and procedures (TTPs) for faster threat investigation. |
| **📊 Executive Incident Summary** | Produces SOC-ready executive reports highlighting attack timeline, affected assets, risk level, and recommended next actions. |
| **🚨 Threat Intelligence Context** | Explains attack techniques, malware families, ransomware behavior, phishing campaigns, and command-and-control (C2) activities. |
| **⚡ Real-Time AI Analysis** | Uses Groq-powered LLM inference to deliver low-latency security analysis and actionable insights. |
| **📄 Multi-Source Log Support** | Supports Windows Event Logs, Linux Syslog, Sysmon, Apache, Nginx, Cisco ASA, Palo Alto, Microsoft Defender, Wazuh, Splunk, Sentinel, and custom SIEM logs. |
| **🎨 Modern Cybersecurity Dashboard** | Enterprise-inspired Streamlit interface featuring a futuristic cyber theme, interactive controls, and responsive design. |

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
