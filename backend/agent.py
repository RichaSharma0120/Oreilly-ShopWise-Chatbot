from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain.tools import Tool
import pandas as pd
from llms import *

def create_dataframe_query_agent(selected_llm_model):

    df1 = pd.read_csv("data/synthetic-orders-data.csv")
    df2 = pd.read_csv("data/synthetic-product-data.csv")
    
    pandas_agent = create_pandas_dataframe_agent(
        selected_llm_model,
        [df1, df2],
        verbose=True,
        agent_type="openai-functions",  
        handle_parsing_errors=True,
        allow_dangerous_code=True 
    )
    
    # Create a tool that uses the pandas agent
    tools = [
        Tool(
            name="Query_Dataframes",
            func=pandas_agent.run,
            description="Useful for querying and analyzing data from the orders and products datasets. Input should be a natural language question about the data."
        )
    ]
    
    prompt = hub.pull("hwchase17/react")
    
    agent = create_react_agent(
        llm=selected_llm_model,
        tools=tools,
        prompt=prompt
    )
    
    agent_executor = AgentExecutor.from_agent_and_tools(
        agent=agent,
        tools=tools,
        handle_parsing_errors=True,
        verbose=True,
        max_iterations=5  
    )
    
    return agent_executor

def generate_response(query: str, model_name: str):
    try:
        models = { 
              "OpenAI" : openai_llm,
              "Llama": llama_llm,
              "GPT4All": gpt4all_llm,
              "Mistral": mistral_llm}

        selected_llm_model = models[model_name]
        
        agent_executor = create_dataframe_query_agent(selected_llm_model)
        
        response = agent_executor.invoke(
            {
                "input": query
            }
        )
        
        print("--------------------------------")
        print("response: ", response)

        result = {
                "user_question": query,
                "main_answer": response["output"],
                "rating": 0
            }
        
        return result
    
    except Exception as e:
        error_msg = str(e)
        print("\n\nError: ", error_msg)
        return {
            "user_question": query,
            "main_answer": "I encountered an issue processing the data.",
            "rating": 0
        }

if __name__ == "__main__":
    agent_executor = create_dataframe_query_agent()
    
    response = agent_executor.invoke(
        {
            "input": "give me details about product ID 11339"
        }
    )
    print(response)