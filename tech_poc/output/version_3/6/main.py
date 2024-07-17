import streamlit as st
import cv2
import base64
import openai
import os
from PIL import Image
from io import BytesIO

# Set up OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to extract frames from video
def extract_frames(video_path, interval=50):
    vidcap = cv2.VideoCapture(video_path)
    success, image = vidcap.read()
    frames = []
    count = 0
    while success:
        if count % interval == 0:
            frames.append(image)
        success, image = vidcap.read()
        count += 1
    vidcap.release()
    return frames

# Function to encode frames in base64
def encode_frames(frames):
    encoded_frames = []
    for frame in frames:
        _, buffer = cv2.imencode('.jpg', frame)
        encoded_frame = base64.b64encode(buffer).decode('utf-8')
        encoded_frames.append(encoded_frame)
    return encoded_frames

# Function to prepare prompt for the model
def prepare_prompt(encoded_frames):
    prompt = "Analyze the following frames and describe the video content:\n"
    for i, frame in enumerate(encoded_frames):
        prompt += f"Frame {i+1}: {frame}\n"
    return prompt

# Function to send request to OpenAI model
def get_video_description(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500
    )
    return response.choices[0].text.strip()

# Streamlit app
st.title("Video Content Analyzer")

uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "avi", "mov"])

if uploaded_file is not None:
    # Save uploaded file to disk
    video_path = os.path.join("temp_video", uploaded_file.name)
    with open(video_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.video(video_path)
    
    st.write("Extracting frames from video...")
    frames = extract_frames(video_path)
    
    st.write("Encoding frames...")
    encoded_frames = encode_frames(frames)
    
    st.write("Preparing prompt for the model...")
    prompt = prepare_prompt(encoded_frames)
    
    st.write("Sending request to OpenAI model...")
    description = get_video_description(prompt)
    
    st.write("Video Description:")
    st.write(description)