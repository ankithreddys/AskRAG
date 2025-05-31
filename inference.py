import os
from dotenv import load_dotenv
import gradio as gr

from rag.loader import load_documents
from rag.text_splitter import split_documents
from rag.vector_store import get_or_create_vector_store
from rag.pipeline import build_rag_pipeline

load_dotenv()

def initialize_rag():
    documents = load_documents("knowledge-base")
    chunks = split_documents(documents)
    vector_store = get_or_create_vector_store(chunks)
    rag_chain = build_rag_pipeline(vector_store)
    return rag_chain

rag_chain = initialize_rag()

def chat(message, history):
    result = rag_chain.invoke({"question": message})
    return result["answer"]

iface = gr.ChatInterface(chat, type="messages")


if __name__ == "__main__":
    iface.launch()
