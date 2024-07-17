import streamlit as st
import pandas as pd
from notion_client import Client
import os
import time

# Streamlit app title
st.title("CSV to Notion Importer")

# Upload CSV file
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read the CSV file
    data = pd.read_csv(uploaded_file).to_dict(orient='records')
    st.write("CSV Data:")
    st.write(data)

    # Notion API token input
    notion_token = st.text_input("Enter your Notion API token", type="password")
    database_id = st.text_input("Enter your Notion Database ID")

    if st.button("Import to Notion"):
        if notion_token and database_id:
            # Initialize Notion client
            notion = Client(auth=notion_token)

            # Map CSV data to Notion format
            def map_csv_to_notion(data):
                notion_data = []
                for row in data:
                    notion_row = {
                        "Name": {"title": [{"text": {"content": row["Name"]}}]},
                        "Description": {"rich_text": [{"text": {"content": row["Description"]}}]},
                        # Add more mappings as needed
                    }
                    notion_data.append(notion_row)
                return notion_data

            notion_data = map_csv_to_notion(data)

            # Create Notion pages or database entries
            for item in notion_data:
                try:
                    notion.pages.create(
                        parent={"database_id": database_id},
                        properties=item
                    )
                    st.success(f"Successfully added: {item['Name']['title'][0]['text']['content']}")
                except Exception as e:
                    st.error(f"Error: {e}")
                    time.sleep(1)  # Wait before retrying
        else:
            st.error("Please provide both Notion API token and Database ID.")