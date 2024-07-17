import streamlit as st
import base64
from openai import OpenAI

# Initialize OpenAI Client
client = OpenAI(api_key="your_api_key")

# Function to encode image
def encode_image(image):
    return base64.b64encode(image.read()).decode('utf-8')

# Streamlit app
st.title("Image Description using OpenAI")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)
    
    # Encode the image
    base64_image = encode_image(uploaded_file)
    
    # Create API request
    try:
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
        st.write("Description of the image:")
        st.write(description)
    except Exception as e:
        st.error(f"An error occurred: {e}")