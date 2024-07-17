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
    st.write("CSV Data:")
    st.write(df)

    # Get Notion database ID from user
    database_id = st.text_input("Enter Notion Database ID")

    if st.button("Import to Notion"):
        # Convert DataFrame to list of dictionaries
        data = df.to_dict(orient="records")

        # Function to create a page in Notion
        def create_page(data):
            new_page = {
                "parent": {"database_id": database_id},
                "properties": {}
            }
            for key, value in data.items():
                new_page["properties"][key] = {
                    "title": [
                        {
                            "text": {
                                "content": str(value)
                            }
                        }
                    ]
                }
            return new_page

        # Import each row to Notion
        for row in data:
            page = create_page(row)
            notion.pages.create(**page)

        st.success("Data imported successfully!")