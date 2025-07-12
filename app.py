import streamlit as st
from utils import handle_pdf, summarize, build_vectorstore, answer_question, generate_challenges

st.set_page_config(page_title="📚 Smart Research Assistant", layout="wide")
st.title("📖 Smart Research Summarizer Assistant (Offline Mode)")

uploaded_file = st.file_uploader("Upload a research paper or document (PDF or TXT)", type=['pdf', 'txt'])

if uploaded_file:
    with st.spinner("Processing document..."):
        doc_text = handle_pdf(uploaded_file)
        st.session_state['doc_text'] = doc_text

        vectorstore = build_vectorstore(doc_text)
        st.session_state['vectorstore'] = vectorstore

        summary = summarize(doc_text)
        st.subheader("🔍 Auto Summary")
        st.write(summary)

        st.subheader("💬 Choose a Mode")
        mode = st.radio("Select interaction mode", ["Ask Anything", "Challenge Me"])

        if mode == "Ask Anything":
            query = st.text_input("Ask your question:")
            if query:
                answer, justification = answer_question(vectorstore, query)
                st.markdown(f"**Answer:** {answer}")
                st.caption("📌 Supporting context:")
                st.code(justification, language='markdown')

        elif mode == "Challenge Me":
            if st.button("Generate Questions"):
                questions = generate_challenges(vectorstore)
                for i, q in enumerate(questions):
                    st.markdown(f"**Q{i+1}. {q.strip()}**")
                    st.text_input(f"Your Answer to Q{i+1}", key=f"user_ans_{i}")
