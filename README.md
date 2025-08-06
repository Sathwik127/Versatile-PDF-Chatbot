
# 🤖 Versatile PDF Chatbot: Conversational RAG with Dynamic LLM Backends

An interactive AI-powered chatbot built with **LangChain** and **Streamlit** that lets you upload PDF documents and chat with their content in natural language. Supports **dynamic switching between Ollama and Groq LLM backends**, making it flexible, fast, and modular.


> **User Question:** *"Whose PDF is it?"*  
> **Bot Response:** *"The PDF appears to be written by Sathwik Alavala, with the ID number 646185."*

---

## 🚀 Features

- 📤 **PDF Upload** – Upload and process any `.pdf` file (up to 200MB)
- 🧠 **RAG Pipeline** – Combines retrieval + generation using LangChain
- 🔍 **Advanced Text Parsing** – Extracts text using `PDFMinerLoader`
- 🔗 **Text Chunking** – Cleanly splits long documents for better context
- 💾 **FAISS Vector Store** – Local vector-based memory for high-speed search
- 🔄 **Dynamic LLM Switching** – Choose between **Ollama** (local) and **Groq** (cloud)
- 💬 **Conversational Memory** – Remembers previous interactions in the same session
- 🌐 **Streamlit Web UI** – Minimal, fast, and modern interface

---

## 🛠️ Tech Stack

| Category           | Tools Used                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| Framework          | 🐍 Python, Streamlit                                                        |
| AI Toolkit         | 🧠 LangChain, HuggingFace Transformers                                      |
| Embedding Model    | `sentence-transformers/all-mpnet-base-v2`                                  |
| Vector Store       | FAISS                                                                      |
| Document Parsing   | PDFMiner                                                                   |
| LLM Integrations   | Ollama (local) 🧠, Groq API (cloud) ⚡                                       |

---

## 🧪 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/versatile-pdf-chatbot.git
cd versatile-pdf-chatbot
```

### 2. Create Virtual Environment

```bash
python -m venv env
source env/bin/activate        # On Windows: .\env\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory with the following:

```env
GROQ_API_KEY=your_groq_api_key
---

## ▶️ Run the App

```bash
streamlit run app.py
```

## Screenshots
After running you see <img width="1273" height="511" alt="image" src="https://github.com/user-attachments/assets/5830eb60-53f1-4ecb-ac2f-d5d60fc93f68" />
After uploading you will have options to choose whether you want to use Ollama or Groq and ask questions
<img width="1251" height="805" alt="image" src="https://github.com/user-attachments/assets/9d5eb9e3-76b8-457c-92cd-3c8c652ef1d8" />
<img width="1275" height="863" alt="image" src="https://github.com/user-attachments/assets/0e6548e1-4a8c-4456-af5c-da4f5c3bb532" />



---

## 💡 How to Use

1. Upload a `.pdf` file using the file uploader.
2. Select your desired LLM backend (Ollama or Groq).
3. Type your question (e.g., *“Summarize the document”* or *“Who is the author?”*).
4. Click **Send** and receive a contextual response.

---

## 🧠 Example Questions to Try

- "Summarize the document."
- "What is this PDF about?"

---



## 📂 Project Structure

```
├── app.py                  # Main Streamlit application
├── .env                    # API keys (not committed)
├── requirements.txt        # Python dependencies
└── README.md               # You're here!
```

---

## 🧑‍💻 Author

**Capstone Project by:** *Sathwik Alavala*  
**Project Title:** *"Versatile PDF Chatbot: Conversational RAG with Dynamic LLM Backends"*

---

## 🙏 Acknowledgements

- [LangChain](https://www.langchain.com/)
- [Streamlit](https://streamlit.io/)
- [Ollama](https://ollama.com/)
- [Groq](https://groq.com/)
- [HuggingFace Transformers](https://huggingface.co/)

---

> 💬 Have feedback? Open an issue or submit a pull request. Contributions welcome!
