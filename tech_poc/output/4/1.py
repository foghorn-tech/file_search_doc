import streamlit as st
import pandas as pd
import urllib.parse

# Function to create Obsidian URL
def create_obsidian_url(title, content):
    encoded_title = urllib.parse.quote(title)
    encoded_content = urllib.parse.quote(content)
    return f"obsidian://new?name={encoded_title}&content={encoded_content}"

# Streamlit app
st.title("CSV to Obsidian Importer")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("CSV Data:", df)
    
    title = st.text_input("Enter the title for the Obsidian note")
    if st.button("Generate Obsidian URL"):
        content = df.to_csv(index=False)
        obsidian_url = create_obsidian_url(title, content)
        st.markdown(f"[Click here to create the note in Obsidian]({obsidian_url})")