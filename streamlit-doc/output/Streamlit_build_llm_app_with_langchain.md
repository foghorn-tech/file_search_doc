Build an LLM app using LangChain
OpenAI, LangChain, and Streamlit in 18 lines of code
In this tutorial, you will build a Streamlit LLM app that can generate text from a user-provided prompt. This Python app will use the LangChain framework and Streamlit. Optionally, you can deploy your app to Streamlit Community Cloud when you're done.

This tutorial is adapted from a blog post by Chanin Nantesanamat: LangChain tutorial #1: Build an LLM-powered app in 18 lines of code.


Built with Streamlit 🎈
Fullscreen
open_in_new
Objectives
Get an OpenAI key from the end user.
Validate the user's OpenAI key.
Get a text prompt from the user.
Authenticate OpenAI with the user's key.
Send the user's prompt to OpenAI's API.
Get a response and display it.
Bonus: Deploy the app on Streamlit Community Cloud!

Prerequisites
Python 3.8+
Streamlit
LangChain
OpenAI API key
Setup coding environment
In your IDE (integrated coding environment), open the terminal and install the following three Python libraries:

pip install streamlit openai langchain
Create a requirements.txt file located in the root of your working directory and save these dependencies. This is necessary for deploying the app to the Streamlit Community Cloud later.

streamlit
openai
langchain
Building the app
The app is only 18 lines of code:

import streamlit as st
from langchain.llms import OpenAI

st.title('🦜🔗 Quickstart App')

openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')

def generate_response(input_text):
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    st.info(llm(input_text))

with st.form('my_form'):
    text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
    submitted = st.form_submit_button('Submit')
    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI API key!', icon='⚠')
    if submitted and openai_api_key.startswith('sk-'):
        generate_response(text)
To start, create a new Python file and save it as streamlit_app.py in the root of your working directory.

Import the necessary Python libraries.

import streamlit as st
from langchain.llms import OpenAI
Create the app's title using st.title.

st.title('🦜🔗 Quickstart App')
Add a text input box for the user to enter their OpenAI API key.

openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')
Define a function to authenticate to OpenAI API with the user's key, send a prompt, and get an AI-generated response. This function accepts the user's prompt as an argument and displays the AI-generated response in a blue box using st.info.

def generate_response(input_text):
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    st.info(llm(input_text))
Finally, use st.form() to create a text box (st.text_area()) for user input. When the user clicks Submit, the generate-response() function is called with the user's input as an argument.

with st.form('my_form'):
    text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
    submitted = st.form_submit_button('Submit')
    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI API key!', icon='⚠')
    if submitted and openai_api_key.startswith('sk-'):
        generate_response(text)
Remember to save your file!

Return to your computer's terminal to run the app.

streamlit run streamlit_app.py
Deploying the app
To deploy the app to the Streamlit Cloud, follow these steps:

Create a GitHub repository for the app. Your repository should contain two files:

your-repository/
├── streamlit_app.py
└── requirements.txt
Go to Streamlit Community Cloud, click the New app button from your workspace, then specify the repository, branch, and main file path. Optionally, you can customize your app's URL by choosing a custom subdomain.

Click the Deploy! button.

Your app will now be deployed to Streamlit Community Cloud and can be accessed from around the world! 🌎

Conclusion
Congratulations on building an LLM-powered Streamlit app in 18 lines of code! 🥳 You can use this app to generate text from any prompt that you provide. The app is limited by the capabilities of the OpenAI LLM, but it can still be used to generate some creative and interesting text.

We hope you found this tutorial helpful! Check out more examples to see the power of Streamlit and LLM. 💖

Happy Streamlit-ing! 🎈