import streamlit as st
import openai
import base64
from PIL import Image
import io

# Initialize the OpenAI client with your API key
openai.api_key = st.secrets["openai_api_key"]

def encode_image(image):
    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    return img_str

def get_image_description(image_base64):
    response = openai.Image.create(
        prompt="Describe the content of this image",
        n=1,
        size="1024x1024",
        image=image_base64
    )
    description = response['choices'][0]['text']
    return description

st.title("Image Description using OpenAI")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Classifying...")

    # Encode the uploaded image in base64 format
    image_base64 = encode_image(image)

    # Get the description from OpenAI
    description = get_image_description(image_base64)

    # Display the description to the user
    st.write("Description:")
    st.write(description)