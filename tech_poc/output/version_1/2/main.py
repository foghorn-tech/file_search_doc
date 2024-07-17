import streamlit as st
import openai
import os

# Initialize the OpenAI client
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to generate a dinner list
def generate_dinner_list(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Define the prompt for the OpenAI API
prompt = "Generate a list of dinner ideas. Include a variety of cuisines and dietary options."

# Streamlit app
st.title("Dinner List Generator")

if st.button("Generate Dinner List"):
    dinner_list = generate_dinner_list(prompt)
    st.write("Here are some dinner ideas:")
    st.write(dinner_list)