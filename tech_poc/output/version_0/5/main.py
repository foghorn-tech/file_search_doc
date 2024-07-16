import os
import pandas as pd
from notion_client import Client
import streamlit as st

# Initialize Notion client
notion = Client(auth=os.environ["NOTION_TOKEN"])

# Streamlit app
st.title("CSV to Notion Importer")

# File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read the CSV file
    df = pd.read_csv(uploaded_file)
    st.write("CSV Data:", df)

    # Notion database ID input
    database_id = st.text_input("Enter Notion Database ID")

    if st.button("Import to Notion"):
        for index, row in df.iterrows():
            properties = {col: {"rich_text": [{"text": {"content": str(row[col])}}]} for col in df.columns}
            notion.pages.create(parent={"database_id": database_id}, properties=properties)
        st.success("Data imported successfully!")