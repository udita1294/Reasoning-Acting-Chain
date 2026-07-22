# ReAct AI Agent with Groq

A simple implementation of the **ReAct (Reasoning + Acting)** framework using the **Groq API**. The agent reasons through a problem step by step, decides when to use external tools, executes one tool at a time, observes the result, and continues reasoning until it reaches a final answer.

## Features

* ReAct (Reasoning + Acting) workflow
* Powered by the Groq LLM API
* Supports iterative reasoning with multiple steps
* Executes one tool call at a time
* Maintains conversation history between reasoning steps
* Parses tool calls using regular expressions
* Demonstrates how LLMs can interact with external functions

## Project Structure

```text
.
├── reasoning_Acting_chain.py   # Main ReAct agent
├── .env                        # Stores GROQ_API_KEY
└── README.md
```

## How It Works

The agent follows the ReAct pattern:

1. Receives a user query.
2. Thinks about the next action.
3. Calls exactly one tool.
4. Receives the tool's observation.
5. Continues reasoning.
6. Produces the final answer.

Example flow:

```text
User Question
      │
      ▼
LLM Reasoning (Thought)
      │
      ▼
Tool Call (Action)
      │
      ▼
Tool Execution
      │
      ▼
Observation
      │
      ▼
LLM Reasoning
      │
      ▼
Final Answer
```

## Available Tools

### Product Price Tool

Returns the price of supported products.

```python
get_product_price(product)
```

Example:

```text
Action: get_product_price("iPhone 17")
```

### Calculator Tool

Evaluates mathematical expressions.

```python
calculator(expression)
```

Example:

```text
Action: calculator("5000-1000")
```

## Example Query

```text
I have 5000 rupees.
What is the price of iPhone 17?
How much money will I have left after buying it?
```

Example reasoning:

```text
Thought: I need the product price.

Action: get_product_price("iPhone 17")

Observation: 1000

Thought: Now calculate the remaining amount.

Action: calculator("5000-1000")

Observation: 4000

Final Answer:
The iPhone 17 costs 1000 rupees.
You will have 4000 rupees remaining.
```

## Tech Stack

* Python 3.11+
* Groq Python SDK
* Groq LLM (Llama 3.3 70B Versatile)
* python-dotenv
* Regular Expressions (`re`)

## Learning Outcomes

This project demonstrates:

* ReAct prompting
* Agentic AI workflows
* Tool calling
* Multi-step reasoning
* Conversation memory
* Prompt engineering
* LLM integration with Python


This project is intended for educational and learning purposes.
