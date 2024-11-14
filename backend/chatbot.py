# import pandas as pd
# import os
# from langchain_experimental.agents import create_csv_agent
# from langchain_openai import ChatOpenAI, OpenAI
# from langchain.agents.agent_types import AgentType
# from llm import *

# api_key = os.getenv("OPENAI_API_KEY")

# selected_llm = mistral_llm

# ##working
# agent = create_csv_agent(
#     selected_llm,
#     ["data/synthetic-orders-data.csv", "data/synthetic-product-data.csv"],
#     verbose=True,
#     agent_type=AgentType.OPENAI_FUNCTIONS,
#     allow_dangerous_code=True
# )

# agent = create_csv_agent(
#     selected_llm,
#     ["data/synthetic-orders-data.csv", "data/synthetic-product-data.csv"],
#     verbose=True,
#     agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
#     allow_dangerous_code=True,
#     handle_parsing_errors=True
# )

# result = agent.run("Tell me about the product with ID 23568")
# print(result)


import os
from typing import Dict, Any, List
from langchain_experimental.agents import create_csv_agent
from langchain.agents import AgentType
from llm import *

def generate_response(query: str) -> Dict[str, Any]:
    api_key = os.getenv("OPENAI_API_KEY")
    selected_llm = openai_llm
    
    # File paths
    csv_files = ["data/synthetic-orders-data.csv", "data/synthetic-product-data.csv"]
    
    try:
        # Create agent with specified configuration
        agent = create_csv_agent(
            selected_llm,
            csv_files,
            verbose=True,
            agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            allow_dangerous_code=True,
            handle_parsing_errors=True
        )
        
        # Get the raw response from agent
        raw_response = agent.run(query)
        
        # Format the result in the specified structure
        result = {
            "user_question": query,
            "main_answer": raw_response,
            "rating": 0,  # Default rating as specified
            "source_documents": csv_files  # Using input files as source documents
        }
        
        return result
    
    except Exception as e:
        # Error handling
        return {
            "user_question": query,
            "main_answer": f"Error occurred: {str(e)}",
            "rating": 0,
            "source_documents": []
        }

# Example usage
if __name__ == "__main__":
    query = "Tell me about the product with ID 23568"
    result = get_agent_response(query)
    print(result)