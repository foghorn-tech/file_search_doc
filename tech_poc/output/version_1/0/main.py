import streamlit as st
import openai
import os

# Initialize the OpenAI client by setting up the API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Create an assistant with the necessary tools
def create_assistant():
    return openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."}
        ]
    )

# Upload the PDF file to OpenAI's platform
def upload_pdf(file):
    response = openai.File.create(
        file=open(file, "rb"),
        purpose='answers'
    )
    return response['id']

# Create a new conversation thread
def create_conversation():
    return openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."}
        ]
    )

# Add the user's query to the conversation thread
def add_query_to_conversation(conversation_id, query, file_id):
    return openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": query},
            {"role": "system", "content": f"Analyze the PDF file with ID: {file_id}"}
        ]
    )

# Initiate a run to process the user's query
def process_query(conversation_id, query, file_id):
    response = add_query_to_conversation(conversation_id, query, file_id)
    return response['choices'][0]['message']['content']

# Streamlit app
st.title("Chat PDF Bot")

# File uploader
uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    # Upload the PDF file
    file_id = upload_pdf(uploaded_file)
    
    # Create a new conversation
    conversation = create_conversation()
    
    # User query input
    user_query = st.text_input("Enter your query about the PDF")
    
    if st.button("Submit Query"):
        # Process the query
        response = process_query(conversation['id'], user_query, file_id)
        
        # Display the response
        st.write(response)