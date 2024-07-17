import streamlit as st
import pandas as pd
import urllib.parse

# Function to generate Obsidian URL
def generate_obsidian_url(title, content):
    encoded_title = urllib.parse.quote(title)
    encoded_content = urllib.parse.quote(content)
    return f"obsidian://new?name={encoded_title}&content={encoded_content}"

# Streamlit app
st.title("CSV to Obsidian Importer")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("CSV Data:", df)
    
    title_column = st.selectbox("Select the column for titles", df.columns)
    content_column = st.selectbox("Select the column for content", df.columns)
    
    if st.button("Generate Obsidian URLs"):
        for index, row in df.iterrows():
            title = row[title_column]
            content = row[content_column]
            obsidian_url = generate_obsidian_url(title, content)
            st.write(f"[{title}]({obsidian_url})")