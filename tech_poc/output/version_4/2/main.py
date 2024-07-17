import streamlit as st
import openai
import os

# Initialize the OpenAI client
openai.api_key = os.getenv("OPENAI_API_KEY", "<your OpenAI API key>")

# Function to collect user input for dinner preferences
def get_user_preferences():
    cuisine = st.text_input("Enter preferred cuisine (e.g., Italian, Chinese):")
    dietary_restrictions = st.text_input("Enter any dietary restrictions (e.g., vegetarian, gluten-free):")
    number_of_dishes = st.number_input("Enter the number of dishes you want:", min_value=1, step=1)
    return cuisine, dietary_restrictions, number_of_dishes

# Function to create a prompt for OpenAI based on the user input
def create_prompt(cuisine, dietary_restrictions, number_of_dishes):
    prompt = f"Generate a dinner list with {number_of_dishes} dishes. Cuisine: {cuisine}. Dietary restrictions: {dietary_restrictions}."
    return prompt

# Function to send the prompt to OpenAI's API and retrieve the generated dinner list
def generate_dinner_list(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Main function to integrate all the steps
def main():
    st.title("Dinner List Generator")
    
    cuisine, dietary_restrictions, number_of_dishes = get_user_preferences()
    
    if st.button("Generate Dinner List"):
        if cuisine and dietary_restrictions and number_of_dishes:
            prompt = create_prompt(cuisine, dietary_restrictions, number_of_dishes)
            dinner_list = generate_dinner_list(prompt)
            st.subheader("Generated Dinner List:")
            st.write(dinner_list)
        else:
            st.error("Please fill in all the fields.")

if __name__ == "__main__":
    main()