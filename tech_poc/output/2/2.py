import streamlit as st
import openai
import os

# Initialize OpenAI client
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to generate dinner list
def generate_dinner_list(preferences):
    prompt = f"Generate a dinner list for a week considering the following preferences: {preferences}."
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Streamlit UI
st.title("Dinner List Generator")

st.header("Enter your preferences")
dietary_restrictions = st.text_input("Dietary Restrictions")
preferred_cuisine = st.text_input("Preferred Cuisine Types")
number_of_meals = st.number_input("Number of Meals", min_value=1, max_value=21, value=7)

if st.button("Generate Dinner List"):
    preferences = {
        "dietary_restrictions": dietary_restrictions,
        "preferred_cuisine": preferred_cuisine,
        "number_of_meals": number_of_meals
    }
    dinner_list = generate_dinner_list(preferences)
    st.subheader("Generated Dinner List")
    st.write(dinner_list)