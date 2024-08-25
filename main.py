import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests

# Initialize the recognizer and the TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = """use your own api key"""

def speak(text):
    """Function to convert text to speech"""
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            # Extract the articles
            articles = data.get('articles', [])
            # Print and speak the headlines
            for article in articles:
                title = article.get('title', 'No title')
                print(title)
                speak(title)
        else:
            print("Failed to fetch news")
    
    else:
        # Let OpenAi handle the request
        pass

if __name__ == "__main__":
    speak("Initializing jarvis...")
    while True:
        # Listen for the wake word "jarvis"
        print("Listening...")
        try:
            with sr.Microphone() as source:
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=3)
                print("Recognizing...")
                command = recognizer.recognize_google(audio)
                print(f"You said: {command}")
                
                if "jarvis" in command.lower():
                    speak("yaa")
                    
                    # Listen for the actual command after the wake word
                    with sr.Microphone() as source:
                        audio = recognizer.listen(source, timeout=3, phrase_time_limit=3)
                        command = recognizer.recognize_google(audio)
                        print(f"You said: {command}")
                        
                        processCommand(command)
        
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        except Exception as e:
            print(f"An error occurred: {e}")