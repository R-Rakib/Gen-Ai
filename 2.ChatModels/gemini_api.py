import os
from dotenv import load_dotenv

load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI


model=ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.2
)

result=model.invoke("Write a poem about the capital of Bangladesh")
print(result.content)