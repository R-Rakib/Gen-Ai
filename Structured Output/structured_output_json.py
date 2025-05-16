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
json_schema = {
  "title": "Review",
  "type": "object",
  "properties": {
    "key_themes": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Write down all the key themes discussed in the review in a list"
    },
    "summary": {
      "type": "string",
      "description": "A brief summary of the review"
    },
    "sentiment": {
      "type": "string",
      "enum": ["pos", "neg"],
      "description": "Return sentiment of the review either negative, positive or neutral"
    },
    "pros": {
      "type": ["array", "null"],
      "items": {
        "type": "string"
      },
      "description": "Write down all the pros inside a list"
    },
    "cons": {
      "type": ["array", "null"],
      "items": {
        "type": "string"
      },
      "description": "Write down all the cons inside a list"
    },
    "name": {
      "type": ["string", "null"],
      "description": "Write the name of the reviewer"
    }
  },
  "required": ["key_themes", "summary", "sentiment"]
}


structured_model=model.with_structured_output(json_schema)
result=structured_model.invoke("The Samsung Galaxy S24 Ultra is a powerhouse flagship phone that combines top-tier performance with stunning design. Its 6.8-inch AMOLED display offers vibrant colors and smooth 120Hz refresh, making media consumption a delight. Powered by the Snapdragon 8 Gen 3 chip and featuring a 200MP main camera, it excels in both speed and photography. The battery life easily lasts a full day, and fast charging adds convenience.")

print(result)
