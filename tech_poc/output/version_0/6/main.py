import streamlit as st
import cv2
import base64
from openai import OpenAI
import os

# Initialize OpenAI client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "<your OpenAI API key>"))

# Function to extract frames from video
def extract_frames(video_path):
    video = cv2.VideoCapture(video_path)
    base64_frames = []
    while video.isOpened():
        success, frame = video.read()
        if not success:
            break
        _, buffer = cv2.imencode(".jpg", frame)
        base64_frames.append(base64.b64encode(buffer).decode("utf-8"))
    video.release()
    return base64_frames

# Streamlit app
st.title("Video Explanation")

uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "avi", "mov"])

if uploaded_file is not None:
    # Save uploaded file temporarily
    with open("temp_video.mp4", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    # Extract frames from video
    frames = extract_frames("temp_video.mp4")
    
    # Prepare prompt with frames
    prompt_messages = [
        {
            "role": "user",
            "content": [
                "These are frames from a video that I want to upload. Generate a compelling description that I can upload along with the video.",
                *map(lambda x: {"image": x, "resize": 768}, frames[0::50]),
            ],
        },
    ]
    
    # Request GPT to describe the video
    params = {
        "model": "gpt-4o",
        "messages": prompt_messages,
        "max_tokens": 200,
    }
    
    result = client.chat.completions.create(**params)
    description = result.choices[0].message.content
    
    # Display the description
    st.write("Video Description:")
    st.write(description)