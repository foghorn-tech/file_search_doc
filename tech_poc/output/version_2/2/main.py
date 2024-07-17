import streamlit as st
import openai
import os

# Initialize OpenAI Client
openai.api_key = os.getenv("OPENAI_API_KEY", "<your OpenAI API key>")

# Function to generate dinner list
def generate_dinner_list(preferences):
    prompt = f"Generate a dinner list based on the following preferences: {preferences}"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    dinner_list = response.choices[0].text.strip()
    return dinner_list

# Streamlit UI
st.title("Dinner List Generator")
st.write("Enter your preferences or dietary restrictions:")

preferences = st.text_area("Preferences")

if st.button("Generate Dinner List"):
    if preferences:
        dinner_list = generate_dinner_list(preferences)
        st.write("Here is your generated dinner list:")
        st.write(dinner_list)
    else:
        st.write("Please enter your preferences.")