# Oreilly-ShopWise-Chatbot

ShopWise is an intelligent, context-aware chatbot designed to help users query CSV files and retrieve relevant information efficiently. This application empowers users by providing instant answers based on the data in the provided CSV files, ensuring accurate and contextual responses tailored to their queries.

### Access the website on this url : https://talktodata.valtech.co.in/
### Documentation can also be accessed on https://github.com/Valtech-AIML-Team/Oreilly-ShopWise-Chatbot/blob/master/ShopWise%20ChatBot%20Details.pdf

## Key features of ShopWise include:

- CSV Querying: Users can upload CSV files and perform natural language queries to extract meaningful insights.
- Context Awareness: The chatbot retains conversational context, enabling a seamless and intuitive user experience.
- User Feedback: Users can provide feedback on the responses, helping to improve the system's accuracy and relevance over time.

ShopWise is a versatile tool designed for users who need quick, reliable insights from structured data while maintaining a user-friendly conversational interface.


## Installation Instructions

### Clone the repository
1. Clone the repository to your local machine:
```
  git clone https://github.com/Valtech-AIML-Team/Oreilly-ShopWise-Chatbot.git
  cd Oreilly-ShopWise-Chatbot
```

### Backend Dependencies
2. Navigate to the backend directory and install the required dependencies:
```
   cd backend/
   pip install -r requirements.txt
```

### Frontend Dependencies
3. Navigate to the frontend directory and install the dependencies:
```
   cd frontend/
   npm i
```

## Running the Application

### Start the Backend
1. Navigate to the backend directory and run the application using the following command:
```
   cd backend/
   uvicorn main:app --reload
```

### Start the Frontend
2. Navigate to the frontend directory and start the development server:
```
   cd frontend/
   npm run dev
```

## Notes:
1. Add .env files in backend and frontend directories
2. With the steps above, the backend will be running locally (usually at http://127.0.0.1:8000), and the frontend will be accessible at the development server URL provided in the terminal (typically http://localhost:3000).


## Future Roadmaps:
1. Apart from current OpenAI llm, other alternative llms can be used by having a dropdown containing all llms in header section.
2. Dashboard can be created for creating graphs and charts based on orders and products for data analysis.





  

  
