# 🤖 Jarvis AI Assistant

A Python-based voice assistant inspired by Iron Man's Jarvis — upgraded to an industry-grade AI system with face authentication, persistent memory, activity logging, user personalization, and a modular plugin architecture.

---

## ⚡ What's New in v2.0

| Feature | Description |
|---|---|
| 🔐 Face Authentication | ArcFace pretrained model via DeepFace |
| 🧠 Conversation Memory | Multi-turn context using Gemini Chat API |
| 💾 Persistent Memory | Conversations saved across sessions via JSON |
| 📋 Activity Logger | Every action timestamped to logs/jarvis.log |
| 👤 User Profile | Personalized responses based on profile.json |
| 🔌 Plugin Architecture | Modular skill system — easily extensible |

---

## 🔐 Security — Face Authentication

Jarvis verifies your identity before starting using the **ArcFace** pretrained model via DeepFace.

- Webcam-based identity verification on every startup
- Face image stored locally inside `faces/` folder
- Unauthorized users are denied access and Jarvis shuts down
- Runs fully offline — no face data sent anywhere

---

## 🧠 AI Brain — Gemini 2.5 Flash

Powered by **Google Gemini 2.5 Flash** with full conversation memory.

- Multi-turn memory — Jarvis remembers context across the conversation
- Persistent memory — remembers across sessions even after restart
- Personalized system prompt built from your user profile
- Fallback for all unknown commands

---

## ✨ Features

### 🗣️ Voice Interaction
- Wake word detection — say **"Jarvis"** to activate
- Speech-to-text via `speech_recognition` (Google STT)
- Text-to-speech via `pyttsx3`

### 🎵 Music Player
- Say **"play [song name]"** to play directly on YouTube
- No manual music library needed

### 📰 Live News
- Fetches top 3 headlines using NewsAPI
- Country configured via `profile.json`

### 💻 System Automation
- Open Calculator
- Open Notepad
- Take Screenshots
- Tell Current Time

### 🌐 Web Browsing
- Open Google, YouTube, LinkedIn via voice

### 🧩 Plugin Architecture
- Every command is a separate skill file
- Add new skills without touching core logic
- Inspired by Amazon Alexa Skills architecture

---

## 🛠️ Tech Stack

**Language:** Python 3.x

### Core Libraries
- `speech_recognition` — Voice input
- `pyttsx3` — Text to speech
- `deepface` — Face recognition (ArcFace)
- `opencv-python` — Webcam access
- `google-generativeai` — Gemini AI
- `pywhatkit` — YouTube automation
- `pyautogui` — Screenshots
- `requests` — API calls
- `python-dotenv` — Environment variables

### AI Models
- **ArcFace** via DeepFace — Face authentication
- **Gemini 2.5 Flash** — Conversational AI brain

---

## 📂 Project Structure

```
Jarvis/
│
├── skills/
│   ├── __init__.py
│   ├── web_skill.py
│   ├── music_skill.py
│   ├── news_skill.py
│   ├── system_skill.py
│   └── memory_skill.py
│
├── memory/
│   └── conversation_log.json
│
├── logs/
│   └── jarvis.log
│
├── faces/
│   └── authorized.jpg
│
├── main.py
├── client.py
├── face_auth.py
├── logger.py
├── profile.py
├── profile.json
├── requirements.txt
├── .env
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository
```bash
git clone https://github.com/Vishwa-Sone/Jarvis.git
cd Jarvis
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Requirements
```bash
pip install -r requirements.txt
```

### 4️⃣ Add API Keys
Create a `.env` file in the project root:
```
GEMINI_API_KEY=your_gemini_api_key
NEWS_API_KEY=your_newsapi_key
```

### 5️⃣ Update Your Profile
Edit `profile.json` with your details:
```json
{
  "name": "Your Name",
  "city": "Your City",
  "interests": []
}
```

### 6️⃣ Register Your Face (First Time Only)
```bash
python face_auth.py --register
```
- Webcam opens → align face in the green box → press **SPACE**

### 7️⃣ Run Jarvis
```bash
python main.py
```

---

## 🗣️ Voice Commands

| Say This | Action |
|---|---|
| "Jarvis, open google" | Opens Google |
| "Jarvis, open youtube" | Opens YouTube |
| "Jarvis, open linkedin" | Opens LinkedIn |
| "Jarvis, play [song]" | Plays song on YouTube |
| "Jarvis, news" | Reads top 3 headlines |
| "Jarvis, time" | Tells current time |
| "Jarvis, screenshot" | Takes a screenshot |
| "Jarvis, open calculator" | Opens Calculator |
| "Jarvis, open notepad" | Opens Notepad |
| "Jarvis, clear memory" | Resets conversation memory |
| "Jarvis, who am I" | Reads your profile |
| "Jarvis, [anything else]" | Answered by Gemini AI |

---

## 🔌 Adding a New Skill

Create `skills/weather_skill.py`:
```python
KEYWORDS = ["weather", "temperature"]

def execute(command, speak, profile):
    speak("It is 28 degrees in Dharwad Sir")
    return True
```

Add it to `main.py`:
```python
from skills import weather_skill
SKILLS = [..., weather_skill]
```

That's it — no other file needs to change.

---

## 📋 Activity Log Sample

```
2026-03-22 21:30:01 | INFO     | Jarvis is starting up...
2026-03-22 21:30:04 | INFO     | Profile loaded for user: Vishwa
2026-03-22 21:30:06 | INFO     | Face authentication: SUCCESS
2026-03-22 21:30:10 | INFO     | Command received: who is virat kohli
2026-03-22 21:30:11 | INFO     | Gemini response: He is an Indian cricketer...
```

---

## ⚠️ Notes

- Windows only for Calculator and Notepad (`os.startfile`)
- Internet required for Gemini AI, NewsAPI, and YouTube
- ArcFace model (~500MB) downloads automatically on first run
- All face data and memory stored **locally only**