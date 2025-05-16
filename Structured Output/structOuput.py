from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
from typing import TypedDict,Annotated,Optional

load_dotenv()


model=ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.2
)

#Schema

class Review(TypedDict):
    key_themes:Annotated[list[str],"key themes of the review in a list"]
    summary:Annotated[str, "A brief summary of the review"]
    sentiment:Annotated[str,"Return the sentimant oth the review either postive ,negartive or neutral"]
    pros:Annotated[Optional[list[str]],"list all the positive aspects of the product in a list"]
    cons:Annotated[Optional[list[str]],"list all the negative aspects of the product in a list"]
structured_model=model.with_structured_output(Review)
result=structured_model.invoke("The Samsung Galaxy S24 Ultra is a powerhouse flagship phone that combines top-tier performance with stunning design. Its 6.8-inch AMOLED display offers vibrant colors and smooth 120Hz refresh, making media consumption a delight. Powered by the Snapdragon 8 Gen 3 chip and featuring a 200MP main camera, it excels in both speed and photography. The battery life easily lasts a full day, and fast charging adds convenience.")

print(result)
print(result['summary'])
print(result['sentiment'])
print(result['key_themes'])
print(result['pros'])
print(result['cons'])