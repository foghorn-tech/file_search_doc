import streamlit as st
import openai
import os

# Initialize OpenAI Client
openai.api_key = os.getenv("OPENAI_API_KEY", "<your OpenAI API key>")

# Function to generate dinner list
def generate_dinner_list(preferences):
    prompt = f"Generate a dinner list based on the following preferences: {preferences}"
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=150
        )
        dinner_list = response.choices[0].text.strip()
        return dinner_list
    except Exception as e:
        return f"An error occurred: {e}"

# Streamlit App
st.title("Dinner List Generator")

# User input
preferences = st.text_input("Enter your preferences for the dinner list:")

if st.button("Generate Dinner List"):
    if preferences:
        dinner_list = generate_dinner_list(preferences)
        st.subheader("Here is your generated dinner list:")
        st.write(dinner_list)
    else:
        st.error("Please enter your preferences.")