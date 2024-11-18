import os
from typing import Dict, Any, List
from langchain_experimental.agents import create_csv_agent
from langchain.agents import AgentType
from llms import *

def generate_response(query: str, modelName: str) -> Dict[str, Any]:

    models = {"OpenAI" : openai_llm}
    selected_llm = models[modelName]
    
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
        
        raw_response = agent.run(query)
        
        result = {
            "user_question": query,
            "main_answer": raw_response,
            "rating": 0
        }
        
        return result
    
    except Exception as e:
        # Error handling
        return {
            "user_question": query,
            "main_answer": f"Error occurred: {str(e)}",
            "rating": 0
        }

# Example usage
if __name__ == "__main__":
    query = "Tell me about the product with ID 23568"
    modelName = "OpenAI" 
    result = generate_response(query, modelName)
    print(result)