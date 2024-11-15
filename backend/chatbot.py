import os
from typing import Dict, Any, List
from langchain_experimental.agents import create_csv_agent
from langchain.agents import AgentType
import pandas as pd
from llm import openai_llm, mistral_llm
def generate_response(query: str, model_name: str) -> Dict[str, Any]:

    models = {"Mistral" : mistral_llm, 
              "OpenAI" : openai_llm}

    selected_llm_model = models[model_name]
    
    csv_files = ["data/synthetic-orders-data.csv", "data/synthetic-product-data.csv"]
    
    try:
        agent = create_csv_agent(
            selected_llm_model,
            csv_files,
            verbose=True,
            agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            allow_dangerous_code=True,
            # handle_parsing_errors=True,
            max_iterations=3,  
            early_stopping_method="force"
        )
 
        raw_response = agent.run(query)
        
        result = {
            "user_question": query,
            "main_answer": raw_response,
            "rating": 0
        }
        
        return result
    
    except Exception as e:
        return {
            "user_question": query,
            "main_answer": f"Error occurred: {str(e)}",
            "rating": 0,
            "source_documents": []
        }

if __name__ == "__main__":
    query = "Tell me about the product with ID 23568"
    result = generate_response(query)
    print(result)