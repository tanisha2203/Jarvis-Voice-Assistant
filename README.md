# 🤖 Jarvis - Voice Assistant in Python

A voice-controlled AI assistant built using Python. Jarvis listens for your voice, performs tasks like opening websites, playing music, reading news, and answering questions via AI — all hands-free!

---

## 🚀 Features

- 🎤 Voice activation with "Jarvis"
- 🌐 Opens Google, YouTube, LinkedIn, Facebook
- 📰 Speaks latest headlines using NewsAPI
- 🎵 Plays custom YouTube songs via keyword
- 🧠 Responds to user queries using Cohere AI
- 💬 Text-to-speech replies using pyttsx3

---

## 🛠️ Tech Stack

- Python 3.x
- `speech_recognition`
- `pyttsx3`
- `cohere`
- `requests`
- `python-dotenv`
- `webbrowser`

---

## 📁 Folder Structure

```bash
Jarvis-Voice-Assistant/
├── main.py              # Core logic (voice, AI, commands)
├── musicLibrary.py      # Custom music keyword-to-link map
├── .env                 # API keys (not uploaded to GitHub)
├── .gitignore           # Ignore rules
├── requirements.txt     # Python dependencies
└── README.md            # This file
