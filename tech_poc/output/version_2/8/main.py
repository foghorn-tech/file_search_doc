import streamlit as st
from openai import OpenAI
import os
import base64

# Initialize OpenAI Client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "<your OpenAI API key>"))

# Function to encode image to base64
def encode_image(image):
    return base64.b64encode(image.read()).decode('utf-8')

# Streamlit app
st.title("Image Explanation using OpenAI Vision")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)
    
    # Encode the image
    base64_image = encode_image(uploaded_file)
    
    # Create the request
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "Explain what happened in this image."},
                        {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
                    ]
                }
            ],
            max_tokens=300,
        )
        explanation = response.choices[0].message.content
        st.write("Explanation of the image:")
        st.write(explanation)
    except Exception as e:
        st.error(f"An error occurred: {e}")