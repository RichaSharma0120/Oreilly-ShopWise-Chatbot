#! OpenAI llm
from langchain_openai import ChatOpenAI, OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

openai_llm = ChatOpenAI(api_key = api_key, temperature=0, model="gpt-4o")

