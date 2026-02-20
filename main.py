import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
import time 
import os
import datetime
import pyautogui
import pywhatkit
import client  
import face_auth                        # ← NEW: Face authentication module
from dotenv import load_dotenv

load_dotenv()

recognizer = sr.Recognizer()
engine = pyttsx3.init()

newsapi = os.getenv("NEWS_API_KEY")

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 160)
engine.setProperty('volume', 1.0)


def speak(text):
    print(f"Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()


def processCommand(c):
    c = c.lower()

    if "open google" in c:
        webbrowser.open("https://google.com")
        speak("Opening Google")
    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube")
    elif "open linkedin" in c:
        webbrowser.open("https://linkedin.com")
        speak("Opening LinkedIn")
    elif c.startswith("play"):
        song = c[5:].strip()
        speak(f"Playing {song} on YouTube")
        pywhatkit.playonyt(song)
    elif "news" in c:
        try:
            r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
            if r.status_code == 200:
                data = r.json()
                articles = data.get('articles', [])
                speak("Here are the top headlines")
                for article in articles[:3]:
                    title = article.get('title', 'No title')
                    speak(title)
            else:
                speak("I encountered an issue fetching the news")
        except Exception:
            speak("I am unable to connect to the news service")
    elif "open calculator" in c:
        speak("Opening Calculator")
        os.startfile("calc.exe")
    elif "open notepad" in c:
        speak("Opening Notepad")
        os.startfile("notepad.exe")
    elif "time" in c:
        strTime = datetime.datetime.now().strftime("%H:%M")
        speak(f"Sir, the time is {strTime}")
    elif "screenshot" in c:
        speak("Taking screenshot")
        pyautogui.screenshot("jarvis_screenshot.png")
        speak("Screenshot saved")
    else:
        reply = client.aiProcess(c)
        speak(reply)


if __name__ == "__main__":
    speak("Initializing Jarvis...")

    # ─────────────────────────────────────────────
    # FACE AUTHENTICATION — runs before anything else
    # ─────────────────────────────────────────────
    speak("Please look at the camera for identity verification.")
    
    if face_auth.verify_face():
        speak("Identity verified. Welcome back, Vishwa.")
    else:
        speak("Access denied. I don't recognize you. Shutting down.")
        print("[JARVIS] Unauthorized access attempt. Exiting.")
        exit()
    # ─────────────────────────────────────────────

    recognizer.dynamic_energy_threshold = False
    recognizer.energy_threshold = 300

    while True:
        print("Listening for wake word...")
        try:
            with sr.Microphone() as source:
                recognizer.pause_threshold = 0.8
                audio = recognizer.listen(source, timeout=None, phrase_time_limit=5)

            word = recognizer.recognize_google(audio)

            if "jarvis" in word.lower():
                speak("Yes sir")
                
                with sr.Microphone() as source:
                    print("Listening for command...")
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

                command = recognizer.recognize_google(audio)
                print(f"Command: {command}")
                processCommand(command)

        except sr.UnknownValueError:
            pass
        except Exception as e:
            print(f"Error: {e}")
