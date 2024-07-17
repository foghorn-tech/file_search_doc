import streamlit as st
import openai
import os

# Initialize OpenAI Client
openai.api_key = st.secrets["openai_api_key"]

# Streamlit app
st.title("Audio Transcription with OpenAI's Whisper Model")

# File uploader
uploaded_file = st.file_uploader("Upload an audio file", type=["mp3", "wav", "m4a"])

if uploaded_file is not None:
    # Save the uploaded file temporarily
    with open("temp_audio_file", "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Open the audio file in binary mode
    with open("temp_audio_file", "rb") as audio_file:
        # Create Transcription Request
        transcription = openai.Audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )

    # Retrieve and display the transcription
    st.subheader("Transcription")
    st.write(transcription["text"])

    # Close the audio file
    audio_file.close()

    # Remove the temporary file
    os.remove("temp_audio_file")