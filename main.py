import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import cohere
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Fetch API keys securely from environment
NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")
COHERE_API_KEY = os.getenv("COHERE_API_KEY")

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiProcess(command):
    co = cohere.Client(COHERE_API_KEY)

    response = co.chat(
        message=command,
        chat_history=[
            {"role": "system", "message": "You are a helpful assistant like Alexa. Give short and clear answers."}
        ]
    )
    return response.text.strip()

def processCommand(c):
    c = c.lower()

    if "open google" in c:
        webbrowser.open("https://google.com")
        speak("Opening Google.")

    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")
        speak("Opening Facebook.")

    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube.")

    elif "open linkedin" in c:
        webbrowser.open("https://linkedin.com")
        speak("Opening LinkedIn.")

    elif c.startswith("play"):
        song = c.replace("play", "", 1).strip().lower()
        matched_song = None

        for key in musicLibrary.music:
            if key in song or song in key:
                matched_song = key
                break

        if matched_song:
            link = musicLibrary.music[matched_song]
            webbrowser.open(link)
            speak(f"Playing {matched_song}.")
        else:
            speak("Sorry, I couldn't find that song.")

    elif "news" in c:
        try:
            r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWSAPI_KEY}")
            if r.status_code == 200:
                data = r.json()
                articles = data.get('articles', [])
                speak("Here are the top 3 headlines.")
                for article in articles[:3]:
                    speak(article['title'])
            else:
                speak("Sorry, I couldn't fetch the news.")
        except Exception as e:
            speak("There was an error fetching the news.")
            print(e)

    elif "exit" in c or "stop" in c or "bye" in c:
        speak("Goodbye!")
        exit()

    else:
        output = aiProcess(c)
        speak(output)

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        try:
            print("Recognizing wake word...")
            with sr.Microphone() as source:
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=4)
            word = recognizer.recognize_google(audio)
            if word.lower() == "jarvis":
                speak("Yes?")
                with sr.Microphone() as source:
                    print("Listening for command...")
                    audio = recognizer.listen(source, timeout=5)
                    command = recognizer.recognize_google(audio)
                    print(f"Command: {command}")
                    processCommand(command)

        except sr.WaitTimeoutError:
            print("Listening timed out...")
        except sr.UnknownValueError:
            print("Could not understand audio.")
        except Exception as e:
            print(f"Error: {e}")
