import streamlit as st
import csv
import urllib.parse
import webbrowser

# Streamlit app title
st.title("CSV to Obsidian Note Converter")

# File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read and parse the CSV file
    data = []
    csv_reader = csv.DictReader(uploaded_file)
    for row in csv_reader:
        data.append(row)
    
    # Convert parsed CSV data to Markdown format
    markdown_content = ""
    for row in data:
        for key, value in row.items():
            markdown_content += f"**{key}**: {value}\n"
        markdown_content += "\n"
    
    # Display the Markdown content
    st.markdown("### Markdown Content")
    st.text(markdown_content)
    
    # Create Obsidian note URL
    note_title = "Imported CSV Data"
    encoded_title = urllib.parse.quote(note_title)
    encoded_content = urllib.parse.quote(markdown_content)
    obsidian_url = f"obsidian://new?name={encoded_title}&content={encoded_content}"
    
    # Display the Obsidian URL
    st.markdown("### Obsidian URL")
    st.text(obsidian_url)
    
    # Button to open the Obsidian URL
    if st.button("Create Obsidian Note"):
        webbrowser.open(obsidian_url)
        st.success("Obsidian note created successfully!")