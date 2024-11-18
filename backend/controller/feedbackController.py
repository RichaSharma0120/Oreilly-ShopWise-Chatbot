from fastapi import APIRouter, Response

import json,os
from pydantic import BaseModel
from pymongo import MongoClient
from bson import ObjectId
from dotenv import load_dotenv
load_dotenv()

feedbackRouter = APIRouter()
mongo_url=os.getenv('MONGO_URL')

client = MongoClient(mongo_url)
db = client["shopwise_db"]
collection = db["shopwise_collection"]

class FeedbackData(BaseModel):
    stars_given: int = 0
    # feedback: Optional[str] = None
    # name: Optional[str] = None

@feedbackRouter.put('/submit_feedback')
def submit_feedback(feedback_data: FeedbackData, _id: str):
    try:
        print("in feedback controller")
        print("feedback data :", feedback_data)

        feedback_collection = collection

        print("feedback given!\n")

        query = {"_id": ObjectId(_id)}
        new_values = {
            "$set": {
                "stars_given": feedback_data.stars_given
            }
        }

        result = feedback_collection.update_one(query, new_values)

        if result.matched_count == 0:
            print("No documents matched the query. Update not applied.")
        else:
            print("Update applied successfully.")

        return Response(content=json.dumps({"message": "Feedback submitted successfully"}), status_code=200)

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return Response(content=json.dumps({"message": "Error submitting feedback"}), status_code=500)




