import streamlit as st
import openai
import os
from sqlalchemy import create_engine
from PyPDF2 import PdfFileReader
import io

# Initialize OpenAI Client
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to read PDF content
def read_pdf(file):
    pdf_reader = PdfFileReader(file)
    text = ""
    for page_num in range(pdf_reader.getNumPages()):
        text += pdf_reader.getPage(page_num).extract_text()
    return text

# Function to handle user query
def handle_query(pdf_text, query):
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=f"Extract information from the following PDF content:\n\n{pdf_text}\n\nUser query: {query}",
        max_tokens=500
    )
    return response.choices[0].text.strip()

# Streamlit UI
st.title("Chat PDF Bot")

# Upload PDF File
uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    pdf_text = read_pdf(uploaded_file)
    st.success("PDF file uploaded and processed successfully.")

    # Create a conversation thread
    if "conversation" not in st.session_state:
        st.session_state.conversation = []

    # Add User Query to the Thread
    user_query = st.text_input("Enter your query about the PDF")
    if st.button("Submit Query"):
        if user_query:
            st.session_state.conversation.append({"user": user_query})
            response = handle_query(pdf_text, user_query)
            st.session_state.conversation.append({"bot": response})

    # Display Conversation Thread
    for message in st.session_state.conversation:
        if "user" in message:
            st.write(f"**User:** {message['user']}")
        if "bot" in message:
            st.write(f"**Bot:** {message['bot']}")

# Error Handling and Logging
try:
    # Your main code logic here
    pass
except Exception as e:
    st.error(f"An error occurred: {e}")
    # Log the error (you can expand this to log to a file or external service)
    print(f"Error: {e}")