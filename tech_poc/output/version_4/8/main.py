import streamlit as st
import base64
from PIL import Image
import io
from openai import OpenAI

# Initialize OpenAI Client
client = OpenAI(api_key="your_openai_api_key")

# Function to encode image
def encode_image(image):
    return base64.b64encode(image.read()).decode('utf-8')

# Streamlit app
st.title("Image Description using OpenAI")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Encode the image
    base64_image = encode_image(uploaded_file)
    
    # Create the API request
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "What’s in this image?"},
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
                ]
            }
        ],
        max_tokens=300,
    )
    
    # Process the response
    description = response.choices[0].message.content
    
    # Display the image and its description
    image_data = base64.b64decode(base64_image)
    image = Image.open(io.BytesIO(image_data))
    
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("Description:", description)