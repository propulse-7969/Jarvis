import sys
import speech_recognition as sr
import webbrowser
import pyttsx3
import creds
import musiclib
import requests
import random
from google import genai
from google.genai import types
from murf import Murf
import pygame
import io

GEMINI_API_KEY = f"{creds.GEMINI_API_KEY}"

API_KEY_NEWS=f"{creds.API_KEY_NEWS}"

sys_instruct='''You are an advanced humanoid AI way, competing Alexa and Siri, 
you are JARVIS as in the Marvel Cinematic Universe. Answer to my commands in a humane way and also apt and to the point.'''
client = genai.Client(api_key=f"{GEMINI_API_KEY}")
mur_client = Murf(
    api_key=f"{creds.MURF_KEY}" # Not required if you have set the MURF_API_KEY environment variable
)

r = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def better_speak(text):
    res = mur_client.text_to_speech.generate(
        text=text,
        voice_id="en-US-ryan",
    )
    # URL of the audio file
    audio_url = res.audio_file

    # Download the audio file
    response = requests.get(audio_url)
    if response.status_code == 200:
        audio_data = io.BytesIO(response.content)

        pygame.mixer.init()
        pygame.mixer.music.load(audio_data)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():  # Keep playing
            continue
    else:
        print("Failed to download audio.")



def speak(text):
    """ Converts text to speech """
    engine.say(text)
    engine.runAndWait()


def processCommand(command):
    """ Processes the voice command and performs actions """
    command = command.lower()

    if "open google" in command:
        print("Opening Google")
        webbrowser.open("https://google.com")

    elif "open youtube" in command:
        print("Opening YouTube")
        webbrowser.open("https://youtube.com")

    elif "open instagram" in command:
        print("Opening Instagram")
        webbrowser.open("https://instagram.com")

    elif "open facebook" in command:
        print("Opening Facebook")
        webbrowser.open("https://facebook.com")

    elif command.lower().startswith("play"):
        song = command.lower().split(" ")[1]
        link=musiclib.music[song]
        print("Playing {}".format(song))
        webbrowser.open(link)

    elif "news" in command:
        req = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY_NEWS}")
        if req.status_code == 200:
            data = req.json()
            articles = data.get('articles', [])
            article = random.choice(articles)
            better_speak(article['title'])
    else:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            config=types.GenerateContentConfig(system_instruction=sys_instruct, temperature=2, max_output_tokens=35),
            contents=[command]
        )
        better_speak(response.text.replace("*", ""))


def activated():
    """ Listens for a command after the wake word is detected """
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        try:
            audio = r.listen(source)
            command = r.recognize_google(audio)
            print(f"You said: {command}")
            processCommand(command)
        except sr.UnknownValueError:
            better_speak("Sorry, I didn't catch that. Please repeat.")
        except sr.RequestError:
            better_speak("Network error. Please check your internet connection.")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    better_speak("Initializing Jarvis")
    while True:
        print("Listening for wake word...")
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
                feed = r.recognize_google(audio).lower()

                if "jarvis" in feed:
                    better_speak("At Your Service")
                    activated()
                if "terminate" in feed:
                    sys.exit()
        except sr.UnknownValueError:
            pass  # Ignore unrecognized audio
        except sr.RequestError:
            better_speak("Network issue detected.")
        except Exception as e:
            print(f"Error: {e}")