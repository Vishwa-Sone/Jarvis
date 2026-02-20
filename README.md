# 🤖 Jarvis AI Assistant

A Python-based virtual assistant inspired by Iron Man's Jarvis.

Now upgraded with:

- 🔐 Face Authentication (DeepFace + ArcFace)
- 🧠 Gemini 2.5 Flash AI Brain
- 🎤 Voice-Controlled Commands
- 💻 System Automation

---

## 🔐 Security Feature – Face Authentication

Jarvis includes secure face recognition before startup.

- Uses DeepFace with ArcFace model
- Webcam-based identity verification
- Face stored locally inside `faces/` folder
- Prevents unauthorized access

⚠️ Face data is NOT uploaded anywhere.

---

## ✨ Features

### 🗣️ Voice Interaction
- Wake word detection ("Jarvis")
- Speech-to-text using `speech_recognition`
- Text-to-speech using `pyttsx3`

---

### 🧠 AI Brain – Gemini 2.5 Flash

Integrated with **Google Gemini 2.5 Flash** model using the `google-generativeai` SDK.

Capabilities:
- Answer general knowledge questions
- Generate poems & creative content
- Explain technical concepts
- Assist with coding questions

---

### 🎵 Dynamic Music Player
- Automatically searches and plays songs on YouTube
- No manual music library required

---

### 📰 Live News
- Fetches top headlines using NewsAPI

---

### 💻 System Automation
- Open Calculator
- Open Notepad
- Take Screenshots
- Tell Current Time

---

### 🌐 Web Browsing
- Open Google
- Open YouTube
- Open LinkedIn

All controlled via voice.

---

## 🛠️ Tech Stack

**Language:** Python 3.x

### Core Libraries:
- speech_recognition
- pyttsx3
- deepface
- opencv-python
- google-generativeai
- pywhatkit
- pyautogui
- requests
- python-dotenv

### AI Model:
- Gemini 2.5 Flash (Google Generative AI)

---

## 📂 Project Structure
Jarvis/
│
├── faces/
│ └── authorized.jpg
│
├── face_auth.py
├── main.py
├── client.py
├── requirements.txt
├── .env
└── README.md



---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Vishwa-Sone/Jarvis.git
cd Jarvis

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate

3️⃣ Install Requirements
pip install -r requirements.txt

4️⃣ Add API Keys
Create a .env file:
NEWS_API_KEY=your_news_api_key
GOOGLE_API_KEY=your_gemini_api_key

5️⃣ Register Face (First Time Only)
python face_auth.py --register

6️⃣ Run Jarvis
python main.py