from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
from typing import TypedDict,Annotated,Optional
from pydantic import BaseModel, Field

load_dotenv()

model=ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.2
)

#Schema

class Review(BaseModel):
   key_themes:list[str]=Field(description="key themes of the review in a list") 
   summary:str=Field(description='A breif summary of the review')
   sentiment:str=Field(description='Return the sentimant oth the review either postive ,negartive or neutral')  
   pros:Optional[list[str]]=Field(description='list all the positive aspects of the product in a list')    
   cons:Optional[list[str]]=Field(description='list all the negative aspects of the product in a list')
structured_model=model.with_structured_output(Review)
result=structured_model.invoke("The Samsung Galaxy S24 Ultra is a powerhouse flagship phone that combines top-tier performance with stunning design. Its 6.8-inch AMOLED display offers vibrant colors and smooth 120Hz refresh, making media consumption a delight. Powered by the Snapdragon 8 Gen 3 chip and featuring a 200MP main camera, it excels in both speed and photography. The battery life easily lasts a full day, and fast charging adds convenience.")

print(result)
result=dict(result)
print(result['summary'])
print(result['sentiment'])
print(result['key_themes'])
print(result['pros'])
print(result['cons'])