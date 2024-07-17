import streamlit as st
import pandas as pd
from notion_client import Client
import os

# Streamlit app title
st.title("CSV to Notion Importer")

# Step 1: Set Up Notion API Connection
st.header("1. Set Up Notion API Connection")
notion_api_key = st.text_input("Enter your Notion API Key", type="password")
if notion_api_key:
    notion = Client(auth=notion_api_key)
    st.success("Notion API Key set successfully!")

# Step 2: Upload CSV File
st.header("2. Upload Your CSV File")
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("CSV Data Preview:")
    st.dataframe(df)

# Step 3: Identify Target Database or Page in Notion
st.header("3. Identify Target Database or Page in Notion")
database_id = st.text_input("Enter your Notion Database ID")
if database_id:
    st.success("Notion Database ID set successfully!")

# Step 4: Map CSV Data to Notion Properties
st.header("4. Map CSV Data to Notion Properties")
property_mapping = {}
if uploaded_file:
    columns = df.columns.tolist()
    for col in columns:
        notion_property = st.text_input(f"Map CSV Column '{col}' to Notion Property", key=col)
        if notion_property:
            property_mapping[col] = notion_property

# Step 5: Create Notion Pages or Database Entries
if st.button("Import CSV to Notion"):
    if notion_api_key and database_id and property_mapping:
        try:
            for index, row in df.iterrows():
                properties = {}
                for csv_col, notion_prop in property_mapping.items():
                    properties[notion_prop] = {"type": "text", "text": {"content": str(row[csv_col])}}
                notion.pages.create(parent={"database_id": database_id}, properties=properties)
            st.success("CSV data imported to Notion successfully!")
        except Exception as e:
            st.error(f"An error occurred: {e}")

# Step 6: Verify the Import
st.header("6. Verify the Import")
if st.button("Verify Import"):
    if notion_api_key and database_id:
        try:
            imported_data = notion.databases.query(database_id=database_id)
            st.write("Imported Data from Notion:")
            st.json(imported_data)
        except Exception as e:
            st.error(f"An error occurred: {e}")