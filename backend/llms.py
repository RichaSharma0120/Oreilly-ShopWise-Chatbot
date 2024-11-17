
#! OpenAI llm
from langchain_openai import ChatOpenAI, OpenAI
import os
from dotenv import load_dotenv
load_dotenv()
from langchain.llms.base import LLM
from typing import Any, Dict, List, Optional

api_key = os.getenv("OPENAI_API_KEY")

openai_llm = ChatOpenAI(api_key = api_key, temperature=0, model="gpt-4o")


#! Mistral llm
# from langchain_community.llms import CTransformers

# mistral_llm = CTransformers(model='llama.cpp/models/Mistral-7B-Instruct-v0.2.Q4_0.gguf', 
#                         model_type='mistral', 
#                         config={'context_length': 2048}
#                         )

class CTransformersLLM(LLM):
    model: Any
    
    def __init__(self, model):
        super().__init__()
        self.model = model
    
    @property
    def _llm_type(self) -> str:
        return "custom_ctransformers"
    
    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        response = self.model(prompt)
        return response

from ctransformers import AutoModelForCausalLM

# mistral_llm = AutoModelForCausalLM.from_pretrained("TheBloke/Llama-2-7B-GGML", gpu_layers=50)

mistral_llm = CTransformersLLM(AutoModelForCausalLM.from_pretrained("TheBloke/Llama-2-7B-GGML",
                                                                    gpu_layers=50))

# mistral_llm = ctransformers.AutoModelForCausalLM.from_pretrained(model='llama.cpp/models/Mistral-7B-Instruct-v0.2.Q4_0.gguf',
#                                                          model_type="gguf", 
#                                                          gpu_layers=5, 
#                                                          threads=24, 
#                                                          reset=False, 
#                                                          context_length=4000, 
#                                                          temperature=0.1)
    


