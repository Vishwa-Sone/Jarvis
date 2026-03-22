
import os
import datetime
import pyautogui
from logger import logger

# Keywords that trigger this skill
KEYWORDS = ["time", "screenshot", "open calculator", "open notepad"]


def execute(command, speak, profile):
    """
    Handles system-level commands.
    """
    if "time" in command:
        strTime = datetime.datetime.now().strftime("%H:%M")
        speak(f"Sir, the time is {strTime}")
        logger.info(f"Told time: {strTime}")
        return True

    elif "screenshot" in command:
        speak("Taking screenshot Sir")
        pyautogui.screenshot("jarvis_screenshot.png")
        speak("Screenshot saved")
        logger.info("Screenshot taken.")
        return True

    elif "open calculator" in command:
        speak("Opening Calculator")
        os.startfile("calc.exe")
        logger.info("Opened Calculator.")
        return True

    elif "open notepad" in command:
        speak("Opening Notepad")
        os.startfile("notepad.exe")
        logger.info("Opened Notepad.")
        return True

    return False