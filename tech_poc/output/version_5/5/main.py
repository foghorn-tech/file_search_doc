import streamlit as st
import pandas as pd
from notion_client import Client

# Set up the Notion client
notion = Client(auth=st.secrets["NOTION_API_TOKEN"])

# Function to create or update a page in Notion
def create_or_update_page(database_id, row):
    properties = {
        "Name": {
            "title": [
                {
                    "text": {
                        "content": row["Name"]
                    }
                }
            ]
        },
        "Tags": {
            "multi_select": [{"name": tag} for tag in row["Tags"].split(",")]
        }
    }
    notion.pages.create(parent={"database_id": database_id}, properties=properties)

# Streamlit app
st.title("CSV to Notion Importer")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("CSV Data Preview:")
    st.write(df)

    database_id = st.text_input("Enter your Notion Database ID")

    if st.button("Import to Notion"):
        for _, row in df.iterrows():
            create_or_update_page(database_id, row)
        st.success("Data imported successfully!")