import os
import pandas as pd
from notion_client import Client
import streamlit as st

# Initialize Notion client
notion = Client(auth=os.environ["NOTION_TOKEN"])

# Streamlit app
st.title("Import CSV into Notion")

# File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read the CSV file
    df = pd.read_csv(uploaded_file)
    st.write("CSV Data:")
    st.write(df)

    # Notion database ID input
    database_id = st.text_input("Enter Notion Database ID")

    if st.button("Import to Notion"):
        # Retrieve database properties
        db = notion.databases.retrieve(database_id=database_id)
        properties = db['properties']

        # Prepare data for Notion
        for index, row in df.iterrows():
            properties_data = {}
            for col in df.columns:
                if col in properties:
                    properties_data[col] = {
                        properties[col]['type']: row[col]
                    }
            
            # Create a new page in the Notion database
            notion.pages.create(
                parent={"database_id": database_id},
                properties=properties_data
            )
        
        st.success("Data imported successfully!")