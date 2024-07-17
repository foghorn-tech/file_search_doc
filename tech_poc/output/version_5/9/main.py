import streamlit as st
import openai
import requests
from io import BytesIO
from PIL import Image
import os

# Set up OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Set up TTS API key and endpoint (example using Google Cloud TTS)
TTS_API_KEY = os.getenv("GOOGLE_CLOUD_TTS_API_KEY")
TTS_ENDPOINT = "https://texttospeech.googleapis.com/v1/text:synthesize"

# Function to generate image using OpenAI's DALL-E
def generate_image(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="512x512"
    )
    image_url = response['data'][0]['url']
    return image_url

# Function to generate speech using Google Cloud TTS
def generate_speech(text):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {TTS_API_KEY}"
    }
    data = {
        "input": {"text": text},
        "voice": {"languageCode": "en-US", "ssmlGender": "NEUTRAL"},
        "audioConfig": {"audioEncoding": "MP3"}
    }
    response = requests.post(TTS_ENDPOINT, headers=headers, json=data)
    audio_content = response.json()['audioContent']
    return audio_content

# Streamlit app
st.title("AI Image and Speech Generator")

# Text input for image generation
image_prompt = st.text_input("Enter text to generate an image:")
if st.button("Generate Image"):
    if image_prompt:
        image_url = generate_image(image_prompt)
        image_response = requests.get(image_url)
        img = Image.open(BytesIO(image_response.content))
        st.image(img, caption="Generated Image")

# Text input for speech generation
speech_text = st.text_input("Enter text to generate speech:")
if st.button("Generate Speech"):
    if speech_text:
        audio_content = generate_speech(speech_text)
        audio_bytes = BytesIO(audio_content.encode('latin1'))
        st.audio(audio_bytes, format='audio/mp3')