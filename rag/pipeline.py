from langchain_openai import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

def build_rag_pipeline(vector_store, model="gpt-4o-mini"):
    llm = ChatOpenAI(temperature=0.7, model=model)
    retriever = vector_store.as_retriever()


    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True,
        output_key="answer"
    )

    conv_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=memory,
        return_source_documents=True
    )
    return conv_chain
