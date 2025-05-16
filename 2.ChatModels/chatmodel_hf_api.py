from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="openchat/openchat-3.5-0106",
task="text-generation"
)


model=ChatHuggingFace(
    llm=llm
)

result=model.invoke("What the capital of Bangladesh")
print(result.content)