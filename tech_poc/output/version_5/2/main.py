import streamlit as st
import openai
import os

# Initialize the OpenAI client
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to generate dinner list using OpenAI API
def generate_dinner_list(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150
        )
        dinner_list = response.choices[0].text.strip()
        return dinner_list
    except Exception as e:
        st.error(f"Error generating dinner list: {e}")
        return None

# Streamlit app UI
st.title("Dinner List Generator")

# User input fields
dietary_restrictions = st.text_input("Dietary Restrictions (optional):")
num_items = st.number_input("Number of Items", min_value=1, max_value=10, value=5)

# Generate button
if st.button("Generate Dinner List"):
    # Format the prompt
    prompt = f"Generate a dinner list with {num_items} items. Dietary restrictions: {dietary_restrictions}."
    
    # Get the dinner list from OpenAI
    dinner_list = generate_dinner_list(prompt)
    
    # Display the dinner list
    if dinner_list:
        st.subheader("Generated Dinner List")
        st.write(dinner_list)

# Error handling for invalid inputs
if not openai.api_key:
    st.error("OpenAI API key is not set. Please set the OPENAI_API_KEY environment variable.")