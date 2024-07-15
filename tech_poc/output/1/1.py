import streamlit as st
from openai import OpenAI
import os

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Function to create an assistant
def create_assistant():
    assistant = client.beta.assistants.create(
        instructions="You are an AI search bot. Answer user queries by searching through the provided data.",
        model="gpt-4o",
        tools=[{"type": "code_interpreter"}]
    )
    return assistant

# Function to create a thread
def create_thread():
    thread = client.beta.threads.create()
    return thread

# Function to add a message to the thread
def add_message(thread_id, content):
    message = client.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=content
    )
    return message

# Function to run the assistant
def run_assistant(thread_id, assistant_id):
    run = client.beta.threads.runs.create_and_poll(
        thread_id=thread_id,
        assistant_id=assistant_id
    )
    return run

# Streamlit app
st.title("AI Search Bot")

query = st.text_input("Enter your query:")

if st.button("Search"):
    assistant = create_assistant()
    thread = create_thread()
    add_message(thread.id, query)
    run = run_assistant(thread.id, assistant.id)

    if run.status == 'completed':
        messages = client.beta.threads.messages.list(thread_id=thread.id)
        result = messages.data[0].content[0].text.value
        st.write(result)
    else:
        st.write("Processing your query, please wait...")