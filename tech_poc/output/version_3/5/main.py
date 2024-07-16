import streamlit as st
import os
import csv
from notion_client import Client

# Streamlit app title
st.title("CSV to Notion Importer")

# Notion API token input
notion_token = st.text_input("Enter your Notion API token:", type="password")

# Notion Database ID input
database_id = st.text_input("Enter your Notion Database ID:")

# CSV file uploader
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if notion_token and database_id and uploaded_file:
    # Initialize Notion client
    notion = Client(auth=notion_token)

    # Read the CSV file
    data = []
    csv_reader = csv.DictReader(uploaded_file)
    for row in csv_reader:
        data.append(row)

    # Prepare data for Notion
    prepared_data = []
    for row in data:
        prepared_data.append({
            "Name": {"title": [{"text": {"content": row["Name"]}}]},
            "Age": {"number": int(row["Age"])},
            "Email": {"email": row["Email"]}
        })

    # Create pages or database entries in Notion
    try:
        for item in prepared_data:
            notion.pages.create(
                parent={"database_id": database_id},
                properties=item
            )
        st.success("Data successfully imported into Notion!")
    except Exception as e:
        st.error(f"An error occurred: {e}")

    # Verify data in Notion
    results = notion.databases.query(database_id=database_id).get("results")
    st.write(f"Number of entries in the database: {len(results)}")