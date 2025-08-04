# app.py

import streamlit as st
from backend import generate_answer
import pdfplumber
import docx

# Page settings
st.set_page_config(page_title="RAG AI Chatbot", page_icon="🤖", layout="centered")

st.markdown("<h1 style='text-align: center;'>🤖 RAG Document Chatbot</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Ask intelligent questions from your own files (.txt, .pdf, .docx)</p>", unsafe_allow_html=True)

# Function to extract text from file
def extract_text(file):
    file_name = file.name

    if file_name.endswith(".txt"):
        return file.read().decode("utf-8")

    elif file_name.endswith(".pdf"):
        text = ""
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        return text

    elif file_name.endswith(".docx"):
        doc = docx.Document(file)
        return "\n".join([para.text for para in doc.paragraphs])

    else:
        return None

# Upload file
uploaded_file = st.file_uploader("📄 Upload a document", type=["txt", "pdf", "docx"])

if uploaded_file:
    st.success(f"✅ Uploaded: {uploaded_file.name}")

    document_text = extract_text(uploaded_file)

    if document_text:
        user_question = st.text_input("💬 Ask a question about your document:")

        if user_question:
            with st.spinner("🔍 Thinking..."):
                answer, context = generate_answer(user_question, document_text)

            st.markdown("### 💡 Answer:")
            st.write(answer)
            st.markdown("---")




            with st.expander("📖 Retrieved Context (for transparency):"):
                st.markdown(context)

    else:
        st.error("❌ Could not extract text from the uploaded file.")
