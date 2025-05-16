from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

model=ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.2
)

parser=JsonOutputParser()

template=PromptTemplate(
    template="Give me a summary of {topic} \n {format_instructions}",
    input_variables=["topic"],
    partial_variables={"format_instructions":parser.get_format_instructions()}

)

chain=template | model | parser

result=chain.invoke({"topic":'Healty lifestyle'})
print(result)