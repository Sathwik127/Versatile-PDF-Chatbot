from dotenv import load_dotenv
load_dotenv()
import os
api_key=os.getenv("GEMINI_API_KEY")
print(api_key)
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
import streamlit as st
uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")


llm3 = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=api_key
)
llm = ChatGroq(
    model="llama3-70b-8192",
    groq_api_key="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"
)
from langchain_community.document_loaders import PDFMinerLoader
import tempfile

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_file_path = tmp_file.name

    # Use PDFMinerLoader instead of PyPDFLoader for better extraction
    from langchain_community.document_loaders import PDFMinerLoader
    loader = PDFMinerLoader(tmp_file_path)
    docs = loader.load()

    st.success("PDF loaded successfully!")
    st.write(docs[0].page_content[:500])  # Preview first chunk
from langchain_community.document_loaders import PDFMinerLoader

loader = PDFMinerLoader("NagasaiBasani_FinalResearchReport.pdf")
docs = loader.load()

from langchain_text_splitters import RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(
    # Set a really small chunk size, just to show.
    chunk_size=300,
    chunk_overlap=50,
    length_function=len,
    is_separator_regex=False,
)
chunks = text_splitter.split_documents(docs)
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
from langchain_community.vectorstores import FAISS
vector_store = FAISS.from_documents(docs, embeddings)
from langchain.memory import ConversationBufferMemory

retriever = vector_store.as_retriever()
from langchain.memory import ConversationBufferMemory

from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq

prompt = PromptTemplate.from_template("""
You are a helpful assistant having a conversation with a user.

Conversation history:
{history}

User: {input}
AI:
""")
from langchain_community.chat_models import ChatOllama

llm1 = ChatOllama(model="llama3")
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI  # or ChatGroq / ChatOllama
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True,output_key="answer")


# Define components


# Build the chain
chain1 = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=retriever,
    memory=memory,
    return_source_documents=True,
    output_key="answer"
)
chain2 = ConversationalRetrievalChain.from_llm(
    llm=llm1,
    retriever=retriever,
    memory=memory,
    return_source_documents=True,
    output_key="answer"
)

import streamlit as st
model = st.radio("Select Model", ["Ollama", "Groq"])
q = st.text_input("Enter your question")
if st.button("Send"):
    if model == "Ollama":
        response=chain1.invoke({"question": q})
        st.write(response["answer"])
    else:
        response=chain2.invoke({"question": q})
        st.write(response["answer"])
