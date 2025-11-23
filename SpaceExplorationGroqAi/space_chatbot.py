"""
Space Exploration Chatbot

RAG-based chatbot using LangChain with:
- PDF document ingestion and chunking
- Chroma vector database with HuggingFace embeddings
- Groq LLM (llama-3.1-8b-instant)
- LangSmith tracing for monitoring
- Gradio web interface with chat history
"""
import os
import sys
from pathlib import Path
from typing import List
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.documents import Document
from langchain_groq import ChatGroq
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
import gradio as gr
from langsmith import traceable

# Load environment variables
load_dotenv()

# Configurations
PDF_FILE = os.getenv("PDF_FILE", "space_exploration.pdf")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
LANGSMITH_API_KEY = os.getenv("LANGSMITH_API_KEY")
LANGSMITH_PROJECT = os.getenv("LANGSMITH_PROJECT")
LANGSMITH_TRACING = True

def setup_langsmith_tracing():
    """Setup LangSmith tracing if API key is configured"""
    if LANGSMITH_API_KEY and LANGSMITH_TRACING:
        os.environ["LANGSMITH_TRACING"] = "true"
        os.environ["LANGSMITH_PROJECT"] = LANGSMITH_PROJECT
        print(f"LangSmith tracing enabled (Project: {LANGSMITH_PROJECT})")
        return True
    return False


class InMemoryChatMessageHistory(BaseChatMessageHistory):
    """In-memory chat message history for storing conversation"""
    
    def __init__(self):
        self.messages: list[BaseMessage] = []
    
    def add_message(self, message: BaseMessage) -> None:
        """Add a message to history"""
        self.messages.append(message)
    
    def clear(self) -> None:
        """Clear all messages"""
        self.messages = []


class SpaceExplorationChatbot:
    """Space Exploration Chatbot with RAG pipeline using Groq LLM"""
    
    def __init__(self):
        self.pdf_path = PDF_FILE
        self.message_history = InMemoryChatMessageHistory()
        self.chain = None
        self.retriever = None
        self.tracing_enabled = setup_langsmith_tracing()
        
        print("Space Exploration Chatbot - Initializing")
        print("-" * 60)
        
        try:
            # Load and split PDF
            self._load_and_split_pdf()
            
            # Initialize vector store
            self._initialize_vector_store()
            
            # Initialize LLM
            self._initialize_llm()
            
            # Create RAG chain
            self._create_rag_chain()
            
            print("Chatbot initialized successfully!")
            print("-" * 60 + "\n")
        
        except Exception as e:
            print(f"Initialization failed: {e}")
            print("-" * 60 + "\n")
            raise
    
    @traceable(name="load_and_split_pdf")
    def _load_and_split_pdf(self):
        """Load PDF and split into chunks"""
        print(f"Loading PDF: {self.pdf_path}")
        
        if not Path(self.pdf_path).exists():
            raise FileNotFoundError(f"PDF not found: {self.pdf_path}")
        
        # Load PDF
        loader = PyPDFLoader(self.pdf_path)
        documents = loader.load()
        print(f"Loaded {len(documents)} pages")
        
        # Split documents
        splitter = CharacterTextSplitter(
            chunk_size=120,
            chunk_overlap=15,
            separator="\n"
        )
        self.documents = splitter.split_documents(documents)
        print(f"Split into {len(self.documents)} chunks")
    
    @traceable(name="initialize_vector_store")
    def _initialize_vector_store(self):
        print("Initializing vector store (Chroma)...")
        
        # Using HuggingFace embeddings
        embeddings = HuggingFaceEmbeddings(
            model_name="all-MiniLM-L6-v2", 
            model_kwargs={"device": "cpu"}
        )
        
        print("Creating Chroma vector store...")
        self.vector_store = Chroma.from_documents(
            documents=self.documents,
            embedding=embeddings,
            collection_name="space_missions",
            persist_directory="./chroma_db"
        )
        print("Vector store created")
        
        self.retriever = self.vector_store.as_retriever(
            search_type="mmr",
            search_kwargs={"k": 3, "fetch_k": 10}
        )
    
    @traceable(name="initialize_llm")
    def _initialize_llm(self):
        print("Initializing LLM (Groq Cloud)...")
        
        if not GROQ_API_KEY:
            raise ValueError(
                "GROQ_API_KEY not found in environment variables."
                "Get a free key at: https://console.groq.com"
                "Set in .env: GROQ_API_KEY=gsk_xxxxx"
            )
        
        self.llm = ChatGroq(
            api_key=GROQ_API_KEY,
            model="llama-3.1-8b-instant",
            temperature=0.3,
            max_retries=2,
        )
        print("LLM initialized (llama-3.1-8b-instant)")
    
    @traceable(name="create_rag_chain")
    def _create_rag_chain(self):
        print("Creating RAG chain...")
        
        # Custom prompt template with better context handling
        prompt = ChatPromptTemplate.from_template("""You are SpaceBot, an expert guide to space exploration.

You have context information about space missions and astronomy.
IMPORTANT: Only use the context if it is relevant to the question.
If the context is not helpful or relevant, simply answer the question based on your knowledge.
Do not force irrelevant information into your response.

Context (use only if relevant):
{context}

Question: {question}

Answer:""")
        
        # Format documents
        def format_docs(docs: List[Document]) -> str:
            return "\n".join(doc.page_content for doc in docs)
        
        # Build LCEL chain
        self.chain = (
            {
                "context": self.retriever | (lambda docs: format_docs(docs)),
                "question": RunnablePassthrough()
            }
            | prompt
            | self.llm
            | StrOutputParser()
        )
        print("RAG chain created")
    
    @traceable(name="space_chatbot_query")
    def chat(self, user_message: str) -> str:
        """Process user message and return response"""
        try:
            response = self.chain.invoke(user_message)
            
            # Store in LangChain message history
            self.message_history.add_message(HumanMessage(content=user_message))
            self.message_history.add_message(AIMessage(content=response))
            
            return response
        
        except Exception as e:
            error_msg = f"Error: {str(e)}"
            print(f"Error during query: {error_msg}")
            return error_msg
    
    def get_history(self) -> str:
        """Get formatted chat history"""
        if not self.message_history.messages:
            return "No conversation history yet."
        
        history_text = "Chat History\n" + "-" * 40 + "\n\n"
        for i in range(0, len(self.message_history.messages), 2):
            if i + 1 < len(self.message_history.messages):
                user_msg = self.message_history.messages[i].content
                ai_msg = self.message_history.messages[i + 1].content
                history_text += f"Q{i // 2 + 1}: {user_msg}\n"
                history_text += f"A{i // 2 + 1}: {ai_msg}\n\n"
        return history_text
    
    def clear_history(self):
        """Clear chat history"""
        self.message_history.clear()
        return "Chat history cleared."


def create_gradio_interface(chatbot: SpaceExplorationChatbot):    
    greeting = "Hello, I am SpaceBot, your guide to space exploration. Ask me about missions or astronomy!"
    
    def process_query(user_input):
        if not user_input.strip():
            return "", chatbot.get_history()
        
        response = chatbot.chat(user_input)
        return response, chatbot.get_history()
    
    def clear_chat():
        chatbot.clear_history()
        return "", "", chatbot.get_history()
    
    with gr.Blocks(
        title="Space Exploration Chatbot",
        theme=gr.themes.Soft()
    ) as interface:
        gr.Markdown("""
        # Space Exploration Chatbot
        ## Your Guide to Space Missions and Astronomy
        """)
        
        gr.Markdown(f"*{greeting}*")
        
        with gr.Row():
            with gr.Column():
                user_input = gr.Textbox(
                    label="Your Question",
                    placeholder="Ask about Space Missions & Astronomy...",
                    lines=3
                )
                submit_btn = gr.Button("Submit", variant="primary")
                clear_btn = gr.Button("Clear History")
            
            with gr.Column():
                response_output = gr.Textbox(
                    label="Response",
                    lines=6,
                    interactive=False
                )
                history_output = gr.Textbox(
                    label="Chat History",
                    lines=8,
                    interactive=False,
                    value="No conversation history yet."
                )
        
        # Connect buttons
        submit_btn.click(
            process_query,
            inputs=[user_input],
            outputs=[response_output, history_output]
        ).then(lambda: "", outputs=user_input)
        
        clear_btn.click(
            clear_chat,
            inputs=[],
            outputs=[user_input, response_output, history_output]
        )
    
    return interface


def main():
    try:
        # Initialize chatbot
        chatbot = SpaceExplorationChatbot()
        
        # Create and launch Gradio interface
        print("Launching Gradio interface...")
        interface = create_gradio_interface(chatbot)
        interface.launch(
            server_name="127.0.0.1",
            server_port=7860,
            share=False,
            show_error=True,
        )
    
    except KeyboardInterrupt:
        print("Chatbot stopped by user")
        sys.exit(0)
    
    except Exception as e:
        print(f"Fatal error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
