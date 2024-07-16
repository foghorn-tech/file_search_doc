import streamlit as st
from openai import OpenAI
import os

# Initialize the OpenAI client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "<your OpenAI API key>"))

# Function to collect user preferences and dietary restrictions
def get_user_preferences():
    preferences = {}
    preferences['cuisine'] = st.text_input("Enter preferred cuisine (e.g., Italian, Chinese, etc.): ")
    preferences['diet'] = st.text_input("Enter dietary restrictions (e.g., vegetarian, gluten-free, etc.): ")
    preferences['allergies'] = st.text_input("Enter any food allergies: ")
    return preferences

# Function to generate a dinner list using OpenAI's API
def generate_dinner_list(preferences):
    prompt = f"Generate a dinner list based on the following preferences: Cuisine: {preferences['cuisine']}, Dietary Restrictions: {preferences['diet']}, Allergies: {preferences['allergies']}."
    
    response = client.completions.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    
    return response.choices[0].text.strip()

# Main function to integrate the user input collection and the dinner list generation
def main():
    st.title("Dinner List Generator")
    preferences = get_user_preferences()
    if st.button("Generate Dinner List"):
        dinner_list = generate_dinner_list(preferences)
        st.write("Generated Dinner List:")
        st.write(dinner_list)

if __name__ == "__main__":
    main()