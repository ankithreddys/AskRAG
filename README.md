
# 🧠 AskRAG — Conversational RAG with LangChain, OpenAI & Gradio

AskRAG is a modular Conversational Retrieval-Augmented Generation (RAG) system. It lets you ask natural language questions about your custom knowledge base of Markdown files — powered by GPT, LangChain, Chroma, and Gradio.

## Features

- Load markdown documents organized by folder
- Split text into overlapping chunks
- Generate embeddings using OpenAI
- Store and retrieve from a Chroma vector database
- Query with GPT-4o or GPT-4o-mini using LangChain’s ConversationalRetrievalChain
- Simple Gradio-based chat interface
- Session memory enabled (recalls chat history)
- Auto-persistence: reuses existing vector DB or builds new one

## Project Structure
````markdown

ASKRAG/
├── knowledge-base/               # markdown files grouped in subfolders  
├── rag/  
│   ├── loader.py                 # Loads documents and tags them with doc_type  
│   ├── text_splitter.py          # Splits documents into chunks  
│   ├── vector_store.py           # Embeds and stores/retrieves from Chroma  
│   ├── pipeline.py               # Builds the LangChain chat pipeline  
├── vector_db/                    # Chroma DB directory (auto-created)  
├── inference.py                  # Gradio app for chat interface  
├── .env                          # API keys and configs (not committed)  
├── .gitignore                    # Ignore vector DB and .env  
├── README.md                     # This file  
````

## Setup Instructions

1. Clone the repository  
   ```bash
   git clone https://github.com/your-username/ASKRAG.git  
   cd ASKRAG  
    ```
2. (Optional) Create and activate a virtual environment

   ```bash
   python -m venv venv  
   source venv/bin/activate  # On Windows: venv\Scripts\activate  
   ```

3. Install dependencies

   ```bash
   pip install -r requirements.txt  
   ```

4. Create a `.env` file in the root directory and add your OpenAI key:

   ```
   OPENAI_API_KEY=your-openai-key-here  
   ```

5. Add your Markdown documents into subfolders inside `knowledge-base/`.
   Each folder acts like a document category (e.g., `./knowledge-base/policy/`, `./knowledge-base/tech/`).

6. Run the application

   ```bash
   python inference.py  
   ```

## Example Usage

Once the app launches, a Gradio chat UI will appear. You can now ask questions like:

* “Summarize the key points from the tech documents.”
* “What does the policy folder say about compliance?”
* “Give me all documents that mention ‘data retention’.”

The system retrieves the most relevant context chunks and answers using GPT-4o.

## Customize

* To change the OpenAI model, update the default in `pipeline.py` or pass it in `build_rag_pipeline()`.
* Chunk size and overlap can be tuned in `text_splitter.py`.
* Use a different embedding model by modifying `vector_store.py`.

## Requirements

* Python 3.8+
* `langchain`
* `langchain-openai`
* `langchain-community`
* `langchain-chroma`
* `chromadb`
* `openai`
* `gradio`
* `python-dotenv`

You can generate the `requirements.txt` with:

```bash
pip freeze > requirements.txt
```


## Acknowledgments

* [LangChain](https://github.com/langchain-ai/langchain)
* [ChromaDB](https://github.com/chroma-core/chroma)
* [OpenAI](https://openai.com/)
* [Gradio](https://www.gradio.app/)

