# 🤖 AI Web Scraper (Desktop App)

An AI-powered desktop application that extracts and summarizes content from any website.

No Python required — just download and run the `.exe`.

---

## 🚀 Features

- 🌐 Scrape clean content from any webpage
- 🧹 Smart extraction (only meaningful text: headings, paragraphs, lists)
- 🧠 AI summarization (2 modes):
  - Local AI (offline, no internet needed)
  - Online AI (high-quality summaries using LLM)
- 💻 Desktop GUI (no coding required)
- ⚡ Fast and responsive (threaded processing)

---

## 🖥️ Demo
<img width="1000" height="647" alt="screenshot1" src="https://github.com/user-attachments/assets/84c5d391-b51e-4158-93ba-800da3f489ae" />
<img width="1001" height="649" alt="screenshot2" src="https://github.com/user-attachments/assets/f2c3a254-c695-4aba-a7de-c8d90a27ce4b" />
<img width="999" height="648" alt="screenshot3" src="https://github.com/user-attachments/assets/401c1091-bafe-45cc-bd5c-b346a145a0c5" />

---

## 📦 Download

👉 Download the latest version here:

**[[Download .exe](../../releases)](https://github.com/nellzx/smart-web-scraper-ai/releases/tag/Releases)**

---

## 🧠 How It Works

1. Enter a website URL  
2. Choose mode:
   - Raw → full extracted text  
   - AI (Local) → offline summary  
   - AI (Online) → advanced AI summary  
3. Click **Run**  
4. Get results instantly  

---

## 🔑 Online AI Setup

To use Online AI mode:

1. Get a free API key from Cohere (https://dashboard.cohere.com/api-keys)
2. Paste it into the app  

---

## ⚙️ Installation (Dev)

```bash
git clone https://github.com/nellzx/smart-web-scraper-ai
cd smart-web-scraper-ai

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
python main.py
