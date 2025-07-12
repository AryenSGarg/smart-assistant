# 📚 Smart Research Summarizer Assistant

An intelligent local assistant that reads research papers, legal docs, or technical reports — then summarizes, answers questions, or challenges you — all offline.

---

## 🚀 Features

- 📄 Upload PDF/TXT documents
- 🧠 Auto-summarization (150 words)
- ❓ Ask contextual questions ("Ask Anything" mode)
- 🧩 Get logic-based questions ("Challenge Me" mode)
- 🔌 Works 100% offline — no OpenAI or internet needed
- 🧪 Test all logic via Postman or API

---

## 🛠️ Setup Instructions

```bash
git clone https://github.com/AryenSGarg/smart-assistant.git
cd smart-assistant
python -m venv venv
source venv/Scripts/activate        # or source venv/bin/activate on Mac/Linux
pip install -r requirements.txt
🖥️ Option 1: Run the Assistant with Streamlit
bash
Copy
Edit
streamlit run app.py
🧑‍💻 What You Can Do in the Web App:
Upload a .pdf or .txt file (e.g., research paper).

The app shows a summary in under 150 words.

Choose interaction mode:

Ask Anything → type your question and get a contextual answer.

Challenge Me → the app generates 3 logic-based questions. You try answering, and it gives feedback + justification.

📡 Option 2: Use API via FastAPI + Postman
Start the backend server:

bash
Copy
Edit
python -m uvicorn api:app --reload
Then open:

arduino
Copy
Edit
http://127.0.0.1:8000/docs
You’ll see 3 endpoints:

POST /summarize → Upload file → Get summary

POST /ask → Send question and context → Get answer

POST /challenge → Send document text → Get logic-based questions

🧪 How to Test via Postman
📥 1. Import the postman_collection.json file
Open Postman → File → Import → Choose postman_collection.json

🧾 2. Run the 3 Requests
🔹 /summarize Request
Method: POST

Body: form-data

Key: file → Upload .txt or .pdf file

🔹 /ask Request
Method: POST

Body: x-www-form-urlencoded

question: Your query

context: Paste full text of the document

🔹 /challenge Request
Method: POST

Body: x-www-form-urlencoded

context: Paste full document text

✅ Each will return a JSON response with answers, questions, or summaries.

📂 File Structure
markdown
Copy
Edit
smart-assistant/
├── app.py
├── api.py
├── requirements.txt
├── .gitignore
├── README.md
├── postman_collection.json
│
├── utils/
│   ├── utils.py
│   └── __init__.py
│
├── assets/
│   └── ai_ethics.txt
👨‍💻 Built by Aryen Garg
📧 aryengarg58@gmail.com
🔗 LinkedIn