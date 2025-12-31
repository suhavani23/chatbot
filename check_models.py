import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("GEMINI_API_KEY")

print(f"API Key found: {api_key[:10]}...")

try:
    # Configure
    genai.configure(api_key=api_key)
    
    # List available models
    print("\nAvailable models for your API key:")
    print("-" * 50)
    
    for model in genai.list_models():
        if 'generateContent' in model.supported_generation_methods:
            print(f"[OK] {model.name}")
            print(f"  Display name: {model.display_name}")
            if model.description:
                desc = model.description[:80] if len(model.description) > 80 else model.description
                print(f"  Description: {desc}")
            print()
    
except Exception as e:
    print(f"\nError: {e}")
