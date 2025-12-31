import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("GEMINI_API_KEY")

print(f"API Key found: {api_key[:10]}..." if api_key else "No API key found")

try:
    # Configure and test
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.0-flash-exp')
    
    # Test with a simple prompt
    response = model.generate_content("Say 'API key is working!'")
    print(f"\n✅ SUCCESS: {response.text}")
    
except Exception as e:
    print(f"\n❌ ERROR: {str(e)}")
    print(f"\nError type: {type(e).__name__}")
