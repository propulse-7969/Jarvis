JARVIS AI Voice Assistant

Overview

This project is an advanced AI voice assistant modeled after J.A.R.V.I.S. from the Marvel Cinematic Universe. It competes with mainstream assistants like Alexa and Siri, providing voice-based interactions, web automation, and news retrieval.

Features

Voice Commands: Recognizes and processes spoken commands.

Web Navigation: Opens Google, YouTube, Instagram, and Facebook via voice commands.

Music Playback: Plays music from a predefined library.

News Updates: Fetches and reads out top headlines.

AI Responses: Uses Google's Gemini AI to generate intelligent responses.

Text-to-Speech: Uses Murf AI and pyttsx3 for voice synthesis.

APIs Used

Google Gemini AI: Generates contextual responses to user queries.

Murf AI: Converts text into realistic speech.

Google Speech Recognition: Captures and interprets voice input.

NewsAPI.org: Fetches real-time news headlines.

Setup

Install dependencies:

pip install speechrecognition webbrowser pyttsx3 requests pygame google-generativeai murf

Configure API keys in creds.py:

GEMINI_API_KEY = "your_gemini_api_key"
API_KEY_NEWS = "your_news_api_key"
MURF_KEY = "your_murf_api_key"

Run the assistant:

python jarvis.py

Usage

Say "Jarvis" to activate the assistant.

Use voice commands such as:

"Open Google"

"Play [song name]"

"News update"

"Terminate" (to exit the program)

Notes

Ensure a stable internet connection for API-based functionality.

Background noise may affect voice recognition accuracy.

License

This project is open-source. Feel free to modify and enhance its capabilities!

