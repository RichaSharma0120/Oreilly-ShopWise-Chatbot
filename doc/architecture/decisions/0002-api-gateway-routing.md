# 2. API Gateway Routing

Date: 2024-11-14

## Status

Accepted

## Context

API gateways serve as a single entry point, streamlining and standardizing control over interactions between an organization's data, services, and applications with users. Since microservice architecture provides fault isolation where a failure in one service won't affect the entire application

## Decision

We have decided to go with FastAPI for creating RESTful APIs having high performance, when compared to other alternatives like Flask

## Consequences

After implementing FastApi our apis are performing faster as they do asynchronous I/O operations wherein it can handle multiple requests concurrently and automatic validation using Pydantic models without much of manual validations

Which to Use and When?

FastAPI is ideal for modern, performance-oriented applications that require speed, concurrency, and robust data validation.
Flask is a lightweight, flexible framework suited for simpler, traditional web applications where rapid prototyping and minimal setup are priorities.