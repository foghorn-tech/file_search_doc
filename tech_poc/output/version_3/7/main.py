import streamlit as st
from openai import OpenAI
import os

# Initialize OpenAI Client
api_key = st.secrets["openai_api_key"]
client = OpenAI(api_key=api_key)

st.title("Audio Transcription with OpenAI")

# Upload the Audio File
uploaded_file = st.file_uploader("Upload an audio file", type=["mp3", "wav", "m4a"])

if uploaded_file is not None:
    with st.spinner("Transcribing audio..."):
        # Transcribe the Audio
        transcription = client.audio.transcriptions.create(
            model="whisper-1",
            file=uploaded_file,
            response_format="text"
        )
        
        # Display the Transcription
        st.subheader("Transcription")
        st.write(transcription.text)