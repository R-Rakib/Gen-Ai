RAG-Based Chatbot on "Advanced Machining Processes" by V.K. Jain

This project is a Retrieval-Augmented Generation (RAG) based chatbot built using LangChain, FAISS, and Gemini 2.0 Flash-001. 
The chatbot is trained on content from the academic textbook "Advanced Machining Processes" by Prof. V.K. Jain, enabling it to answer 
complex questions related to non-traditional machining processes.

🔍 Overview

The chatbot uses:
- FAISS for efficient similarity-based retrieval of document chunks
- LangChain to integrate the retrieval pipeline and LLM
- Gemini 2.0 Flash (001) as the core language model for response generation

It can accurately answer queries from topics like:
- Electrical Discharge Machining (EDM)
- Electrochemical Machining (ECM)
- Ultrasonic Machining (USM)
- Laser Beam Machining (LBM)
- Abrasive Jet Machining (AJM)
- And more!

📌 Key Features

- Query answering using textbook-based knowledge
- Context-aware and fact-based replies
- Powered by Google’s Gemini-2.0-Flash LLM
- Fast vector search using FAISS
- Easily extendable to other academic resources

🛠 Tech Stack

| Component        | Tool / Framework           |
|------------------|----------------------------|
| Language Model   | Gemini 2.0 Flash (001)     |
| Retrieval        | FAISS                      |
| Framework        | LangChain                  |
| Programming Lang | Python                     |
| Interface        | CLI or Streamlit (optional)|

📂 Project Structure

├── data/                 # PDF/Text chunks of the book
├── embeddings/           # Vector store (FAISS)
├── chatbot/              # LangChain RAG logic
├── app.py                # Main script / UI
├── requirements.txt
└── README.md

