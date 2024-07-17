import streamlit as st
import openai
import base64
import os

# Initialize the OpenAI client with the appropriate API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to encode the uploaded image in base64 format
def encode_image(image):
    return base64.b64encode(image.read()).decode('utf-8')

# Streamlit app
st.title("Image Content Analysis")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)
    
    # Encode the uploaded image in base64 format
    base64_image = encode_image(uploaded_file)
    
    # Create a request to the OpenAI API
    response = openai.Completion.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Provide a detailed explanation of the events depicted in this image."
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                ]
            }
        ],
        max_tokens=300,
    )
    
    # Parse the response to extract the detailed explanation
    explanation = response.choices[0].message.content
    
    # Display the detailed explanation
    st.write("Detailed Explanation of the Events Depicted in the Image:")
    st.write(explanation)