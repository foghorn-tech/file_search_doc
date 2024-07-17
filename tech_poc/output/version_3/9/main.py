import streamlit as st
import openai
import os
import requests
from gtts import gTTS
from io import BytesIO
from PIL import Image

# Initialize OpenAI client
openai.api_key = os.getenv("OPENAI_API_KEY", "<your OpenAI API key>")

# Streamlit app
st.title("AI Image and Speech Generator")
st.write("Enter text to generate an image and speech using OpenAI's DALL-E and a TTS service.")

# Text input
user_text = st.text_input("Enter text:")

if st.button("Generate"):
    if user_text:
        # Generate image from text using OpenAI DALL-E
        response = openai.Image.create(
            prompt=user_text,
            n=1,
            size="1024x1024"
        )
        image_url = response['data'][0]['url']
        
        # Download and display the generated image
        image_data = requests.get(image_url).content
        image = Image.open(BytesIO(image_data))
        st.image(image, caption='Generated Image', use_column_width=True)
        
        # Generate speech from text using gTTS
        tts = gTTS(text=user_text, lang='en')
        tts_audio = BytesIO()
        tts.save(tts_audio)
        tts_audio.seek(0)
        
        # Provide a link to download the generated speech
        st.audio(tts_audio, format='audio/mp3')
        st.download_button(label="Download Speech", data=tts_audio, file_name="output.mp3", mime="audio/mp3")
    else:
        st.error("Please enter some text to generate an image and speech.")