import os
import json
from spitch import Spitch

# Load API Key
with open("config.json", "r") as file:
    config = json.load(file)
    api_key = config["API_KEY"]

os.environ["SPITCH_API_KEY"] = api_key
client = Spitch()

# file should be a .wav or .mp3
def speech_to_text(file, src, target):
    with open(file, 'rb') as f:
        response = client.speech.transcribe(
            language=src,
            content=f.read(),
        )
    
    print(f'What was said: {response.text}')

    translation = client.text.translate(
        text=response.text,
        source=src,
        target=target
    )

    print(f'Translation: {translation.text}')
    return translation.text
    
# English voices: 'john', 'lucy', 'lina', 'jude'
def text_to_speech(text, language, voice, output_file):
    with open(output_file, 'wb') as f:
        response = client.speech.generate(
            text=text,
            language=language,
            voice=voice,
        )
        f.write(response.read())

text_to_speech("How many eggs can you get by tonight?", 'en', 'lucy', 'new_audio.wav')
