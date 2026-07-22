import os
from pathlib import Path
from time import sleep
from dotenv import load_dotenv
from groq import Groq
import re

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("GROQ_API_KEY not found.")

client = Groq(api_key=my_api_key)
model = "llama-3.3-70b-versatile"

def get_product_price(product):
    if product == 'iPhone 17':
        return 1000
    elif product == 'iPhone 15':
        return 500
    else:
        return 0

def calculator(expression):
    try:
        return eval(expression)
    except:
        return "calculation error"

tool = {
    "get_product_price": get_product_price,
    "calculator": calculator
}