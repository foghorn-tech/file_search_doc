import streamlit as st
import cv2
import base64
import openai
import numpy as np
from PIL import Image
from io import BytesIO

# Set OpenAI API key
openai.api_key = st.secrets["openai_api_key"]

# Function to extract frames from video
def extract_frames(video_path, interval=50):
    vidcap = cv2.VideoCapture(video_path)
    frames = []
    success, image = vidcap.read()
    count = 0
    while success:
        if count % interval == 0:
            # Convert frame to RGB
            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            frames.append(image_rgb)
        success, image = vidcap.read()
        count += 1
    vidcap.release()
    return frames

# Function to encode frames to base64
def encode_frames(frames):
    encoded_frames = []
    for frame in frames:
        pil_img = Image.fromarray(frame)
        buffered = BytesIO()
        pil_img.save(buffered, format="JPEG")
        encoded_frame = base64.b64encode(buffered.getvalue()).decode('utf-8')
        encoded_frames.append(encoded_frame)
    return encoded_frames

# Function to create prompt for OpenAI
def create_prompt(encoded_frames):
    prompt = "Describe the content of the following video frames:\n"
    for idx, frame in enumerate(encoded_frames):
        prompt += f"Frame {idx+1}: {frame}\n"
    prompt += "Provide a detailed description of what is happening in the video."
    return prompt

# Function to get description from OpenAI
def get_video_description(prompt):
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=prompt,
        max_tokens=500
    )
    return response.choices[0].text.strip()

# Streamlit app
st.title("Video Content Description")

# Upload video file
uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "avi", "mov"])

if uploaded_file is not None:
    # Save uploaded video to a temporary file
    with open("temp_video.mp4", "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Extract frames from video
    frames = extract_frames("temp_video.mp4")

    # Encode frames to base64
    encoded_frames = encode_frames(frames)

    # Create prompt for OpenAI
    prompt = create_prompt(encoded_frames)

    # Get video description from OpenAI
    description = get_video_description(prompt)

    # Display the description
    st.header("Video Description")
    st.write(description)