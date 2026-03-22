
import os
import json
import google.generativeai as genai
from dotenv import load_dotenv
from logger import logger
import profile as user_profile       

load_dotenv(override=True)

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    logger.critical("Gemini API key not found! Check your .env file.")
else:
    genai.configure(api_key=api_key)
    logger.info("Gemini API configured successfully.")



system_prompt = user_profile.get_system_prompt(user_profile.profile)
logger.info(f"System prompt built for: {user_profile.profile.get('name')}")



model = genai.GenerativeModel(
    model_name='gemini-2.5-flash',
    system_instruction=system_prompt  
)

MEMORY_FOLDER = "memory"
MEMORY_FILE = os.path.join(MEMORY_FOLDER, "conversation_log.json")
MAX_HISTORY = 20


def load_memory():
    if not os.path.exists(MEMORY_FILE):
        logger.info("No previous memory found. Starting fresh.")
        return []
    try:
        with open(MEMORY_FILE, "r") as f:
            data = json.load(f)
        history = data[-MAX_HISTORY:]
        logger.info(f"Loaded {len(history)} messages from memory.")
        return history
    except Exception as e:
        logger.error(f"Could not load memory: {e}")
        return []


def save_memory(history):
    try:
        if not os.path.exists(MEMORY_FOLDER):
            os.makedirs(MEMORY_FOLDER)
        with open(MEMORY_FILE, "w") as f:
            json.dump(history, f, indent=2)
        logger.debug("Memory saved to disk.")
    except Exception as e:
        logger.error(f"Could not save memory: {e}")


conversation_history = load_memory()


def aiProcess(command):
    global conversation_history
    try:
        if not api_key:
            return "my API key is missing. Please check the dot env file."

        logger.info(f"Command received: {command}")

        chat = model.start_chat(history=conversation_history)
        response = chat.send_message(command)
        reply = response.text

        conversation_history.append({"role": "user",  "parts": [command]})
        conversation_history.append({"role": "model", "parts": [reply]})

        save_memory(conversation_history)

        logger.info(f"Gemini response: {reply[:60]}...")

        return reply

    except Exception as e:
        logger.error(f"Gemini Error: {e}")
        return "I am having trouble reaching my Gemini servers."


def clear_memory():
    global conversation_history
    conversation_history = []
    save_memory([])
    logger.info("Memory cleared by user.")