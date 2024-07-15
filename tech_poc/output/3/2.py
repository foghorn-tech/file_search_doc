import os
import pandas as pd
from pyairtable import Api, Table
import streamlit as st

# Streamlit app
st.title("CSV to Airtable Importer")

# Step 1: Prepare Airtable API Credentials
api_key = st.text_input("Enter your Airtable API Key", type="password")
base_id = st.text_input("Enter your Airtable Base ID")
table_name = st.text_input("Enter your Airtable Table Name")

# Step 2: Upload CSV
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file and api_key and base_id and table_name:
    # Step 3: Data Preprocessing
    df = pd.read_csv(uploaded_file)
    st.write("CSV Data Preview:", df.head())

    # Step 4: Initialize Airtable Client
    api = Api(api_key)
    table = Table(api_key, base_id, table_name)

    # Step 5: Data Import
    if st.button("Import to Airtable"):
        for index, row in df.iterrows():
            record = row.to_dict()
            try:
                table.create(record)
                st.success(f"Record {index + 1} inserted successfully.")
            except Exception as e:
                st.error(f"Error inserting record {index + 1}: {e}")