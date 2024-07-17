import streamlit as st
from openai import OpenAI
import os

# Initialize OpenAI Client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Create Assistant with File Search Tool
assistant = client.beta.assistants.create(
    name="PDF Chat Assistant",
    instructions="You are an assistant that helps users extract information from PDF files.",
    model="gpt-4o",
    tools=[{"type": "file_search"}]
)

# Streamlit App
st.title("Chat with your PDF")

# Upload PDF File
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    # Save the uploaded file temporarily
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    # Upload PDF File to OpenAI
    file = client.files.create(file=open("temp.pdf", "rb"), purpose="file_search")
    
    # Create a Thread
    thread = client.beta.threads.create(
        messages=[
            {
                "role": "system",
                "content": "You can ask questions about the content of the uploaded PDF."
            }
        ]
    )
    
    # User Query Input
    user_query = st.text_input("Ask a question about the PDF content:")
    
    if st.button("Submit"):
        if user_query:
            # Add User Query to the Thread
            thread = client.beta.threads.update(
                thread_id=thread.id,
                messages=[
                    {
                        "role": "user",
                        "content": user_query
                    }
                ]
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
                st.write(response)
            else:
                st.write("Processing, please wait...")