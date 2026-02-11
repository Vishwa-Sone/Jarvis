# 🤖 Jarvis AI Assistant

A Python-based virtual assistant inspired by Iron Man's Jarvis. This application uses speech recognition and text-to-speech engines to execute voice commands, control system applications, play music, and answer general queries using OpenAI's GPT models.

## ✨ Features

- **🗣️ Voice Interaction:**
  - Wake word detection ("Jarvis").
  - Realistic text-to-speech response using `pyttsx3`.
- **🧠 AI "Brain":**
  - Integrated with **OpenAI API (GPT-3.5)** to answer general questions (e.g., "Who is Elon Musk?", "Write a poem").
- **🎵 Dynamic Music Player:**
  - Automatically searches and plays songs directly from **YouTube** (no manual library needed).
- **📰 Live News:**
  - Fetches top headlines using **NewsAPI**.
- **💻 System Automation:**
  - Opens desktop applications (Calculator, Notepad).
  - Takes screenshots.
  - Tells the current time.
- **🌐 Web Browsing:**
  - Opens websites like Google, YouTube, and LinkedIn via voice command.

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **Libraries:**
  - `speech_recognition` (Speech-to-Text)
  - `pyttsx3` (Text-to-Speech)
  - `openai` (AI Chat)
  - `pywhatkit` (YouTube automation)
  - `pyautogui` (Screenshots & System control)
  - `requests` (API calls)
