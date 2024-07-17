import streamlit as st
import pandas as pd
import urllib.parse

# Function to convert DataFrame to Markdown table
def df_to_markdown(df):
    markdown = df.to_markdown(index=False)
    return markdown

# Function to create Obsidian URL
def create_obsidian_url(title, content):
    encoded_title = urllib.parse.quote(title)
    encoded_content = urllib.parse.quote(content)
    url = f"obsidian://new?name={encoded_title}&content={encoded_content}"
    return url

# Streamlit app
st.title("CSV to Obsidian Note")

# File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read the CSV file
    df = pd.read_csv(uploaded_file)
    
    # Convert DataFrame to Markdown table
    markdown_table = df_to_markdown(df)
    
    # Display the Markdown table
    st.markdown("### Markdown Table")
    st.text(markdown_table)
    
    # Input for note title
    note_title = st.text_input("Enter the note title")
    
    if st.button("Generate Obsidian URL"):
        if note_title:
            # Create Obsidian URL
            obsidian_url = create_obsidian_url(note_title, markdown_table)
            
            # Display the Obsidian URL
            st.markdown(f"[Create Obsidian Note]({obsidian_url})")
        else:
            st.error("Please enter a note title.")