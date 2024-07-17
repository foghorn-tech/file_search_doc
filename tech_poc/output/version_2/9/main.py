import streamlit as st
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key="YOUR_API_KEY")

# Function to generate image
def generate_image(prompt):
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        n=1,
        size="1024x1024",
        response_format="url"
    )
    return response.data[0].url

# Function to generate speech
def generate_speech(prompt):
    response = client.speech.generate(
        model="text-to-speech",
        prompt=prompt,
        voice="en_us_male"
    )
    return response.data[0].audio_url

# Streamlit app
st.title("AI Image and Speech Generator")

user_input = st.text_area("Enter Text to Generate Image and Speech")

if st.button("Generate"):
    if user_input:
        image_url = generate_image(user_input)
        speech_url = generate_speech(user_input)
        
        st.image(image_url, caption="Generated Image")
        st.audio(speech_url, format="audio/mpeg")
    else:
        st.error("Please enter some text.")