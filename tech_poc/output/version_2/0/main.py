import streamlit as st
from openai import OpenAI
import os

# Initialize OpenAI Client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "<your OpenAI API key>"))

# Create Assistant with Required Tools
assistant = client.beta.assistants.create(
    name="PDF Chat Assistant",
    instructions="You are an assistant that helps users extract information from PDF files.",
    model="gpt-4o",
    tools=[{"type": "code_interpreter"}, {"type": "file_search"}]
)

# Streamlit app
st.title("Chat PDF Bot")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    # Upload PDF File to OpenAI
    file = client.files.create(file=uploaded_file, purpose="assistants")

    # Create a Thread
    thread = client.beta.threads.create()

    # Add User Query to the Thread
    user_query = st.text_input("Enter your query about the PDF")
    if st.button("Submit Query"):
        message = client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=user_query,
            attachments=[{"file_id": file.id, "tools": [{"type": "file_search"}]}]
        )

        # Run the Assistant
        run = client.beta.threads.runs.create_and_poll(
            thread_id=thread.id,
            assistant_id=assistant.id
        )

        # Display the Results
        if run.status == 'completed':
            messages = client.beta.threads.messages.list(thread_id=thread.id)
            result = messages.data[0].content[0].text.value
            st.write(result)
        else:
            st.write("Processing, please wait...")