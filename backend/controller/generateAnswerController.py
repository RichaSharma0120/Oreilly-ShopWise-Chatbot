from fastapi import APIRouter, Response, HTTPException, Header
from pymongo import MongoClient
from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime, timezone
import json
import os
from bson import ObjectId, json_util
from dotenv import load_dotenv
load_dotenv()
import pytz

from chatbot import generate_response 

generateAnswerRouter = APIRouter()

mongo_url = os.getenv('MONGO_URL')
client = MongoClient(mongo_url)
db = client["shopwise_db"]
collection = db["shopwise_collection"]

class QuestionAnswer(BaseModel):
    _id: ObjectId
    question: str
    answer: str
    stars_given: int = 0
    created_at: datetime
    name: Optional[str] = None

@generateAnswerRouter.post('/generate_answer')
async def generate_answer(queryText: str, name: str = None, modelName: str = None):
    try:
        print("\nin try block of generate answer controller")
        # answer = generate_response(queryText, modelName)
        answer = generate_response(queryText, modelName)
        
        ist_timezone = pytz.timezone('Asia/Kolkata')
        current_time_ist = datetime.now(timezone.utc).astimezone(ist_timezone)
        
        current_time_naive = current_time_ist.replace(tzinfo=None)
        
        # Create QuestionAnswer instance
        response_obj = QuestionAnswer(
            question=answer["user_question"],
            answer=answer["main_answer"],
            stars_given=answer["rating"],
            name=name,
            _id=ObjectId(),
            created_at=current_time_naive
        )
        
        # Convert to dict and store in MongoDB
        response_dict = response_obj.dict()
        new_response = collection.insert_one(response_dict)
            
        # Prepare response data
        response_data = {
            "_id": str(new_response.inserted_id),
            "user_question": answer["user_question"],
            "main_answer": answer["main_answer"],
            "rating": answer["rating"],
            "name": name,
            "created_at": current_time_naive.isoformat()
        }
        
        # Convert response to JSON and return
        json_content = json.dumps(response_data, default=json_util.default).encode('utf-8')
        return Response(content=json_content, status_code=200)
    
    except Exception as e:
        print(f"Error in agent query controller: {str(e)}")
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")



