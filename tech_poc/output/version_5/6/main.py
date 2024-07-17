import streamlit as st
import openai
import cv2
import base64
import numpy as np
from io import BytesIO
from PIL import Image

# Initialize OpenAI client
openai.api_key = st.secrets["openai_api_key"]

# Function to extract frames from video
def extract_frames(video_path, interval=30):
    vidcap = cv2.VideoCapture(video_path)
    frames = []
    success, image = vidcap.read()
    count = 0
    while success:
        if count % interval == 0:
            frames.append(image)
        success, image = vidcap.read()
        count += 1
    vidcap.release()
    return frames

# Function to encode frames to base64
def encode_frames(frames):
    encoded_frames = []
    for frame in frames:
        _, buffer = cv2.imencode('.jpg', frame)
        encoded_frame = base64.b64encode(buffer).decode('utf-8')
        encoded_frames.append(encoded_frame)
    return encoded_frames

# Function to create prompt for GPT-4
def create_prompt(encoded_frames):
    prompt = "Describe the content of the following video frames:\n"
    for i, frame in enumerate(encoded_frames):
        prompt += f"Frame {i+1}: {frame}\n"
    return prompt

# Function to get description from GPT-4
def get_description(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500
    )
    return response.choices[0].text.strip()

# Streamlit app
st.title("Video Content Description using GPT-4")

uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "avi", "mov"])

if uploaded_file is not None:
    with st.spinner("Extracting frames from video..."):
        frames = extract_frames(uploaded_file)

    with st.spinner("Encoding frames..."):
        encoded_frames = encode_frames(frames)

    with st.spinner("Creating prompt for GPT-4..."):
        prompt = create_prompt(encoded_frames)

    with st.spinner("Getting description from GPT-4..."):
        description = get_description(prompt)

    st.subheader("Generated Description")
    st.write(description)

    st.subheader("Extracted Frames")
    for frame in frames:
        st.image(frame, channels="BGR")