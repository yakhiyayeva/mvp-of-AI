import streamlit as st
from utils.rag_pipeline import process_files, query_documents

st.set_page_config(page_title="🇰🇿 Constitution AI Assistant", layout="centered")
st.title("🇰🇿 Ask Anything About Constitution of Kazakhstan")

uploaded_files = st.file_uploader("Upload documents (PDF/TXT)", type=["pdf", "txt"], accept_multiple_files=True)

if uploaded_files:
    with st.spinner("Processing uploaded documents..."):
        process_files(uploaded_files)
    st.success("Documents processed and added to vector store.")

query = st.text_input("Ask a question about the Constitution:")

if query:
    with st.spinner("Thinking..."):
        response = query_documents(query)
    st.markdown(f"**Answer:**\n\n{response}")
