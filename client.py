import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv(override=True)

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("CRITICAL ERROR: Gemini API key not found! Check your .env file.")
else:
    genai.configure(api_key=api_key)
    
model = genai.GenerativeModel('gemini-2.5-flash')

def aiProcess(command):
    """Sends command to Gemini and returns the text response."""
    try:
        if not api_key:
            return "Sir, my API key is missing. Please check the dot env file."
            
        prompt = f"You are Jarvis, a helpful virtual assistant. Keep your response very short and concise. User says: {command}"
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Gemini Error: {e}")
        return "Sir, I am having trouble reaching my Gemini servers."