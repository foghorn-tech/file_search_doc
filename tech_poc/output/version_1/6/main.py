import streamlit as st
import cv2
import base64
import os
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Function to extract frames from video
def extract_frames(video_path, frame_interval=50):
    video = cv2.VideoCapture(video_path)
    frames = []
    base64_frames = []
    frame_count = 0

    while video.isOpened():
        success, frame = video.read()
        if not success:
            break
        if frame_count % frame_interval == 0:
            _, buffer = cv2.imencode(".jpg", frame)
            base64_frames.append(base64.b64encode(buffer).decode("utf-8"))
        frame_count += 1

    video.release()
    return base64_frames

# Function to generate video description using GPT
def generate_video_description(frames):
    prompt_messages = [
        {
            "role": "user",
            "content": [
                "These are frames from a video that I want to upload. Generate a compelling description that I can upload along with the video.",
                *map(lambda x: {"image": x, "resize": 768}, frames),
            ],
        },
    ]
    params = {
        "model": "gpt-4o",
        "messages": prompt_messages,
        "max_tokens": 200,
    }
    result = client.chat.completions.create(**params)
    return result.choices[0].message.content

# Streamlit app
st.title("Video Content Analyzer")

uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "avi", "mov"])

if uploaded_file is not None:
    # Save uploaded file temporarily
    video_path = os.path.join("temp", uploaded_file.name)
    with open(video_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Extract frames from video
    st.write("Extracting frames from video...")
    frames = extract_frames(video_path)

    # Generate video description
    st.write("Generating video description...")
    description = generate_video_description(frames)

    # Display the description
    st.write("Video Description:")
    st.write(description)