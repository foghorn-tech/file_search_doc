import streamlit as st
import openai
import os

# Initialize OpenAI client
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to generate dinner list
def generate_dinner_list(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Streamlit app
st.title("Dinner List Generator")

prompt = st.text_input("Enter your preferences:")

if st.button("Generate"):
    if prompt:
        dinner_list = generate_dinner_list(prompt)
        st.subheader("Your Dinner List:")
        st.write(dinner_list)
    else:
        st.error("Please enter your preferences.")