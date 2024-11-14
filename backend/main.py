from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controller import generateAnswerController, feedbackController

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(generateAnswerController.generateAnswerRouter)
app.include_router(feedbackController.feedbackRouter)