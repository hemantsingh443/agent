import requests  
from dotenv import load_dotenv
import os 

load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY") 

OPENROUTER_API_BASE = "https://openrouter.ai/api/v1/chat/completions"
MODEL = "xiaomi/mimo-v2-flash:free" 

def call_llm(messages: list[dict]) -> str: 
    headers = { 
        "Authorization": f"Bearer {OPENROUTER_API_KEY}", 
        "Content-Type": "application/json",  
        "HTTP-Referer": "https://github.com/",
        "X-Title": "GitHub"
    } 
    payload = { 
        "model": MODEL, 
        "messages": messages,  
    } 
    response = requests.post(OPENROUTER_API_BASE, headers=headers, json=payload) 
    response.raise_for_status()  

    return response.json()["choices"][0]["message"]["content"]

