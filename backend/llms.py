
#! OpenAI llm
from langchain_openai import ChatOpenAI, OpenAI
import os
from dotenv import load_dotenv
load_dotenv()
from langchain.llms.base import LLM
from typing import Any, Dict, List, Optional

api_key = os.getenv("OPENAI_API_KEY")

openai_llm = ChatOpenAI(api_key = api_key, temperature=0, model="gpt-4o")

from langchain_community.llms import LlamaCpp
from langchain_core.callbacks import CallbackManager, StreamingStdOutCallbackHandler

callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])
llama_llm = LlamaCpp(
    model_path="llama.cpp/models/llama-3.2-1b-instruct-q8_0.gguf",
    temperature=0.75,
    max_tokens=2000,
    n_ctx=4096,  # Increase context window
    top_p=1,
    callback_manager=callback_manager,
    verbose=True,
    n_batch=512,  # Add batch size for better memory handling
    f16_kv=True,  # Enable memory efficiency option
)


#! GPT4ALl llm

from langchain_community.llms import GPT4All

gpt4all_llm = GPT4All(model="llama.cpp/models/Meta-Llama-3-8B-Instruct.Q4_0.gguf", n_threads=8)

    


