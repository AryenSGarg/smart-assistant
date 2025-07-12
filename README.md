# 📚 Smart Research Summarizer Assistant

A local GenAI assistant to read and understand research papers, legal docs, and more.

---

## 🚀 Features

- Upload PDF/TXT documents
- Auto-summarization (150 words)
- Ask contextual questions (Ask Anything)
- Answer logic-based questions (Challenge Me)
- No internet/API needed — 100% offline

---

## 🧠 Architecture

- `sentence-transformers` for local embeddings
- `FAISS` for vector similarity search
- `transformers` model for summarization
- `Streamlit` for frontend

---

## 🛠️ Setup Instructions

```bash
git clone https://github.com/<your-username>/smart-research-assistant.git
cd smart-research-assistant
python -m venv venv
source venv/Scripts/activate       # or source venv/bin/activate on Mac/Linux
pip install -r requirements.txt
streamlit run app.py
