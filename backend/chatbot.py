import os
import json
from typing import Dict, Any, List
from langchain_experimental.agents import create_csv_agent
from langchain.agents import AgentType
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from langchain.agents.agent import AgentOutputParser
from langchain.schema import AgentAction, AgentFinish
from langchain.output_parsers.json import SimpleJsonOutputParser
import traceback
import re
from llms import openai_llm

# Directory to store session files
SESSION_DIR = "session_data"

# Ensure the session directory exists
if not os.path.exists(SESSION_DIR):
    os.makedirs(SESSION_DIR)

class CustomOutputParser(AgentOutputParser):
    """
    Custom output parser to handle various response formats more flexibly
    """
    def parse(self, llm_output: str) -> AgentFinish:
        # Clean and process the output
        cleaned_output = llm_output.strip('`\'"')
        
        # Remove any additional prefixes or action indicators
        cleaned_output = re.sub(r'^(Final Answer:|Answer:|Observation:)', '', cleaned_output).strip()
        
        # Return as a final answer
        return AgentFinish(
            return_values={"output": cleaned_output},
            log=llm_output
        )

def load_session(session_id: str) -> List[str]:
    session_file = os.path.join(SESSION_DIR, f"{session_id}.json")
    if os.path.exists(session_file):
        with open(session_file, "r") as f:
            return json.load(f)
    return []

def save_session(session_id: str, context: List[str]):
    session_file = os.path.join(SESSION_DIR, f"{session_id}.json")
    with open(session_file, "w") as f:
        json.dump(context, f)

def generate_response(query: str, modelName: str, session_id: str) -> Dict[str, Any]:
    llm = openai_llm
    
    csv_files = ["data/synthetic-orders-data.csv", "data/synthetic-product-data.csv"]
    
    try:
        # Load session context
        context = load_session(session_id)
        
        # Add the query to the context
        context.append(f"User: {query}")
        
        # Create agent with enhanced error handling and custom output parser
        agent = create_csv_agent(
            llm,
            csv_files,
            verbose=True,
            agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            handle_parsing_errors=True,  
            output_parser=CustomOutputParser(),  
            max_iterations=5, 
            allow_dangerous_code=True
        )
        
        full_context = "\n".join(context)
        
        try:
            # Run the agent with the query
            response = agent.run(full_context)
            
            # Clean the response
            cleaned_response = response.strip('`\'"')
            
            # Remove any additional prefixes
            cleaned_response = re.sub(r'^(Final Answer:|Answer:|Observation:)', '', cleaned_response).strip()
            
            # Ensure we have a valid response
            if not cleaned_response:
                cleaned_response = "I apologize, but I encountered an issue processing your query. Please try again"
            
            # Store the response in the session context
            context.append(f"Assistant: {cleaned_response}")
            
            # Save the updated session context
            save_session(session_id, context)
            
            result = {
                "user_question": query,
                "main_answer": cleaned_response,
                "rating": 0
            }
            
            return result
        
        except Exception as run_error:
            # Comprehensive error handling
            print(f"Agent run error: {run_error}")
            print(traceback.format_exc())
            
            return {
                "user_question": query,
                "main_answer": f"I apologize, but I encountered an issue processing your query. Please try again",
                "rating": 0
            }
    
    except Exception as e:
        # Catch-all error handling
        print(f"Global exception occurred: {e}")
        print(traceback.format_exc())
        
        return {
            "user_question": query,
            "main_answer": f"I apologize, but I couldn't retrieve the relevant information. Please try again",
            "rating": 0
        }

# Example usage
if __name__ == "__main__":
    modelName = "OpenAI"
    session_id = "unique_session_id_07"

    # Test queries
    test_queries = [
        "Tell me about the product with ID 23568",
        "What is the price of nikon coolpix s32 digital camera white?",
        "was it returned?"
    ]

    for query in test_queries:
        result = generate_response(query, modelName, session_id)
        print(f"\n\nQuery: {query}")
        print("Result:", result)

