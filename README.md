[![Deploy on Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/)

# 🤖 RAG-Based Document Chatbot using Streamlit

A lightweight Retrieval-Augmented Generation (RAG) chatbot built using Hugging Face models, FAISS, and Streamlit.  
It lets users upload `.txt`, `.pdf`, or `.docx` documents and ask questions — generating context-grounded answers locally using a small transformer model.

---

## 🚀 Features

- 📁 Upload `.txt`, `.pdf`, or `.docx` files
- 🧠 Context-aware answer generation using `flan-t5-small`
- 🔍 Document retrieval using `FAISS` + `Sentence-Transformers`
- 💬 Simple and clean chatbot-like UI (Streamlit)
- 💻 Runs locally on low-spec machines (≤ 8GB RAM)
- 🌐 Easily deployable on Streamlit Cloud

---

## 📂 Folder Structure

rag-chatbot-streamlit/
├── app.py # Main Streamlit app (UI)
├── backend.py # Backend logic (RAG: retrieval + generation)
├── requirements.txt # All Python dependencies
├── .gitignore # Ignore virtualenv, cache, etc.
└── README.md # You're here!


---

## ⚙️ Requirements

- Python 3.8 or higher
- pip
- Internet (to download models once)

---

## 🔧 Installation (Run Locally)

1. **Clone the repository**

```bash
git clone https://github.com/RANJANA12-SHUKLA/rag-mini-chatbot-streamlit.git
cd rag-chatbot-streamlit

```
2. Create and activate a virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows

3. Install DEPENDICIES
pip install -r requirements.txt

4. Run the Streamlit app
streamlit run app.py


### How It Works
1. User uploads a file (.txt, .pdf, .docx)

2. File is parsed and split into chunks

3. Chunks are embedded using all-MiniLM-L6-v2

4. FAISS retrieves the most relevant chunk for the query

5. Query + context are passed to flan-t5-small for generation

6. Result is displayed in the app

## 📤 Deploy to Streamlit Cloud

1. Push this project to a **public GitHub repository**
2. Go to [Streamlit Cloud](https://share.streamlit.io/)
3. Click "New App" → Select your repo
4. Set `app.py` as the entry point
5. Click **Deploy**

### you can see  live app at:
https://RANJANA12-SHUKLA-rag-chatbot-streamlit.streamlit.app

## Technologies Used

| Tool                     | Purpose                         |
| ------------------------ | ------------------------------- |
| Streamlit                | User interface                  |
| HuggingFace Transformers | Text generation (flan-t5-small) |
| Sentence-Transformers    | Semantic embeddings             |
| FAISS                    | Fast document retrieval         |
| pdfplumber               | Extract text from PDF           |
| python-docx              | Extract text from Word files    |

### Future Enhancements
Chat history with session state
Support for .pdf with tables/images (via PyMuPDF)
Feedback/rating buttons
Downloadable responses
Option to choose different models (flan-t5, mistral, etc.)



## 📄 License

This project is licensed under the MIT License.  
See the [LICENSE](LICENSE) file for more information.



