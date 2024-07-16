import streamlit as st
from openai import OpenAI
import os

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Create an assistant with Code Interpreter tool
assistant = client.beta.assistants.create(
    instructions="You are an AI search bot. Answer the user's queries using the provided tools.",
    model="gpt-4o",
    tools=[{"type": "code_interpreter"}]
)

# Streamlit app
st.title("AI Search Bot")

query = st.text_input("Enter your query:")

if query:
    # Create a thread and add the user's query
    thread = client.beta.threads.create(
        messages=[
            {
                "role": "user",
                "content": query
            }
        ]
    )
    
    run = client.beta.threads.runs.create_and_poll(
        thread_id=thread.id,
        assistant_id=assistant.id
    )
    
    if run.status == 'completed':
        messages = client.beta.threads.messages.list(
            thread_id=thread.id
        )
        result = messages.data[0].content[0].text.value
        st.write(result)
    else:
        st.write("Processing your query, please wait...")