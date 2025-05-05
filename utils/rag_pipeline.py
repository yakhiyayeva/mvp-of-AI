import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import OllamaEmbeddings
from utils.ollama_llm import ask_ollama

load_dotenv()

CHROMA_DB_DIR = os.getenv("CHROMA_DB_DIR", "./chroma_db")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "mistral")

embedding = OllamaEmbeddings(model=OLLAMA_MODEL)
vectorstore = Chroma(persist_directory=CHROMA_DB_DIR, embedding_function=embedding)

def process_files(files):
    documents = []
    for file in files:
        if file.name.endswith('.pdf'):
            loader = PyPDFLoader(file)
        elif file.name.endswith('.txt'):
            loader = TextLoader(file)
        else:
            continue
        docs = loader.load()
        documents.extend(docs)

    splitter = RecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=64)
    chunks = splitter.split_documents(documents)

    vectorstore.add_documents(chunks)
    vectorstore.persist()

def query_documents(user_query):
    similar_docs = vectorstore.similarity_search(user_query, k=3)
    context = "\n\n".join([doc.page_content for doc in similar_docs])
    return ask_ollama(user_query, context)
