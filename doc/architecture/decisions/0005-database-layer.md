# 5. Database Layer

Date: 2024-11-14

## Status

Accepted

## Context

A database is required to efficiently store, manage, and access large amounts of structured data, ensuring its accuracy, consistency, and integrity. We wanted to store feedback details of response generated such as user queries, respective responses, ratings given, model details to generate response, user's name and feedback timestamp.

## Decision

We chose to store in MongoDB compared to other like MySQL, PostgreSQL or any.

## Consequences

In near future, apart from users feedback data, extra parameters or details of the products might be added which would be helpful in data analysis, so a flexible schema is required which can change in real time including unstructured data.

Which to Use and When?

MongoDB is best for applications needing flexibility, unstructured data handling, and horizontal scalability.
Applications related to real-time analytics or content management.
PostgreSQL is preferred for complex queries, strong data integrity, and transactional applications 
Applications related to financial systems or enterprise applications.


How MongoDB Helps in LLM based applications:

1) Storing Chat History & Conversations	    
MongoDB can efficiently store user conversations, chat history, and interaction logs as documents, enabling quick retrieval and context management for LLMs.

2) Caching LLM Responses	
You can use MongoDB to cache frequently accessed LLM responses, reducing response times and improving overall system performance.

3) Storing User Profiles & Preferences	
Flexible schema allows storing user-specific data, such as preferences, interaction history, and personalized prompts, aiding in context-aware LLM responses.

4) Logging and Analytics	
MongoDB's aggregation framework and flexible document model can be used for logging, monitoring, and analyzing LLM performance, including prompt effectiveness.