
import pywhatkit
from logger import logger

# Keywords that trigger this skill
KEYWORDS = ["play"]


def execute(command, speak, profile):
    """
    Plays a song on YouTube using pywhatkit.
    Extracts song name from command after 'play'.
    """
    if command.startswith("play"):
        song = command[4:].strip()

        if not song:
            speak("What song would you like me to play, Sir?")
            return True

        speak(f"Playing {song} on YouTube")
        logger.info(f"Playing song: {song}")
        pywhatkit.playonyt(song)
        return True

    return False