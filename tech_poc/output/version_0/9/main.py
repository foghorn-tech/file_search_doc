import streamlit as st
from openai import OpenAI
import os
from pathlib import Path

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Streamlit app
st.title("AI Image and Speech Generator")

# Text input for image generation
image_prompt = st.text_input("Enter text to generate an image:")

if st.button("Generate Image"):
    if image_prompt:
        # Generate image from text
        image_response = client.images.generate(
            model="dall-e-3",
            prompt=image_prompt,
            n=1,
            size="1024x1024",
            response_format="url"
        )
        image_url = image_response.data[0].url
        st.image(image_url, caption="Generated Image")

# Text input for speech generation
speech_text = st.text_input("Enter text to generate speech:")

if st.button("Generate Speech"):
    if speech_text:
        # Generate speech from text
        speech_file_path = Path("speech.mp3")
        speech_response = client.audio.speech.create(
            model="tts-1",
            voice="alloy",
            input=speech_text
        )
        speech_response.stream_to_file(speech_file_path)
        audio_file = open(speech_file_path, 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/mp3')