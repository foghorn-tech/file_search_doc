# Chat Pdf bot

Help me write a chat PDF bot
1. Initialize Open Client
2. Create Assistant with Code Interpreter and File Search tools
3. Upload a pdf file to OpenAI
4. Create a thread
5. Add a message to the thread
6. Create a run
7. Get the response from the assistant

```python
import streamlit as st
from openai import OpenAI

# Streamlit app
st.title("Chat PDF Bot")

# Input for OpenAI API key
api_key = st.text_input("Enter your OpenAI API key:", type="password")

if api_key:
    # Initialize OpenAI client
    client = OpenAI(api_key=api_key)

    # Create an Assistant
    assistant = client.beta.assistants.create(
        name="Document Assistant",
        instructions="You are a helpful assistant that helps users understand PDF documents through a conversational form.",
        tools=[
            {"type": "code_interpreter"}
        ],
        model="gpt-4o",
    )

    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

    if uploaded_file is not None:
        # Upload the file to OpenAI
        file = client.files.create(
            file=uploaded_file,
            purpose='assistants'
        )

        # Create a thread
        thread = client.beta.threads.create()

        # Add a message to the thread
        user_query = st.text_input("Ask a question about the document:")
        if user_query:
            message = client.beta.threads.messages.create(
                thread_id=thread.id,
                role="user",
                content=user_query,
                attachments=[
                    {
                        "file_id": file.id,
                        "tools": [{"type": "code_interpreter"}]
                    }
                ]
            )

            # Create a run
            run = client.beta.threads.runs.create_and_poll(
                thread_id=thread.id,
                assistant_id=assistant.id,
            )
            if run.status == 'completed':
                messages = client.beta.threads.messages.list(
                    thread_id=thread.id
                )
                for msg in messages:
                    st.write(messages.data[0].content[0].text.value)
            else:
                st.write("Processing...")
```