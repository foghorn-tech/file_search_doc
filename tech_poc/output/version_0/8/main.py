import streamlit as st
from PIL import Image
import requests
from io import BytesIO

st.title("Image Explanation")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    
    # Convert image to bytes
    img_byte_arr = BytesIO()
    image.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()
    
    # Encode image to base64
    import base64
    encoded_image = base64.b64encode(img_byte_arr).decode('utf-8')
    
    # Send image to OpenAI for explanation
    import openai
    openai.api_key = st.secrets["openai_api_key"]
    
    response = openai.ChatCompletion.create(
      model="gpt-4o",
      messages=[
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "What’s in this image?"
            },
            {
              "type": "image_url",
              "image_url": {
                "url": f"data:image/png;base64,{encoded_image}"
              }
            }
          ]
        }
      ],
      max_tokens=300,
    )
    
    explanation = response.choices[0].message['content']
    st.write(explanation)