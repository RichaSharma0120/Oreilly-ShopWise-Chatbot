# 3. AI Agent

Date: 2024-11-14

## Status

Accepted

## Context

Making decisions for thousands of user queries in a day is very cumbersome, so ai agents are designed to make decisions and take actions to achieve a specific goal or set of goals. The agent operates autonomously, therefore it is not directly controlled by a human. 

## Decision

 Decided with (create_csv_agent) pandas dataframe agent, which is most appropriate to analyze simple csv files where in it seamlessly interacts with CSV files using natural language. while comparing to other ai agents like Pandas AI, LangChain's pandas_data_agent.

## Consequences

After using create_csv_agent, it automatically parses the CSV file and analyzes its structure, columns, and data types which makes easier to derive insights, run calculations, or summarize the data. There is easiness for non technical persons also. Moreover, it supports direct CSV files directly and no dataframe conversions are required and setup complexity is minimal.

Below is comparison table for agents made during decision making.

Feature	                    	create_csv_agent	Pandas AI	LangChain's pandas_data_agent

Ease of Use	                        ⭐⭐⭐⭐⭐	  ⭐⭐⭐	        ⭐⭐⭐
Data Preprocessing	                 Limited	      Extensive	        Extensive
Direct CSV File Support	              Yes	          No 	            No
Advanced Data Analysis	              Basic	          Advanced	        Advanced
Integration with Pandas	              No	          Yes	            Yes
Ideal for Non-Technical Users	      Yes	          No	            No
Setup Complexity	                  Minimal	      Moderate	        Moderate



| Feature | create_csv_agent | Pandas AI | LangChain's pandas_data_agent |

|---|---|---|---|

| Ease of Use | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |

| Data Preprocessing | Limited | Extensive | Extensive |

| Direct CSV File Support | Yes | No | No |

| Advanced Data Analysis | Basic | Advanced | Advanced |

| Integration with Pandas | No | Yes | Yes |

| Ideal for Non-Technical Users | Yes | No | No |

| Setup Complexity | Minimal | Moderate | Moderate |
