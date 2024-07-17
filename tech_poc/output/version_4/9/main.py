import streamlit as st
import openai
import os
from pathlib import Path

# Set up OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Streamlit app
st.title("AI Image and Speech Generator")
st.write("Enter text to generate an image and speech using OpenAI's DALL-E and text-to-speech API.")

# Text input
user_input = st.text_input("Enter your text:")

if st.button("Generate"):
    if user_input:
        # Generate image using DALL-E
        try:
            image_response = openai.Image.create(
                prompt=user_input,
                n=1,
                size="1024x1024"
            )
            image_url = image_response['data'][0]['url']
            st.image(image_url, caption="Generated Image")
        except Exception as e:
            st.error(f"Error generating image: {e}")

        # Generate speech using OpenAI's text-to-speech API
        try:
            speech_response = openai.Audio.create(
                model="text-to-speech",
                input=user_input,
                voice="alloy"
            )
            speech_file_path = Path("speech.mp3")
            with open(speech_file_path, "wb") as f:
                f.write(speech_response['data'])
            audio_file = open(speech_file_path, "rb")
            st.audio(audio_file.read(), format="audio/mp3")
        except Exception as e:
            st.error(f"Error generating speech: {e}")
    else:
        st.warning("Please enter some text.")