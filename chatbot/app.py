
import os
import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.messages import HumanMessage, AIMessage

# Load environment variables 
load_dotenv()

# Set up the Gemini model 
model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash-001", 
    temperature=0.2 
)

# Load the FAISS index 
load_directory = "faiss_index_hillier"
db = FAISS.load_local(
    load_directory,
    GoogleGenerativeAIEmbeddings(model="models/embedding-001"),
    allow_dangerous_deserialization=True  # Required for loading FAISS index
)
retriever = db.as_retriever(search_type='similarity', search_kwargs={"k": 4})

# Default prompt for the chatbot
PROMPT = """You are a helpful assistant. Answer using only the given context.
If the answer is not in the context, say "I don't know the answer."
CONTEXT:
"""

# Set up the Streamlit app
st.set_page_config(page_title="Simple RAG Chatbot", page_icon="🤖", layout="wide")
st.header("Simple RAG Chatbot 🤖")

def render_app():
    custom_css = """
        <style>
            .stTextArea textarea {font-size: 13px;}
        </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

    hide_streamlit_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
    """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)


    if 'chat_dialogue' not in st.session_state:
        st.session_state['chat_dialogue'] = []

    
    for message in st.session_state.chat_dialogue:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

   
    if prompt := st.chat_input("Ask me anything!"):
      
        st.session_state.chat_dialogue.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

       
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""

   
            retrieved_docs = retriever.invoke(prompt)
            context = ""
            for idx, doc in enumerate(retrieved_docs):
                context += f"\nChunk {idx}: {doc.page_content}"

      
            final_prompt = f"{PROMPT}{context}\nUser: {prompt}\nAssistant: "

        
            for chunk in model.stream([HumanMessage(content=final_prompt)]):
                full_response += chunk.content
                message_placeholder.markdown(full_response + "▌")  # Show typing effect

         
            message_placeholder.markdown(full_response)

       
        st.session_state.chat_dialogue.append({"role": "assistant", "content": full_response})


render_app()