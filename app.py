import streamlit as st
from create_vectorstore import create_vectorstore
from ask_question import ask_question
import os

st.title("Save Time by Reading Documents via Docutrace")

uploaded_file = st.file_uploader("Upload your PDF", type=["pdf"])

if uploaded_file:
    with open("uploaded_doc.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    if not os.path.exists("vector_db"):
        create_vectorstore("uploaded_doc.pdf")
    else:
        st.info("Using existing vector database")

query = st.text_input("Ask a question about your document:")

if st.button("Get Answer") and query:
    st.write("⏳ Processing...")
    answer = ask_question(query)
    st.subheader("Answer:")
    st.write(answer)
