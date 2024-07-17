import streamlit as st
from openai import OpenAI
import os

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Step 2: Upload Audio File
audio_file = st.file_uploader("Upload an audio file", type=["mp3", "wav", "m4a"])

if audio_file is not None:
    # Step 3: Transcribe Audio
    transcription = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file,
        response_format="text"
    )
    
    # Step 4: Retrieve Transcription
    transcribed_text = transcription['text']
    
    # Step 5: Analyze Transcription
    st.write("Transcribed Text:")
    st.write(transcribed_text)
    
    # Step 6: Provide Explanation
    st.write("Explanation of the Audio Content:")
    # Here you can add any additional analysis or summary of the transcribed text
    st.write(transcribed_text)