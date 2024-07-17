import streamlit as st
from openai import OpenAI
import os

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Streamlit app
st.title("Chat PDF Bot")

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file is not None:
    # Upload file to OpenAI
    file = client.files.create(file=uploaded_file, purpose='assistants')
    
    # Create an assistant with Code Interpreter and File Search tools
    assistant = client.beta.assistants.create(
        instructions="You are a PDF analysis assistant. Extract information or answer questions from the PDF.",
        model="gpt-4o",
        tools=[{"type": "code_interpreter"}, {"type": "file_search"}],
        tool_resources={
            "code_interpreter": {
                "file_ids": [file.id]
            },
            "file_search": {
                "file_ids": [file.id]
            }
        }
    )
    
    # User input for query
    query = st.text_input("Ask a question about the PDF")
    
    if query:
        # Create a thread and add the user's query
        thread = client.beta.threads.create(
            messages=[
                {
                    "role": "user",
                    "content": query,
                    "attachments": [
                        {
                            "file_id": file.id,
                            "tools": [{"type": "code_interpreter"}, {"type": "file_search"}]
                        }
                    ]
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