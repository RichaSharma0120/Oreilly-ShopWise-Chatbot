# 7. Mistral LLM Model

Date: 2024-11-15

## Status

Accepted

## Context

A simple machine learning models, which struggle with context, ambiguity, and natural language while interacting with humans even after having written big amount of code. However, by using LLMs, applications can perform a wide range of language-related tasks—like answering questions, summarizing text, automating customer support and generating content. Thereby enhancing productivity, improving user experiences, and automating complex workflows.

## Decision

We also decided to try Mistral AI as an alternative option since  they can achieve high performance with fewer parameters compared to models like GPT-4. This results in faster inference times and lower computational costs.

## Consequences

What becomes easier or more difficult to do and any risks introduced by the change that will need to be mitigated.

We could minimize costs while still leveraging powerful language models. It is Perfect for applications that require complete data control and compliance with privacy regulations. Also it is flexible and customizable LLM solution that can be adapted for specific use cases.


Comparison Mistral AI LLM with OpenAI GPT LLM Models


Features	                              Mistral AI LLM	                     OpenAI GPT LLM

License	                             Open-source (free)	                    Proprietary (paid)
Cost	                             No usage fees	                        Pay-per-use API
Model Efficiency	                 High performance, fewer parameters	    High performance, large model size
Customization	                     Full control, easy fine-tuning	        Limited customization without API access
Deployment Flexibility          	 On-premise and cloud-compatible	    Cloud-based with API integration