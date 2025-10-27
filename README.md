
# 📘 Q-A System — Educational Document Question Answering

This project implements an **offline Retrieval-Augmented Generation (RAG)** pipeline for answering questions based on **educational documents** (such as textbooks, PDFs, or lecture notes).  
It uses **LangChain**, **Sentence Transformers**, and **Ollama** to enable local, API-free question answering.

---

## 🧠 Overview

- 🧾 Upload educational documents (PDFs or text)
- 💬 Ask natural-language questions about the content
- ⚡ Works **completely offline** with Ollama models (`phi3`, `mistral`, or `llama3`)
- 🧩 Built for research flexibility — tweakable and publishable

---

## 🧩 Tech Stack

- **Python 3.10+**
- **LangChain** — Document loading, embedding, retrieval
- **Sentence Transformers** — Local embeddings
- **Ollama** — Local LLM inference (no API key needed)
- **Streamlit** — Frontend interface for Q&A
- **FAISS** — Vector similarity search

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/DishaJillella/Q-A-System.git
cd Q-A-System
````

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
```

### 3️⃣ Activate the Virtual Environment

* **Windows (PowerShell / VS Code Terminal):**

  ```bash
  venv\Scripts\activate
  ```
* **macOS / Linux:**

  ```bash
  source venv/bin/activate
  ```

Once active, your terminal should show `(venv)` at the start of the line.

---

### 4️⃣ Install Dependencies

Make sure `pip` is updated:

```bash
python -m pip install --upgrade pip
```

Then install all dependencies:

```bash
pip install -r requirements.txt
```

---

### 5️⃣ Install and Pull an Ollama Model

If you haven’t already, [download Ollama](https://ollama.ai/download).

Then pull a lightweight model (recommended for this project):

```bash
ollama pull phi3
```

You can test it with:

```bash
ollama run phi3
```

---

### 6️⃣ Run the Application

```bash
streamlit run app.py
```

This will open a browser window (usually at [http://localhost:8501](http://localhost:8501)) where you can upload documents and ask questions interactively.

---

## 🧾 Example Project Structure

```
Q-A-System/
│
├── app.py                     # Main Streamlit app for user interface
├── rag_pipeline.py             # Core RAG logic (loading, embedding, retrieval)
├── requirements.txt            # Project dependencies
├── README.md                   # Documentation file
├── .gitignore                  # Files to ignore in version control
└── data/                       # Folder for storing educational documents (PDFs, etc.)
```





## 🚀 Future Enhancements

* Add support for multiple file formats (DOCX, TXT, etc.)
* Add summarization and note-generation features
* Evaluate answer accuracy for research publication
* Deploy web version for educational use

---

## 🧑‍💻 Author

**Disha Jillella**
*Research and Development Project — Educational Document Q&A System (2025)*

---

## 🏁 Quick Start Summary

```bash
# Clone the project
git clone https://github.com/DishaJillella/Q-A-System.git
cd Q-A-System

# Create environment
python -m venv venv
venv\Scripts\activate

# Install requirements
pip install -r requirements.txt

# Pull model
ollama pull phi3

# Run app
streamlit run app.py

# Exit environment
deactivate
```

---


