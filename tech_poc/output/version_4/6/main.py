import streamlit as st
import cv2
import base64
import openai
import numpy as np
from PIL import Image
from io import BytesIO

# Set OpenAI API key
openai.api_key = st.secrets["openai_api_key"]

def extract_frames(video_path, frame_interval=50):
    vidcap = cv2.VideoCapture(video_path)
    frames = []
    success, image = vidcap.read()
    count = 0
    while success:
        if count % frame_interval == 0:
            frames.append(image)
        success, image = vidcap.read()
        count += 1
    vidcap.release()
    return frames

def encode_frames(frames):
    encoded_frames = []
    for frame in frames:
        _, buffer = cv2.imencode('.jpg', frame)
        jpg_as_text = base64.b64encode(buffer).decode('utf-8')
        encoded_frames.append(jpg_as_text)
    return encoded_frames

def generate_prompt(encoded_frames):
    prompt = "These are frames from a video that I want to upload. Generate a compelling description that I can upload along with the video.\n"
    for frame in encoded_frames:
        prompt += f"![frame](data:image/jpeg;base64,{frame})\n"
    return prompt

def get_video_description(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500
    )
    return response.choices[0].text.strip()

def main():
    st.title("Video Description Generator")
    
    uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "avi", "mov"])
    
    if uploaded_file is not None:
        # Save uploaded video to a temporary file
        tfile = BytesIO(uploaded_file.read())
        video_path = "temp_video.mp4"
        with open(video_path, "wb") as f:
            f.write(tfile.getbuffer())
        
        st.video(video_path)
        
        st.write("Extracting frames from the video...")
        frames = extract_frames(video_path)
        
        st.write("Encoding frames for analysis...")
        encoded_frames = encode_frames(frames)
        
        st.write("Generating prompt for the model...")
        prompt = generate_prompt(encoded_frames)
        
        st.write("Sending request to OpenAI model...")
        description = get_video_description(prompt)
        
        st.write("Generated Description:")
        st.write(description)

if __name__ == "__main__":
    main()