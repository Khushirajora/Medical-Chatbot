# 🩺 Medical Chatbot using RAG

An AI-powered Medical Chatbot built with **Python, LangChain, FAISS, Hugging Face, Mistral, Ollama, and Streamlit**. It answers medical questions by retrieving relevant information from medical PDF documents using Retrieval-Augmented Generation (RAG).

## 📌 Project Overview

The Medical Chatbot is designed to provide users with medical information from a provided medical encyclopedia.

It uses a Retrieval-Augmented Generation (RAG) pipeline to retrieve relevant information from PDF documents and generate context-based answers using a locally running Mistral language model.

The chatbot also includes an interactive web interface developed using Streamlit.

## ✨ Features

- **PDF Document Loading:** Loads medical PDF documents using LangChain.
- **Text Chunking:** Splits extracted PDF text into smaller chunks.
- **Text Embeddings:** Generates vector embeddings using Hugging Face Sentence Transformers.
- **Vector Database:** Stores and searches document embeddings using FAISS.
- **Retrieval-Augmented Generation:** Retrieves relevant medical information to answer user questions.
- **Local LLM Integration:** Uses Mistral through Ollama.
- **Interactive Chat Interface:** Provides a conversational interface using Streamlit.
- **Context-Based Responses:** Instructs the model to answer using retrieved context rather than inventing information.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| LangChain | RAG pipeline development |
| Hugging Face | Text embedding model |
| Sentence Transformers | Text embeddings |
| FAISS | Vector database and similarity search |
| Mistral | Large Language Model |
| Ollama | Local LLM execution |
| Streamlit | Web-based chatbot interface |

## 🏗️ Project Architecture

```text
             Medical PDF Documents
                      |
                      v
               PDF Document Loader
                      |
                      v
                 Text Splitting
                      |
                      v
             Hugging Face Embeddings
                      |
                      v
                FAISS Vector DB
                      |
                      |
User Question --------+
       |
       v
 Streamlit Interface
       |
       v
  LangChain Retriever
       |
       v
 Retrieve Relevant Chunks
       |
       v
   Mistral LLM (Ollama)
       |
       v
 Generated Medical Answer
       |
       v
 Streamlit Chat Interface
```

## 📂 Project Structure

```text
Medical-Chatbot/
│
├── data/
│   └── Medical PDF documents
│
├── vectorstore/
│   └── db_faiss/
│
├── create_memory_for_llm.py
├── connect_memory_with_llm.py
├── medibot.py
├── requirements.txt
├── Pipfile
├── .gitignore
└── README.md
```

**Note:** Medical PDF documents and the generated FAISS database are not included in this repository. You need to provide your own legally usable medical PDF and generate the vector database locally.

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Khushirajora/Medical-Chatbot.git
```

### 2. Navigate to the project directory

```bash
cd Medical-Chatbot
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Install Ollama

Download and install Ollama:

https://ollama.com/

Download the Mistral model:

```bash
ollama pull mistral
```

### 6. Add medical PDF documents

Create a folder named `data` in the project directory and place your legally usable medical PDF documents inside it.

### 7. Create the FAISS vector database

Run:

```bash
python create_memory_for_llm.py
```

This script loads the PDF documents, splits their text into chunks, generates embeddings, and saves them in the FAISS vector database.

### 8. Run the chatbot

Start the Streamlit application:

```bash
streamlit run medibot.py
```

Open the local URL displayed in your terminal to access the chatbot.

## 💬 Example Questions

You can ask questions such as:

- What is cancer?
- What are the symptoms of diabetes?
- What is chemotherapy?
- What are the symptoms of anemia?

The chatbot retrieves relevant information from the available medical documents before generating its response.

## 🚀 Future Improvements

- Implement conversational memory for follow-up questions.
- Display source references and PDF page numbers with answers.
- Improve retrieval accuracy.
- Add better error handling and testing.
- Improve the chatbot interface.
- Deploy the application for public access.

## ⚠️ Disclaimer

This project is developed for educational and informational purposes only.

The chatbot is not a medical professional and should not be used for medical diagnosis, treatment decisions, or emergencies. Always consult a qualified healthcare professional for medical advice.

## 👩‍💻 Author

**Khushi Rajora**

GitHub: https://github.com/Khushirajora

---

⭐ If you find this project interesting, consider giving the repository a star!
