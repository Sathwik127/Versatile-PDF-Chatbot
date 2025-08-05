# Versatile PDF Chatbot: Conversational RAG with Dynamic LLM Backends

This capstone project is an interactive PDF chatbot built with **Streamlit** and **LangChain**, allowing users to upload PDF files and ask natural language questions about their contents. Users can dynamically switch between different LLM backends such as **Ollama (Llama2, Gemma, Mistral)** and **Groq API (Llama3)** during the conversation.

---

## 🎯 Project Objective

Build a conversational interface that:
- Ingests PDF files
- Uses a local RAG pipeline for context retrieval
- Dynamically routes queries to different LLM backends
- Preserves chat history for coherent conversations

---

## 🗂️ Project Structure

```bash
CHAPTER 8 CAPSTONE/
│
├── env/             # Virtual environment (auto-created, not committed to Git)
├── .env             # Environment variables (contains GROQ_API_KEY)
├── app.py           # Streamlit app for PDF chat + LLM backend switcher
└── app.ipynb        # Optional notebook for testing or experimentation
