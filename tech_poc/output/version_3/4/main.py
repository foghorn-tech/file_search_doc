import streamlit as st
import csv
import urllib.parse
import webbrowser

def parse_csv(file):
    parsed_data = []
    csv_reader = csv.reader(file)
    for row in csv_reader:
        parsed_data.append(row)
    return parsed_data

def convert_to_markdown(parsed_data):
    markdown_content = "# Your Note Title\n\n"
    markdown_content += "| Column1 | Column2 | Column3 |\n"
    markdown_content += "|---------|---------|---------|\n"
    for row in parsed_data:
        markdown_content += f"| {' | '.join(row)} |\n"
    return markdown_content

def create_obsidian_note(markdown_content):
    note_title = "Your Note Title"
    encoded_title = urllib.parse.quote(note_title)
    encoded_content = urllib.parse.quote(markdown_content)
    obsidian_url = f"obsidian://new?name={encoded_title}&content={encoded_content}"
    webbrowser.open(obsidian_url)

st.title("CSV to Obsidian Note Converter")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    parsed_data = parse_csv(uploaded_file)
    markdown_content = convert_to_markdown(parsed_data)
    st.markdown("### Markdown Content")
    st.code(markdown_content, language='markdown')
    
    if st.button("Create Obsidian Note"):
        create_obsidian_note(markdown_content)
        st.success("Obsidian note created successfully!")