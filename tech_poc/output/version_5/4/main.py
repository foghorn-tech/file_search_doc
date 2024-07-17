import streamlit as st
import pandas as pd
import base64

def convert_df_to_markdown(df):
    """Convert a DataFrame to a Markdown table."""
    return df.to_markdown(index=False)

def download_link(object_to_download, download_filename, download_link_text):
    """
    Generates a link to download the given object_to_download.
    """
    if isinstance(object_to_download, pd.DataFrame):
        object_to_download = object_to_download.to_csv(index=False)

    b64 = base64.b64encode(object_to_download.encode()).decode()
    return f'<a href="data:file/txt;base64,{b64}" download="{download_filename}">{download_link_text}</a>'

st.title('CSV to Markdown Converter for Obsidian')

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Data Preview:")
    st.dataframe(df)

    markdown = convert_df_to_markdown(df)
    st.write("Markdown Preview:")
    st.text(markdown)

    st.markdown(download_link(markdown, 'converted_markdown.md', 'Download Markdown file'), unsafe_allow_html=True)
    
    st.write("""
    ### Instructions to Import into Obsidian:
    1. Open Obsidian and navigate to the vault where you want to import the data.
    2. Create a new note by clicking on the "New Note" button or pressing `Ctrl+N`.
    3. Copy the Markdown table generated above.
    4. Paste the copied Markdown data into the new note created in Obsidian.
    5. Save the note in Obsidian.
    6. Optionally, format the note further using Obsidian's Markdown editor to ensure it looks the way you want.
    7. Review the imported data in Obsidian to ensure it has been imported correctly.
    8. Make any necessary adjustments or corrections.
    """)