from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import JSONResponse
from utils.utils import handle_pdf, summarize, build_vectorstore, answer_question
import shutil
import os

app = FastAPI()

@app.post("/summarize")
async def summarize_endpoint(file: UploadFile = File(...)):
    contents = await file.read()
    with open("temp_upload", "wb") as f:
        f.write(contents)

    with open("temp_upload", "rb") as f:
        file.filename = file.filename or "uploaded.txt"
        text = handle_pdf(f)
        summary = summarize(text)

    os.remove("temp_upload")
    return {"summary": summary}

@app.post("/ask")
async def ask_endpoint(
    question: str = Form(...),
    context: str = Form(...)
):
    vectorstore = build_vectorstore(context)
    answer, justification = answer_question(vectorstore, question)
    return {"answer": answer, "justification": justification}
from utils.utils import generate_challenges

@app.post("/challenge")
async def challenge_endpoint(context: str = Form(...)):
    vectorstore = build_vectorstore(context)
    questions = generate_challenges(vectorstore)
    formatted = [q["question"] if isinstance(q, dict) else q for q in questions]
    return {"questions": formatted}
