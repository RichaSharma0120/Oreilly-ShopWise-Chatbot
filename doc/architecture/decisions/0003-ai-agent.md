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

<html lang="en">
<head>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Comparison Table</title>
    <style>
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            font-size: 18px;
            text-align: left;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
        }
        th {
            background-color: #f2f2f2;
            text-align: center;
        }
        tr:nth-child(even) {
            background-color: #f9f9f9;
        }
        tr:hover {
            background-color: #f1f1f1;
        }
        td {
            text-align: left; /* Changed to align text to the left */
        }
    </style>
</head>
<body>
    <h2>Feature Comparison Table</h2>
    <table>
        <thead>
            <tr>
                <th>Feature</th>
                <th>create_csv_agent</th>
                <th>Pandas AI</th>
                <th>LangChain's pandas_data_agent</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Ease of Use</td>
                <td>⭐⭐⭐⭐⭐</td>
                <td>⭐⭐⭐</td>
                <td>⭐⭐⭐</td>
            </tr>
            <tr>
                <td>Data Preprocessing</td>
                <td>Limited</td>
                <td>Extensive</td>
                <td>Extensive</td>
            </tr>
            <tr>
                <td>Direct CSV File Support</td>
                <td>Yes</td>
                <td>No</td>
                <td>No</td>
            </tr>
            <tr>
                <td>Advanced Data Analysis</td>
                <td>Basic</td>
                <td>Advanced</td>
                <td>Advanced</td>
            </tr>
            <tr>
                <td>Integration with Pandas</td>
                <td>No</td>
                <td>Yes</td>
                <td>Yes</td>
            </tr>
            <tr>
                <td>Ideal for Non-Technical Users</td>
                <td>Yes</td>
                <td>No</td>
                <td>No</td>
            </tr>
            <tr>
                <td>Setup Complexity</td>
                <td>Minimal</td>
                <td>Moderate</td>
                <td>Moderate</td>
            </tr>
        </tbody>
    </table>
</body>
</html>
