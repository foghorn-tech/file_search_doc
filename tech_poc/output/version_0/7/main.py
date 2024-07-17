import streamlit as st
from openai import OpenAI
import os

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Upload the audio file
audio_file = st.file_uploader("Upload an audio file", type=["mp3", "wav", "m4a"])

if audio_file is not None:
    # Transcribe the audio file
    transcription = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file,
        response_format="text"
    )
    
    # Display the transcription
    st.write("Transcription of the audio:")
    st.write(transcription.text)