import streamlit as st
from openai import OpenAI
import os
import requests
from pathlib import Path

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Function to generate image from text
def generate_image(prompt):
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        response_format="url",
        n=1
    )
    return response.data[0].url

# Function to generate speech from text
def generate_speech(text):
    speech_file_path = Path("speech.mp3")
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=text
    )
    response.stream_to_file(speech_file_path)
    return speech_file_path

# Streamlit app
st.title("AI Image and Speech Generator")

# Text input
user_input = st.text_input("Enter text to generate image and speech:")

if st.button("Generate"):
    if user_input:
        # Generate image
        image_url = generate_image(user_input)
        st.image(image_url, caption="Generated Image")

        # Generate speech
        speech_path = generate_speech(user_input)
        audio_file = open(speech_path, "rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mp3")
    else:
        st.error("Please enter some text to generate image and speech.")