<h1 align="center"> 🧠 AI-SOCA: AI-Driven Adaptive SOC Assistant </h1>

![logo](https://github.com/user-attachments/assets/c93495d6-320d-4490-99df-d9fded99f496)

---
![Python](https://img.shields.io/badge/Python-3.9%2B-blueviolet) ![Streamlit](https://img.shields.io/badge/Streamlit-1.25%2B-brightgreen) ![Groq AI](https://img.shields.io/badge/Groq%20AI-Powered-blue)

---

## An intelligent assistant for Security Operations Centers (SOCs), built with **Python**, **Streamlit**, the **Groq API**, and the **Qwen-32B** model. AI-SOCA helps security analysts triage, respond to, and report security incidents quickly and effectively.

---

## 🚀 Features

- 🔍 **SIEM Log Summarization**  
  Translates raw logs into human-readable summaries highlighting anomalies and threats.

- 📖 **MITRE ATT&CK-based Playbook Recommendations**  
  Maps incident indicators to the MITRE framework and recommends proper response actions.

- ⚠️ **CVE Threat Contextualization**  
  Provides threat intel, exploitation details, and impact summaries for CVEs.

- 💬 **Interactive Chat Mode**  
  Ask questions about your SOC environment with a natural language interface.

---

## 🛠️ Tech Stack

- 🐍 Python  
- 🌐 Streamlit  
- ⚡ [Groq API](https://groq.com/)  
- 🧠 Qwen-qwq-32b LLM  
- 📦 dotenv (for secure API key loading)

---

## 📥 Installation

```bash
# 1. Clone the repository
git clone https://github.com/your-username/AI-Driven-Adaptive-SOC-Assistant-AI-SOCA-.git
cd AI-Driven-Adaptive-SOC-Assistant-AI-SOCA-

# 2. Install dependencies
pip install -r requirements.txt
````

---

## 🔐 Setup API Key

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_actual_groq_api_key
```

---

## 🧪 Usage

```bash
streamlit run app.py
```

Open your browser to: `http://localhost:8501`

---

## 🧾 Sample Inputs

### 1. Summarize Logs

```text
Jun 13 18:12:34 firewall1 kernel: [UFW BLOCK] IN=eth0 OUT= MAC=00:0c:29:48:bc:35 SRC=45.77.50.12 DST=192.168.1.100 LEN=60 PROTO=TCP SPT=445 DPT=3389
Jun 13 18:12:35 firewall1 kernel: [UFW BLOCK] IN=eth0 OUT= MAC=00:0c:29:48:bc:35 SRC=45.77.50.12 DST=192.168.1.100 LEN=60 PROTO=TCP SPT=445 DPT=3389
Jun 13 18:13:02 ids-snort alert: [1:2010935:3] ET POLICY PE EXE or DLL Windows file download HTTP [Classification: Potential Corporate Privacy Violation] [Priority: 1] SRC=185.173.36.50 DST=192.168.1.200 SPT=80 DPT=52304
```

### 2. Recommend Playbook

```text
Multiple failed login attempts from IP 203.0.113.50 on the SSH port (22), followed by a successful login. User account: devops-admin.
Brute-force attack suspected.
```

### 3. Contextualize CVE

```text
CVE-2024-3094
```

---

## 📸 Screenshot

| **Summarize Logs** |
|--------------------------------------------------------------------------------------------------|
|![Summarize Logs](https://github.com/user-attachments/assets/18a40d5f-8077-4768-b3cb-3edac79600cc)|

| **Recommend Playbook** |
|------------------------------------------------------------------------------------------------------|
|![Recommend Playbook](https://github.com/user-attachments/assets/1e96ce4e-0d67-4819-ac5d-243654c47c91)|

| **Contextualize CVE** |
|-----------------------------------------------------------------------------------------------------|
|![Contextualize CVE](https://github.com/user-attachments/assets/be916638-765e-47a9-b3ec-03b882fdffe1)|

| **Chat Interface Example** |
|----------------------------------------------------------------------------------------------------------|
|![Chat Interface Example](https://github.com/user-attachments/assets/2341203b-54fb-4dd0-bf40-6e1a773ff6f6)|


---

## 🤝 Contributing
Feel free to **fork** the repository, submit **issues**, or contribute **pull requests** to improve the project.

---

## 🔗 Contact & Support
Have questions or suggestions? Feel free to reach out:

- 📧 [Email](mailto:gauravghandat12@gmail.com)
- 💼 [LinkedIn](www.linkedin.com/in/gaurav-ghandat-68a5a22b4)
---

## 📄 License

This project is licensed under the MIT License.



