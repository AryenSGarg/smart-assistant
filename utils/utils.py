import os
import pdfplumber
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document
from sentence_transformers import SentenceTransformer
from langchain_community.embeddings import HuggingFaceEmbeddings
from transformers import pipeline

load_dotenv()

# Load local sentence transformer model
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Use local summarization (optional: offline)
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")


# 1. Read file
def handle_pdf(file):
    text = ""
    if file.name.endswith(".pdf"):
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
    elif file.name.endswith(".txt"):
        text = file.read().decode("utf-8")
    return text.strip()


# 2. Summarize locally
def summarize(text):
    text = text[:3000]  # prevent overload
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return summary[0]['summary_text']


# 3. Build FAISS vectorstore using local embeddings
def build_vectorstore(text):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_text(text)
    docs = [Document(page_content=chunk) for chunk in chunks]
    db = FAISS.from_documents(docs, embedding_model)
    return db


# 4. Answer questions using local retrieval + LLM-free response
def answer_question(vectorstore, question):
    retriever = vectorstore.as_retriever()
    docs = retriever.get_relevant_documents(question)
    context = "\n\n".join([doc.page_content for doc in docs[:3]])

    # basic response logic without GPT
    if question.lower() in context.lower():
        answer = "Yes, it is mentioned in the document."
    else:
        answer = "Based on the document context, no direct answer found."

    return answer, context


# 5. Generate mock logic-based questions
def generate_challenges(vectorstore):
    retriever = vectorstore.as_retriever()
    docs = retriever.get_relevant_documents("generate comprehension questions")
    context = "\n\n".join([doc.page_content for doc in docs[:2]])

    return [
        "What are the main arguments presented in the document?",
        "How does the author support their claims?",
        "Are there any underlying assumptions in the reasoning?"
    ]
