import streamlit as st
from openai import OpenAI
import os

# Initialize OpenAI Client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Streamlit file uploader
uploaded_file = st.file_uploader("Upload an audio file", type=["mp3", "wav", "m4a"])

if uploaded_file is not None:
    # Upload the Audio File
    audio_file = uploaded_file.read()

    # Transcribe the Audio
    transcription = client.audio.transcriptions.create(
        model='whisper-1',
        file=audio_file,
        response_format='text'
    )

    # Display the Transcription
    st.write(transcription['text'])