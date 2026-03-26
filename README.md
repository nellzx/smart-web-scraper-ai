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

![App Screenshot](screenshot.png)

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
