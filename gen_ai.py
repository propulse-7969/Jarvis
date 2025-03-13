from google import genai
from google.genai import types

GEMINI_API_KEY = "AIzaSyBIOGYDY9jYGHqd0mE6PZyf1SCPgNC5Iqw"

sys_instruct="You are an advanced humanoid AI way, competing Alexa and Siri, you are like Jarvis and your name is STELLA. Answer to my commands in a humane way and also apt and to the point."
client = genai.Client(api_key=f"{GEMINI_API_KEY}")

response = client.models.generate_content(
    model="gemini-2.0-flash",
    config=types.GenerateContentConfig(system_instruction=sys_instruct, temperature=2, max_output_tokens=35),
    contents=["hello how are you?"]
)
print(response.text.replace("*",""))

