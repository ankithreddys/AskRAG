import os
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

DB_DIR = "vector_db"

def get_or_create_vector_store(documents):
    embeddings = OpenAIEmbeddings()
    if os.path.exists(DB_DIR):
        print("Loading existing vector store...")
        vector_store = Chroma(persist_directory=DB_DIR, embedding_function=embeddings)
    else:
        print("Creating new vector store...")
        vector_store = Chroma.from_documents(
            documents=documents,
            embedding=embeddings,
            persist_directory=DB_DIR
        )
    return vector_store
