import streamlit as st
from openai import OpenAI
import os

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Create an assistant with Code Interpreter tool
assistant = client.beta.assistants.create(
    instructions="You are an AI search bot. Answer questions based on the provided data.",
    model="gpt-4o",
    tools=[{"type": "code_interpreter"}]
)

# Streamlit app
st.title("AI Search Bot")

# User input
user_query = st.text_input("Enter your query:")

if user_query:
    # Create a thread and add the user's query
    thread = client.beta.threads.create(
        messages=[
            {
                "role": "user",
                "content": user_query
            }
        ]
    )
    
    # Run the assistant with the user's query
    run = client.beta.threads.runs.create_and_poll(
        thread_id=thread.id,
        assistant_id=assistant.id
    )
    
    # Display the results of the analysis
    if run.status == 'completed':
        messages = client.beta.threads.messages.list(
            thread_id=thread.id
        )
        result = messages.data[0].content[0].text.value
        st.write(result)
    else:
        st.write("Analysis in progress, please wait...")