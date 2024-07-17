import streamlit as st
from openai import OpenAI
import os

# Initialize OpenAI Client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "<your OpenAI API key>"))

# Create Assistant with File Search Tool
assistant = client.beta.assistants.create(
    name="PDF Chat Assistant",
    instructions="You are an assistant that can answer questions based on the content of PDF files.",
    model="gpt-4o",
    tools=[{"type": "file_search"}],
)

# Streamlit app
st.title("Chat PDF Bot")

# File uploader
uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    # Save the uploaded file temporarily
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Upload PDF File to OpenAI
    file = client.files.create(file=open("temp.pdf", "rb"), purpose="file_search")

    # Create a Thread
    thread = client.beta.threads.create()

    # User input for query
    user_query = st.text_input("Enter your query about the PDF content")

    if st.button("Submit Query"):
        # Add User Query to the Thread
        message = client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=user_query,
            attachments=[{"file_id": file.id, "tools": [{"type": "file_search"}]}]
        )

        # Run the Assistant
        run = client.beta.threads.runs.create_and_poll(
            thread_id=thread.id,
            assistant_id=assistant.id,
        )

        # Display the Response
        if run.status == 'completed':
            messages = client.beta.threads.messages.list(thread_id=thread.id)
            response = messages.data[0].content[0].text.value
            st.write(response)
        else:
            st.write("Processing, please wait...")