import streamlit as st
from openai import OpenAI
import os

# Initialize OpenAI Client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "<your OpenAI API key>"))

# Create Assistant with File Search Tool
assistant = client.beta.assistants.create(
    name="PDF Chat Assistant",
    instructions="You are an assistant that helps users extract information from PDF files.",
    model="gpt-4o",
    tools=[{"type": "file_search"}]
)

# Streamlit app
st.title("Chat with your PDF")

# File uploader
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    # Save uploaded file temporarily
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Upload PDF File to OpenAI
    file = client.files.create(file=open("temp.pdf", "rb"), purpose="fine-tune")

    # Create a Thread
    thread = client.beta.threads.create(
        assistant_id=assistant.id,
        messages=[
            {"role": "system", "content": "You can ask questions about the PDF file."}
        ]
    )

    # User input
    user_query = st.text_input("Ask a question about the PDF")

    if st.button("Submit"):
        # Add User Message to the Thread
        client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=user_query
        )

        # Create a Run
        run = client.beta.threads.runs.create_and_poll(
            thread_id=thread.id,
            assistant_id=assistant.id
        )

        # Get the Response from the Assistant
        if run.status == 'completed':
            messages = client.beta.threads.messages.list(thread_id=thread.id)
            response = messages.data[-1].content
            st.write("Assistant's response:", response)
        else:
            st.write("Processing, please wait...")