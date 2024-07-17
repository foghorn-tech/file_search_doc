import streamlit as st
import openai
import PyPDF2
from io import BytesIO

# Initialize OpenAI client
openai.api_key = st.secrets["openai_api_key"]

# Function to read PDF content
def read_pdf(file):
    pdf_reader = PyPDF2.PdfFileReader(file)
    text = ""
    for page in range(pdf_reader.getNumPages()):
        text += pdf_reader.getPage(page).extract_text()
    return text

# Function to query OpenAI with PDF content and user query
def query_openai(pdf_text, user_query):
    response = openai.Completion.create(
        engine="davinci",
        prompt=f"The following is the content of a PDF:\n\n{pdf_text}\n\nUser query: {user_query}\n\nResponse:",
        max_tokens=500
    )
    return response.choices[0].text.strip()

# Streamlit app layout
st.title("Chat PDF Bot")

# File uploader
uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    # Read PDF content
    pdf_text = read_pdf(uploaded_file)
    
    # Display PDF content (optional)
    with st.expander("Show PDF content"):
        st.write(pdf_text)
    
    # User query input
    user_query = st.text_input("Enter your query about the PDF content:")
    
    if st.button("Submit Query"):
        if user_query:
            # Query OpenAI with PDF content and user query
            response = query_openai(pdf_text, user_query)
            
            # Display response
            st.write("Response from assistant:")
            st.write(response)
        else:
            st.error("Please enter a query.")