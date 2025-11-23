# 🚀 Space Exploration Chatbot - GenAI Projects

A collection of RAG (Retrieval-Augmented Generation) based chatbots that answer questions about space exploration and astronomy using PDF documents as knowledge base.

## 🎯 Available Versions

This repository contains **two versions** of the Space Exploration Chatbot:

### 1. **SpaceExplorationGroqAI** - Cloud-Based (Online)
- Uses **Groq API** with llama-3.1-8b-instant model
- **Fast inference** with cloud computing
- Requires internet connection
- Free tier available (30 req/min)
- ✅ Best for: Quick setup, no local resources needed

### 2. **SpaceExplorationllama3** - Ollama-Based (Offline)
- Uses **Ollama** with llama3 model running locally
- **Complete offline** functionality
- No API costs or rate limits
- Response caching for faster repeated queries
- ✅ Best for: Privacy, offline use, unlimited queries

## 📋 Table of Contents
- [Available Versions](#-available-versions)
- [Features Comparison](#-features-comparison)
- [Quick Start Guide](#-quick-start-guide)
- [Prerequisites](#-prerequisites)
- [Project Setup](#-project-setup)
  - [Setup: SpaceExplorationGroqAI (Cloud)](#1-spaceexplorationgroqai-cloud-based)
  - [Setup: SpaceExplorationllama3 (Offline)](#2-spaceexplorationllama3-ollama-offline)
- [Getting API Keys](#-getting-api-keys)
- [Project Structure](#-project-structure)
- [Technology Stack](#-technology-stack)
- [Troubleshooting](#-troubleshooting)

## ⚖️ Features Comparison

| Feature | GroqAI (Cloud) | Ollama (Offline) |
|---------|----------------|------------------|
| **Internet Required** | ✅ Yes | ❌ No |
| **Setup Complexity** | 🟢 Easy | 🟡 Medium |
| **Response Speed** | ⚡ Very Fast | 🚶 Moderate |
| **API Costs** | Free Tier | Free Forever |
| **Rate Limits** | 30/min | Unlimited |
| **Privacy** | Cloud Processing | 100% Local |
| **Resource Usage** | Low | High (RAM/CPU) |
| **Response Caching** | ❌ No | ✅ Yes |
| **LangSmith Tracing** | ✅ Yes | ✅ Yes |
| **Gradio Interface** | ✅ Yes | ✅ Yes |

## 🚀 Quick Start Guide

### Choose Your Version:

**Want fast, cloud-based responses?** → Use **SpaceExplorationGroqAI**
```bash
cd SpaceExplorationGroqAi
pip install -r requirements.txt
# Add GROQ_API_KEY to .env file
python space_chatbot.py
```

**Want complete offline privacy?** → Use **SpaceExplorationllama3**
```bash
# Install Ollama first
ollama pull llama3
ollama serve

cd SpaceExplorationllama3
pip install -r requirements.txt
python space_chatbot.py
```

## 📦 Prerequisites

### Common Requirements (Both Versions):
- Python 3.8 or higher
- pip (Python package manager)
- PDF document for knowledge base

### Additional Requirements by Version:

**For SpaceExplorationGroqAI:**
- Internet connection
- Groq API key (free tier available)
- LangSmith API key (optional, for monitoring)

**For SpaceExplorationllama3:**
- Ollama installed locally ([Download](https://ollama.ai))
- Minimum 8GB RAM recommended
- LangSmith API key (optional, for monitoring)

---

## 🛠️ Project Setup

## 1. SpaceExplorationGroqAI (Cloud-Based)

### Installation Steps:

```bash
# Navigate to project folder
cd SpaceExplorationGroqAi

# Install dependencies
pip install -r requirements.txt
```

### Configuration:

Edit `.env` file with your API keys:

```env
# Required: Groq API Key
GROQ_API_KEY=gsk_your_actual_groq_api_key_here

# Optional: LangSmith Configuration
LANGSMITH_API_KEY=lsv2_pt_your_langsmith_api_key_here
LANGSMITH_PROJECT=space-exploration-chatbot
LANGSMITH_TRACING=true
```

### Running:

```bash
python space_chatbot.py
```

Access at: `http://127.0.0.1:7860`

### Features:
- ⚡ Ultra-fast responses (Groq cloud inference)
- 🌐 Cloud-based processing
- 📊 LangSmith tracing support
- 💬 Chat history tracking
- 🎨 Gradio web interface

**Detailed documentation:** All setup and usage information is in this README file.

---

## 2. SpaceExplorationllama3 (Ollama Offline)

### Installation Steps:

**Step 1: Install Ollama**

- **macOS/Linux:**
  ```bash
  # Visit https://ollama.ai and download, or:
  curl -fsSL https://ollama.ai/install.sh | sh
  ```

- **Windows:**
  - Download from [https://ollama.ai/download](https://ollama.ai/download)

**Step 2: Pull llama3 Model**

```bash
ollama pull llama3
```

**Step 3: Start Ollama Server**

```bash
ollama serve
```

Keep this terminal running. Open a new terminal for next steps.

**Step 4: Install Python Dependencies**

```bash
# Navigate to project folder
cd SpaceExplorationllama3

# Install dependencies
pip install -r requirements.txt
```

### Configuration:

Edit `.env` file (optional - only if using LangSmith):

```env
# Optional: LangSmith Configuration
LANGSMITH_API_KEY=lsv2_pt_your_langsmith_api_key_here
LANGSMITH_PROJECT=space-exploration-chatbot
LANGSMITH_TRACING=true
```

### Running:

```bash
python space_chatbot.py
```

Access at: `http://127.0.0.1:7860`

### Features:
- 🔒 100% offline - complete privacy
- 💾 Response caching for faster repeated queries
- 🚫 No API costs or rate limits
- 📊 LangSmith tracing support (optional)
- 💬 Chat history tracking
- 🎨 Gradio web interface

### System Requirements:
- **RAM**: 8GB minimum (16GB recommended)
- **Storage**: ~4GB for llama3 model
- **CPU**: Modern multi-core processor

---

## 🔑 Getting API Keys

### 1. Groq API Key (Required for SpaceExplorationGroqAI only)

Groq provides fast LLM inference with a generous free tier. **Note**: Only needed if you're using the cloud-based SpaceExplorationGroqAI version.

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

### 2. LangSmith API Key (Optional for Both Versions)

LangSmith provides monitoring, tracing, and debugging for LLM applications. **This is completely optional** for both versions and only needed if you want advanced monitoring.

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

## 💡 Usage Examples

### Example Questions to Ask:

Both chatbots can answer questions like:
- "What are the major space exploration missions?"
- "Tell me about Mars exploration"
- "What is the International Space Station?"
- "Explain black holes"
- "Who was the first person in space?"
- "What are the phases of the moon?"
- "Tell me about the Hubble Space Telescope"

### Using the Web Interface:

1. **Open Browser**: Navigate to `http://127.0.0.1:7860`
2. **Type Question**: Enter your question in the text box
3. **Submit**: Click the "Submit" button
4. **View Response**: See the answer in the Response section
5. **Check History**: View all Q&A in Chat History
6. **Clear**: Click "Clear History" to start fresh

### Stopping the Chatbot:

Press `Ctrl + C` in the terminal to stop the server.

---

---

## 📁 Project Structure

```
GenAI/
│
├── README.md                          # This file - Universal documentation for both projects
├── requirements.txt                   # Common dependencies (if any)
│
├── SpaceExplorationGroqAi/           # Cloud-based version
│   ├── space_chatbot.py              # Main application (Groq API)
│   ├── space_exploration.pdf         # Knowledge base PDF
│   ├── .env                          # API keys configuration
│   ├── requirements.txt              # Project dependencies
│   └── chroma_db/                    # Vector database (auto-generated)
│
└── SpaceExplorationllama3/           # Offline version
    ├── space_chatbot.py              # Main application (Ollama)
    ├── space_exploration.pdf         # Knowledge base PDF
    ├── .env                          # Optional LangSmith config
    ├── requirements.txt              # Project dependencies
    └── chroma_db/                    # Vector database (auto-generated)
```

---

## 🔧 Technology Stack

### Common Technologies (Both Versions):

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Framework** | LangChain | LLM application framework |
| **Vector DB** | ChromaDB | Document embeddings storage |
| **Embeddings** | HuggingFace (all-MiniLM-L6-v2) | Text vectorization |
| **PDF Loader** | PyPDF | Document processing |
| **UI** | Gradio | Web interface |
| **Monitoring** | LangSmith | Tracing and debugging (optional) |

### Version-Specific:

**SpaceExplorationGroqAI:**
- **LLM**: Groq Cloud API (llama-3.1-8b-instant)
- **Deployment**: Cloud-based
- **Connection**: Internet required

**SpaceExplorationllama3:**
- **LLM**: Ollama (llama3 local)
- **Deployment**: Self-hosted
- **Connection**: Offline capable
- **Caching**: In-memory response cache

---

## 🐛 Troubleshooting

### Common Issues (Both Versions):

#### 1. **"PDF not found"**
   - **Solution**: Ensure `space_exploration.pdf` exists in the respective project folder
   - Or update `PDF_FILE` path in `.env`

#### 2. **"Module not found" errors**
   - **Solution**: Install missing packages:
     ```bash
     pip install -r requirements.txt
     ```

#### 3. **Slow First Run**
   - First run takes longer (building vector database)
   - Subsequent runs are faster (uses cached embeddings)

#### 4. **Port Already in Use (7860)**
   - Another application is using port 7860
   - Solution: Change port in `space_chatbot.py`:
     ```python
     interface.launch(server_port=7861)  # Different port
     ```

---

### SpaceExplorationGroqAI Specific:

#### 1. **"GROQ_API_KEY not found"**
   - **Solution**: Set `GROQ_API_KEY` in `.env` file
   - Verify the key starts with `gsk_`
   - Ensure no extra spaces

#### 2. **Rate Limit Errors**
   - Groq free tier: 30 requests/minute
   - Wait a minute or upgrade plan

#### 3. **Slow Response Times**
   - Check your internet connection
   - Groq cloud may be experiencing high load

---

### SpaceExplorationllama3 Specific:

#### 1. **"Ollama server not running"**
   - **Solution**: Start Ollama server:
     ```bash
     ollama serve
     ```
   - Keep the terminal running

#### 2. **"Model not found"**
   - **Solution**: Pull the llama3 model:
     ```bash
     ollama pull llama3
     ```

#### 3. **Very Slow Responses**
   - Ollama needs sufficient RAM (8GB minimum)
   - Close other applications
   - First query is slowest (model loading)
   - Cached queries are instant

#### 4. **Connection Refused (localhost:11434)**
   - Ollama server is not running
   - Start with: `ollama serve`
   - Check if port 11434 is available

#### 5. **Out of Memory Errors**
   - llama3 requires ~8GB RAM
   - Close other applications
   - Consider using smaller model: `ollama pull llama3:8b`

---

### LangSmith Tracing (Both Versions):

#### 1. **LangSmith Not Working**
   - Set `LANGSMITH_TRACING=true` in `.env`
   - Verify `LANGSMITH_API_KEY` is correct
   - Check project name matches in LangSmith dashboard

#### 2. **Disable Tracing**
   - Set `LANGSMITH_TRACING=false` in `.env`
   - Or remove `LANGSMITH_API_KEY`

---

## 📝 Notes & Best Practices

### Security:

- ✅ Store API keys in `.env` file
- ✅ Add `.env` to `.gitignore`
- ❌ Never hardcode API keys in code
- ❌ Never share your API keys publicly
- ❌ Never commit API keys to Git

### Performance Tips:

**Both Versions:**
- First run builds vector database (slower)
- Subsequent runs reuse cached database (faster)
- Delete `chroma_db/` folder to rebuild from scratch
- Use shorter PDFs for faster initialization

**GroqAI Specific:**
- Be aware of rate limits (30 requests/min on free tier)
- Cloud processing = fast responses
- Requires stable internet connection

**Ollama Specific:**
- First query loads model into memory (slower)
- Cached responses are instant
- Close other apps for better performance
- 8GB+ RAM recommended for smooth operation

### When to Use Each Version:

**Use GroqAI when:**
- ⚡ You need fastest responses
- 🌐 Internet connection is reliable
- 💻 Limited local resources
- 🆓 Free tier limits are acceptable

**Use Ollama when:**
- 🔒 Privacy is critical
- 📴 Offline access needed
- 🚫 Want no usage limits
- 💾 Have sufficient RAM/CPU

---

## 🔗 Additional Resources

### Documentation:
- **Groq API**: [https://console.groq.com/docs](https://console.groq.com/docs)
- **Ollama**: [https://ollama.ai/docs](https://ollama.ai/docs)
- **LangSmith**: [https://docs.smith.langchain.com](https://docs.smith.langchain.com)
- **LangChain**: [https://python.langchain.com/docs/](https://python.langchain.com/docs/)

### Useful Ollama Commands:
```bash
# List installed models
ollama list

# Pull a model
ollama pull llama3

# Remove a model
ollama rm llama3

# Run model in terminal (test)
ollama run llama3

# Start Ollama server
ollama serve
```

---

## 🤝 Contributing

Feel free to fork, modify, and use these projects for your own learning. If you make improvements, consider sharing them!

---

## 📄 License

This project is for educational purposes. Please ensure you comply with the terms of service for:
- Groq API
- Ollama
- LangSmith
- All other third-party services

---

**Happy Space Exploring! 🌌🚀✨**

*Choose your version: Cloud-powered speed or local privacy - both deliver excellent results!*
