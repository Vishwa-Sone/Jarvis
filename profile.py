
import os
import json
from logger import logger

PROFILE_FILE = "profile.json"


DEFAULT_PROFILE = {
    "name": "Sir",
    "greeting": "Welcome back, Sir",
    "city": "India",
    "interests": [],
    "wake_word": "jarvis",
    "news_country": "in",
    "assistant_name": "Jarvis"
}


def load_profile():
    """
    Loads profile.json from disk.
    If file doesn't exist, creates one with default values.
    """
    if not os.path.exists(PROFILE_FILE):
        logger.warning("profile.json not found. Creating default profile.")
        save_profile(DEFAULT_PROFILE)
        return DEFAULT_PROFILE

    try:
        with open(PROFILE_FILE, "r") as f:
            profile = json.load(f)
        logger.info(f"Profile loaded for user: {profile.get('name', 'Unknown')}")
        return profile

    except Exception as e:
        logger.error(f"Could not load profile: {e}")
        return DEFAULT_PROFILE


def save_profile(profile):
    """
    Saves profile data to profile.json.
    """
    try:
        with open(PROFILE_FILE, "w") as f:
            json.dump(profile, f, indent=2)
        logger.info("Profile saved successfully.")
    except Exception as e:
        logger.error(f"Could not save profile: {e}")


def get_system_prompt(profile):
    """
    Builds a personalized system prompt for Gemini
    using the user's profile data.

    This is the KEY function — it makes Gemini aware
    of WHO it's talking to.
    """
    name = profile.get("name", "Sir")
    city = profile.get("city", "India")
    interests = profile.get("interests", [])
    assistant_name = profile.get("assistant_name", "Jarvis")

    # Build interests string naturally
    if interests:
        interests_str = ", ".join(interests)
    else:
        interests_str = "not specified"

    prompt = (
        f"You are {assistant_name}, a smart and helpful voice assistant inspired by Iron Man. "
        f"You are talking to {name}, who lives in {city}. "
        f"{name}'s interests include: {interests_str}. "
        f"Keep all responses short, clear, and conversational — suitable for text-to-speech. "
        f"Never use markdown, bullet points, or symbols in your responses. "
        f"Address the user as 'Sir' when appropriate. "
        f"When relevant, personalize your responses based on {name}'s interests and location."
    )

    return prompt



profile = load_profile()