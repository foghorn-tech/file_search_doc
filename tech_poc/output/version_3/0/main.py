import streamlit as st
from openai import OpenAI
import os

# Initialize OpenAI client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "<your OpenAI API key>"))

# Create an assistant with required tools
assistant = client.beta.assistants.create(
    instructions="You are a PDF analysis assistant. Use the provided tools to analyze PDF files and answer questions.",
    model="gpt-4o",
    tools=[{"type": "code_interpreter"}, {"type": "file_search"}]
)

# Streamlit app
st.title("Chat PDF Bot")
st.write("Upload a PDF file and ask questions about its content.")

# File uploader
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    # Save the uploaded file temporarily
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Upload the PDF file to OpenAI for analysis
    file = client.files.create(
        file=open("temp.pdf", "rb"),
        purpose="assistants"
    )

    # Create a thread to manage the conversation context
    thread = client.beta.threads.create()

    # User input for questions
    user_query = st.text_input("Ask a question about the PDF")

    if st.button("Submit"):
        if user_query:
            # Add a message to the thread with the user's query and attach the uploaded PDF file
            message = client.beta.threads.messages.create(
                thread_id=thread.id,
                role="user",
                content=user_query,
                attachments=[{"file_id": file.id, "tools": [{"type": "file_search"}]}]
            )

            # Initiate a run to process the user's query and get the response from the assistant
            run = client.beta.threads.runs.create_and_poll(
                thread_id=thread.id,
                assistant_id=assistant.id
            )

            if run.status == 'completed':
                messages = client.beta.threads.messages.list(thread_id=thread.id)
                result = messages.data[0].content[0].text.value
                st.write(result)
            else:
                st.write("Processing in progress, please wait...")
        else:
            st.write("Please enter a question.")