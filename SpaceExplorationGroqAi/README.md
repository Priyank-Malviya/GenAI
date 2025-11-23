# 🚀 Space Exploration Chatbot

A RAG (Retrieval-Augmented Generation) based chatbot that answers questions about space exploration and astronomy using PDF documents as knowledge base.

## 📋 Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Getting API Keys](#getting-api-keys)
  - [Groq API Key](#1-groq-api-key-required)
  - [LangSmith API Key](#2-langsmith-api-key-optional)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Technology Stack](#technology-stack)
- [Troubleshooting](#troubleshooting)

## ✨ Features

- **RAG Pipeline**: Retrieval-Augmented Generation using PDF documents
- **Vector Search**: Chroma vector database with HuggingFace embeddings
- **LLM Integration**: Powered by Groq's llama-3.1-8b-instant model
- **LangSmith Tracing**: Optional monitoring and debugging of LLM calls
- **Web Interface**: User-friendly Gradio interface with chat history
- **Chat History**: Maintains conversation context throughout the session

## 📦 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Internet connection (for API calls)

## 🔑 Getting API Keys

### 1. Groq API Key (Required)

Groq provides fast LLM inference with a generous free tier.

#### Step-by-Step Instructions:

1. **Visit Groq Console**
   - Go to [https://console.groq.com](https://console.groq.com)

2. **Sign Up / Log In**
   - Click "Sign Up" if you don't have an account
   - You can sign up using:
     - Google account
     - GitHub account
     - Email address

3. **Navigate to API Keys**
   - Once logged in, click on your profile icon (top right)
   - Select "API Keys" from the dropdown menu
   - Or directly go to [https://console.groq.com/keys](https://console.groq.com/keys)

4. **Create New API Key**
   - Click "Create API Key" button
   - Give your key a descriptive name (e.g., "Space Chatbot")
   - Click "Submit" or "Create"

5. **Copy Your API Key**
   - Your API key will be displayed (starts with `gsk_`)
   - **IMPORTANT**: Copy it immediately - you won't be able to see it again!
   - Format: `gsk_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

6. **Store Securely**
   - Keep your API key secret
   - Never commit it to version control
   - Never share it publicly

#### Groq Free Tier Limits:
- **30 requests per minute**
- **14,400 requests per day**
- Multiple models available (we use llama-3.1-8b-instant)

---

### 2. LangSmith API Key (Optional)

LangSmith provides monitoring, tracing, and debugging for LLM applications.

#### Step-by-Step Instructions:

1. **Visit LangSmith**
   - Go to [https://smith.langchain.com](https://smith.langchain.com)

2. **Sign Up / Log In**
   - Click "Sign Up" or "Log In"
   - You can sign up using:
     - Email address
     - Google account
     - GitHub account

3. **Create an Organization** (if first time)
   - After signing up, you'll be prompted to create an organization
   - Enter an organization name
   - Click "Create"

4. **Navigate to Settings**
   - Click on your profile icon (top right)
   - Select "Settings"
   - Or go to [https://smith.langchain.com/settings](https://smith.langchain.com/settings)

5. **Create API Key**
   - Click on "API Keys" tab in the left sidebar
   - Click "Create API Key" button
   - Give your key a name (e.g., "Space Chatbot Key")
   - Select permissions (default is fine)
   - Click "Create API Key"

6. **Copy Your API Key**
   - Your API key will be displayed (starts with `lsv2_`)
   - **IMPORTANT**: Copy it immediately!
   - Format: `lsv2_pt_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx_xxxxxxxxxxxxxxxx`

7. **Note Your Project Name**
   - You can use the default project name in the `.env` file
   - Or create a new project in LangSmith and use that name

#### LangSmith Features:
- **Request Tracing**: See all LLM calls and their inputs/outputs
- **Performance Monitoring**: Track latency and token usage
- **Debugging**: Identify issues in your RAG pipeline
- **Cost Tracking**: Monitor API usage

#### LangSmith Free Tier:
- **5,000 traces per month** for free
- Perfect for development and testing

---

## 🛠️ Installation

### 1. Clone or Download the Project

```bash
cd /Users/admin/Desktop/Nick/GenAI/SpaceExplorationGroqAi
```

### 2. Install Required Dependencies

**Option 1: Using requirements.txt (Recommended)**

```bash
pip install -r requirements.txt
```

**Option 2: Manual Installation**

```bash
pip install langchain langchain-community langchain-groq langchain-huggingface
pip install chromadb pypdf gradio python-dotenv langsmith
pip install sentence-transformers
```

**Required Python Packages:**
- `langchain` - Framework for LLM applications
- `langchain-community` - Community integrations
- `langchain-groq` - Groq LLM integration
- `langchain-huggingface` - HuggingFace embeddings
- `chromadb` - Vector database
- `pypdf` - PDF loading
- `gradio` - Web interface
- `python-dotenv` - Environment variable management
- `langsmith` - LangSmith tracing
- `sentence-transformers` - Embeddings model

---

## ⚙️ Configuration

### 1. Create/Edit `.env` File

In the `SpaceExplorationGroqAi` folder, you should have a `.env` file. Edit it with your API keys:

```env
# Required: Groq API Key
GROQ_API_KEY=gsk_your_actual_groq_api_key_here

# Optional: LangSmith Configuration
LANGSMITH_API_KEY=lsv2_pt_your_langsmith_api_key_here
LANGSMITH_PROJECT=space-exploration-chatbot
LANGSMITH_TRACING=true

# Optional: PDF File Path (if different location)
# PDF_FILE=space_exploration.pdf
```

### 2. Configure Your Keys

Replace the placeholder values:

- **`GROQ_API_KEY`**: Paste your Groq API key (starts with `gsk_`)
- **`LANGSMITH_API_KEY`**: Paste your LangSmith API key (starts with `lsv2_`) or leave empty to disable tracing
- **`LANGSMITH_PROJECT`**: Your project name (default: `space-exploration-chatbot`)
- **`LANGSMITH_TRACING`**: Set to `true` to enable, `false` to disable

### 3. Prepare Your PDF

Ensure you have a PDF file named `space_exploration.pdf` in the same folder, or update the `PDF_FILE` variable in `.env` to point to your document.

---

## 🚀 Usage

### Running the Chatbot

1. **Navigate to the project folder:**
   ```bash
   cd $HOME/{YOUR_LOCATION}/GenAI/SpaceExplorationGroqAi
   ```

2. **Run the chatbot:**
   ```bash
   python space_chatbot.py
   ```

3. **Expected Output:**
   ```
   Space Exploration Chatbot - Initializing
   ------------------------------------------------------------
   Loading PDF: space_exploration.pdf
   Loaded X pages
   Split into X chunks
   Initializing vector store (Chroma)...
   Creating Chroma vector store...
   Vector store created
   Initializing LLM (Groq Cloud)...
   LLM initialized (llama-3.1-8b-instant)
   Creating RAG chain...
   RAG chain created
   Chatbot initialized successfully!
   ------------------------------------------------------------
   
   LangSmith tracing enabled (Project: space-exploration-chatbot)
   Launching Gradio interface...
   Running on local URL:  http://127.0.0.1:7860
   ```

4. **Access the Web Interface:**
   - Open your browser
   - Go to: `http://127.0.0.1:7860`

### Using the Interface

1. **Ask Questions:**
   - Type your question in the "Your Question" text box
   - Example questions:
     - "What are the major space exploration missions?"
     - "Tell me about Mars exploration"
     - "What is the International Space Station?"
     - "Explain black holes"

2. **Submit:**
   - Click the "Submit" button
   - View the response in the "Response" section

3. **View History:**
   - All your questions and answers are saved in "Chat History"
   - Scroll through previous conversations

4. **Clear History:**
   - Click "Clear History" to start fresh
   - This clears the conversation context

### Stopping the Chatbot

Press `Ctrl + C` in the terminal to stop the server.

---

## 📁 Project Structure

```
SpaceExplorationGroqAi/
│
├── space_chatbot.py          # Main chatbot application
├── space_exploration.pdf     # Knowledge base PDF document
├── .env                       # Configuration file (API keys)
├── README.md                  # This documentation file
│
└── chroma_db/                 # Vector database (auto-generated)
    └── (database files)
```

### Key Files:

- **`space_chatbot.py`**: Main application with RAG pipeline and Gradio interface
- **`space_exploration.pdf`**: Source document for the knowledge base
- **`.env`**: Environment variables and API keys (keep private!)
- **`chroma_db/`**: Automatically created directory for vector embeddings

---

## 🔧 Technology Stack

### Core Technologies:

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **LLM** | Groq (llama-3.1-8b-instant) | Fast inference and text generation |
| **Framework** | LangChain | LLM application framework |
| **Vector DB** | ChromaDB | Document embeddings storage |
| **Embeddings** | HuggingFace (all-MiniLM-L6-v2) | Text vectorization |
| **PDF Loader** | PyPDF | Document processing |
| **UI** | Gradio | Web interface |
| **Monitoring** | LangSmith | Tracing and debugging |

### Architecture:

```
User Question
    ↓
Gradio Interface
    ↓
RAG Chain
    ↓
┌─────────────────┐
│  Retriever      │ ← Vector DB (Chroma)
│  (Find Context) │ ← Embeddings (HuggingFace)
└─────────────────┘
    ↓
┌─────────────────┐
│  LLM (Groq)     │ ← Context + Question
│  Generate Answer│
└─────────────────┘
    ↓
Response + History
```

---

## 🐛 Troubleshooting

### Common Issues:

#### 1. **"GROQ_API_KEY not found"**
   - **Solution**: Make sure you've set `GROQ_API_KEY` in your `.env` file
   - Verify the key starts with `gsk_`
   - Ensure there are no extra spaces

#### 2. **"PDF not found"**
   - **Solution**: Ensure `space_exploration.pdf` exists in the same folder
   - Or update `PDF_FILE` path in `.env`

#### 3. **"Module not found" errors**
   - **Solution**: Install missing packages:
     ```bash
     pip install langchain langchain-community langchain-groq
     pip install chromadb pypdf gradio python-dotenv langsmith
     ```

#### 4. **Slow Response Times**
   - First run takes longer (building vector database)
   - Subsequent runs are faster (uses cached embeddings)
   - Check your internet connection

#### 5. **LangSmith Tracing Not Working**
   - Set `LANGSMITH_TRACING=true` in `.env`
   - Verify your `LANGSMITH_API_KEY` is correct
   - Check project name matches in LangSmith dashboard

#### 6. **Port Already in Use (7860)**
   - Another application is using port 7860
   - Solution: Stop the other application or modify port in `space_chatbot.py`:
     ```python
     interface.launch(server_port=7861)  # Change to different port
     ```

### Getting Help:

- Check the terminal output for detailed error messages
- Verify all API keys are correctly formatted
- Ensure all dependencies are installed
- Try with LangSmith tracing disabled first

---

## 📝 Notes

### Best Practices:

1. **Never Commit `.env`**: Add `.env` to `.gitignore` to protect your API keys
2. **Rate Limits**: Be aware of Groq's free tier limits (30 req/min)
3. **PDF Quality**: Better quality PDFs yield better responses
4. **Question Style**: Ask specific questions for better answers

### Security:

- ✅ Store API keys in `.env` file
- ✅ Add `.env` to `.gitignore`
- ❌ Never hardcode API keys in code
- ❌ Never share your API keys publicly
- ❌ Never commit API keys to Git

### Performance Tips:

- The first run builds the vector database (slower)
- Subsequent runs reuse the cached database (faster)
- Delete `chroma_db/` folder to rebuild from scratch
- Use shorter PDFs for faster initialization

---

## 📞 Support

For issues with:
- **Groq API**: [https://console.groq.com/docs](https://console.groq.com/docs)
- **LangSmith**: [https://docs.smith.langchain.com](https://docs.smith.langchain.com)
- **LangChain**: [https://python.langchain.com/docs/](https://python.langchain.com/docs/)

---

## 📄 License

This project is for educational purposes. Please ensure you comply with the terms of service for Groq and LangSmith APIs.

---

**Happy Space Exploring! 🌌🚀**
