
#! OpenAI llm
from langchain_openai import ChatOpenAI, OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

openai_llm = ChatOpenAI(api_key = api_key, temperature=0, model="gpt-4o")


#! Mistral llm
from langchain_community.llms import CTransformers

mistral_llm = CTransformers(model='llama.cpp/models/Mistral-7B-Instruct-v0.2.Q4_0.gguf', 
                        model_type='mistral', 
                        config={'context_length': 2048}
                        )

from ctransformers import AutoModelForCausalLM

mistral_llm = AutoModelForCausalLM.from_pretrained("TheBloke/Llama-2-7B-GGML", gpu_layers=50)

mistral_llm = ctransformers.AutoModelForCausalLM.from_pretrained(model='llama.cpp/models/Mistral-7B-Instruct-v0.2.Q4_0.gguf',
                                                         model_type="gguf", 
                                                         gpu_layers=5, 
                                                         threads=24, 
                                                         reset=False, 
                                                         context_length=4000, 
                                                         temperature=0.1)
    


