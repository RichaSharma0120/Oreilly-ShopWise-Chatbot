#! llms

#! llama_cpp llm
from langchain_community.llms import LlamaCpp
from langchain_core.callbacks import CallbackManager, StreamingStdOutCallbackHandler

callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])

llama_llm = LlamaCpp(
    model_path="llama.cpp/models/llama-3.2-1b-instruct-q8_0.gguf",  
    temperature=0.75,
    max_tokens=2000,
    top_p=1,
    callbacks=[StreamingStdOutCallbackHandler()],
    verbose=True,
)

#! GPT4All llm
from langchain_community.llms import GPT4All
from langchain_core.callbacks import BaseCallbackHandler

count = 0

class MyCustomHandler(BaseCallbackHandler):
    def on_llm_new_token(self, token: str, **kwargs) -> None:
        global count
        if count < 10:
            print(f"Token: {token}")
            count += 1

gpt4all_llm = GPT4All(model="llama.cpp/models/llama-3.2-1b-instruct-q8_0.gguf",
              callbacks=[MyCustomHandler()], streaming=True)

#! OpenAI llm
from langchain_openai import ChatOpenAI, OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

# openai_llm = OpenAI(api_key=api_key, temperature=0, model="gpt-3.5-turbo-0613")
openai_llm = ChatOpenAI(api_key = api_key, temperature=0, model="gpt-4o")


#! Mistral llm
### steps for installation-------
## pip install --upgrade vllm
## pip install --upgrade mistral_common

# from vllm import LLM
# from vllm.sampling_params import SamplingParams
# from vllm.config import DeviceConfig

# model_name = "mistralai/Mistral-Small-Instruct-2409"

# sampling_params = SamplingParams(max_tokens=8192)
# device = "cpu"

# sampling_params = SamplingParams(max_tokens=8192)
# mistral_llm = LLM(
#     model=model_name,
#     tokenizer_mode="mistral",
#     config_format="mistral",
#     load_format="mistral",
#     device="cpu"  # specify CPU as the device if GPU is unavailable
# )
