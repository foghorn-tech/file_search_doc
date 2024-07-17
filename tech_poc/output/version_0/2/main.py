import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = st.secrets["openai_api_key"]

st.title("AI-Generated Dinner List")

# Function to generate dinner list using OpenAI
def generate_dinner_list(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# User input for dinner preferences
user_input = st.text_input("Enter your dinner preferences:", "Healthy, vegetarian, quick to prepare")

if st.button("Generate Dinner List"):
    with st.spinner("Generating..."):
        dinner_list = generate_dinner_list(f"Generate a dinner list based on the following preferences: {user_input}")
        st.write(dinner_list)