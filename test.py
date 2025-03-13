from murf import Murf

client = Murf(
    api_key=""
)

res = client.text_to_speech.generate(
    text="There is much to be said",
    voice_id="en-US-miles",
)

print(res.audio_file)

