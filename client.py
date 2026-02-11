import os
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()

# Fetch the key from the environment
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def aiProcess(command):
    """Sends command to OpenAI and returns the text response."""
    try:
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are Jarvis, a helpful virtual assistant. Keep answers short and concise."},
                {"role": "user", "content": command}
            ]
        )
        return completion.choices[0].message.content
    except Exception as e:
        print(f"OpenAI Error: {e}")
        return "I am having trouble connecting to my AI brain."