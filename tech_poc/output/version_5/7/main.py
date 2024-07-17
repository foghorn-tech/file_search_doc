import streamlit as st
import openai
import os

# Initialize OpenAI client
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("Audio Transcription with OpenAI Whisper")

# Upload audio file
uploaded_file = st.file_uploader("Upload an audio file", type=["mp3", "wav", "m4a"])

if uploaded_file is not None:
    # Save the uploaded file temporarily
    with open("temp_audio_file", "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.audio(uploaded_file, format='audio/mp3')

    # Transcribe audio using OpenAI Whisper model
    with st.spinner('Transcribing audio...'):
        audio_file = open("temp_audio_file", "rb")
        response = openai.Audio.transcribe("whisper-1", audio_file)
        transcription = response['text']

    # Display transcription
    st.subheader("Transcription")
    st.write(transcription)