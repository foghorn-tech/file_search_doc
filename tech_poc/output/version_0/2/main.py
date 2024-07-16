import streamlit as st
import openai

# Set up OpenAI API key
openai.api_key = st.secrets["openai_api_key"]

def generate_dinner_list(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

st.title("AI-Generated Dinner List")

prompt = st.text_input("Enter your dinner preferences:", "Generate a dinner list for a week with healthy recipes.")

if st.button("Generate"):
    with st.spinner("Generating..."):
        dinner_list = generate_dinner_list(prompt)
        st.write(dinner_list)