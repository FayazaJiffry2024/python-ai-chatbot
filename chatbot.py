# Load environment variables
from dotenv import load_dotenv
import os
import requests

# Load .env file
load_dotenv()

# Free alternative using Ollama (local, no API key needed)
def get_ollama_response(prompt):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3.2:1b",  # Smaller, faster model
                "prompt": prompt,
                "stream": False,
                "options": {
                    "num_predict": 200  # Limit response length
                }
            }
        )
        return response.json()["response"]
    except:
        return "Error: Make sure Ollama is installed and running. Download from https://ollama.ai"

print("🤖 AI Chat Started (type 'exit' to stop)\n")

# Infinite chat loop
while True:
    user_input = input("👤 You: ")

    if user_input.lower() == "exit":
        print("👋 Goodbye!")
        break

    # Send message to AI (free local model)
    ai_response = get_ollama_response(user_input)
    
    # Print AI reply with better formatting
    print("\n🤖 AI:", ai_response)
    print("-" * 50)  # Separator line