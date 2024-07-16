import streamlit as st
import openai
import os

# Initialize OpenAI client
openai.api_key = os.getenv("OPENAI_API_KEY")

# Step 1: Create a user interface (UI) for user inputs
st.title("Dinner List Generator")
st.write("Generate a dinner list based on your preferences using OpenAI's API.")

# User inputs
dietary_restrictions = st.text_input("Dietary Restrictions (e.g., vegetarian, vegan, gluten-free)")
preferred_cuisine = st.text_input("Preferred Cuisine (e.g., Italian, Chinese, Mexican)")
number_of_meals = st.number_input("Number of Meals", min_value=1, max_value=10, step=1)

# Step 2: Capture user inputs and format them into a prompt
if st.button("Generate Dinner List"):
    prompt = f"Generate a dinner list with {number_of_meals} meals. Dietary restrictions: {dietary_restrictions}. Preferred cuisine: {preferred_cuisine}."

    # Step 3: Send the prompt to OpenAI's API
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=150
        )

        # Step 4: Receive and parse the response
        dinner_list = response.choices[0].text.strip()

        # Step 5: Display the dinner list
        st.subheader("Generated Dinner List")
        st.write(dinner_list)

        # Step 6: Provide options to save, edit, or regenerate the list
        if st.button("Regenerate List"):
            st.experimental_rerun()

    except Exception as e:
        st.error(f"An error occurred: {e}")