# 6. Front End Interaction

Date: 2024-11-15

## Status

Accepted

## Context

A First point of contact and bridge between users and the system, directly impacts the overall user experience, engagement, and success of the application. A visually appealing and well-designed interface can attract users and create a positive first impression

## Decision

We decided to implement in Next.JS programming language as it is a excellent choice for building modern, fast, and SEO-friendly React application

## Consequences

Next.js has a large and active community, extensive documentation making it a stable and well-supported choice.


                              

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Main comparisons between Next.JS and Nuxt.JS and Gatsby</title>
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
            text-align: left; /* Align text to the left */
        }
    </style>
</head>
<body>
    <h2>Framework Comparison Table</h2>
    <table>
        <thead>
            <tr>
                <th>Feature</th>
                <th>Next.js</th>
                <th>Nuxt.js</th>
                <th>Gatsby</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Dynamic Routing</td>
                <td>Built-in support</td>
                <td>File-based routing with dynamic segments</td>
                <td>Limited (static routes preferred)</td>
            </tr>
            <tr>
                <td>Scalability</td>
                <td>Highly scalable with support for both SSR and ISR</td>
                <td>File-based routing with dynamic segments</td>
                <td>Not ideal for highly dynamic content</td>
            </tr>
        </tbody>
    </table>
</body>
</html>
