import streamlit as st
import openai
import os

# Initialize the OpenAI client by setting up the API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to upload PDF file
def upload_pdf():
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    if uploaded_file is not None:
        return uploaded_file
    return None

# Function to create a new conversation thread
def create_conversation():
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
        ]
    )
    return response['id']

# Function to add a message to the thread
def add_message(conversation_id, user_query):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        conversation_id=conversation_id,
        messages=[
            {"role": "user", "content": user_query},
        ]
    )
    return response

# Function to process the user's query
def process_query(conversation_id, user_query):
    response = add_message(conversation_id, user_query)
    return response['choices'][0]['message']['content']

# Streamlit app
def main():
    st.title("Chat PDF Bot")
    
    # Step 1: Upload the PDF file
    pdf_file = upload_pdf()
    
    if pdf_file:
        # Step 2: Create a new conversation thread
        conversation_id = create_conversation()
        
        # Step 3: Get user query
        user_query = st.text_input("Enter your query about the PDF file:")
        
        if st.button("Submit"):
            # Step 4: Process the user's query
            response = process_query(conversation_id, user_query)
            
            # Step 5: Display the response
            st.write("Response from assistant:")
            st.write(response)

if __name__ == "__main__":
    main()