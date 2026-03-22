
import client
from logger import logger

# Keywords that trigger this skill
KEYWORDS = ["clear memory", "forget everything", "my profile", "who am i"]


def execute(command, speak, profile):
    """
    Handles memory management and profile read commands.
    """
    if "clear memory" in command or "forget everything" in command:
        client.clear_memory()
        speak("Memory cleared Sir, starting fresh.")
        return True

    elif "my profile" in command or "who am i" in command:
        name      = profile.get("name", "Unknown")
        city      = profile.get("city", "Unknown")
        interests = ", ".join(profile.get("interests", []))
        speak(
            f"Your name is {name}, you live in {city}, "
            f"and your interests are {interests}."
        )
        logger.info("Profile read to user.")
        return True

    return False