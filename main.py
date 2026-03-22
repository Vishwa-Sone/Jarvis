

import speech_recognition as sr
import pyttsx3
import client
import face_auth
import profile as user_profile
from logger import logger
from dotenv import load_dotenv

# ── Import all skills ────────────────────────────────────────
from skills import web_skill
from skills import music_skill
from skills import news_skill
from skills import system_skill
from skills import memory_skill
# ─────────────────────────────────────────────────────────────

load_dotenv()

recognizer = sr.Recognizer()
engine     = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 160)
engine.setProperty('volume', 1.0)



SKILLS = [
    web_skill,
    music_skill,
    news_skill,
    system_skill,
    memory_skill,
]



def speak(text):
    print(f"Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()


def processCommand(command):
    """
    Routes command to the correct skill.
    If no skill matches → falls back to Gemini AI.

    This replaces the entire if/elif chain.
    Clean, scalable, and professional.
    """
    c       = command.lower()
    profile = user_profile.profile

    logger.info(f"Processing command: {c}")

    # ── Loop through all skills ──────────────────
    for skill in SKILLS:
        # Check if any of the skill's keywords match
        for keyword in skill.KEYWORDS:
            if keyword in c:
                # Found a match — execute the skill
                handled = skill.execute(c, speak, profile)
                if handled:
                    return   # skill handled it — done!

    # ── No skill matched → send to Gemini AI ────
    logger.info("No skill matched — sending to Gemini.")
    reply = client.aiProcess(c)
    speak(reply)


if __name__ == "__main__":
    logger.info("=" * 50)
    logger.info("Jarvis is starting up...")
    logger.info("=" * 50)

    speak("Initializing Jarvis...")

    # ── Face Authentication ──────────────────────
    speak("Please look at the camera for identity verification.")

    if face_auth.verify_face():
        logger.info("Face authentication: SUCCESS")
        greeting = user_profile.profile.get("greeting", "Welcome back Sir")
        name     = user_profile.profile.get("name", "Sir")
        speak(f"{greeting}, {name}. All systems are online.")
    else:
        logger.warning("Face authentication: FAILED")
        speak("Access denied. Shutting down.")
        exit()

    recognizer.dynamic_energy_threshold = False
    recognizer.energy_threshold         = 400

    logger.info("Jarvis is ready and listening.")

    while True:
        print("Listening for wake word...")
        try:
            with sr.Microphone() as source:
                recognizer.pause_threshold = 0.8
                audio = recognizer.listen(
                    source, timeout=None, phrase_time_limit=5)

            word = recognizer.recognize_google(audio)

            if "jarvis" in word.lower():
                speak("Yes sir")

                with sr.Microphone() as source:
                    print("Listening for command...")
                    audio = recognizer.listen(
                        source, timeout=5, phrase_time_limit=5)

                command = recognizer.recognize_google(audio)
                print(f"Command: {command}")
                processCommand(command)

        except sr.UnknownValueError:
            pass
        except Exception as e:
            logger.error(f"Main loop error: {e}")