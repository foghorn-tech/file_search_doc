import os
import pandas as pd
import streamlit as st
from pyairtable import Api, Table

# Streamlit app
st.title("CSV to Airtable Importer")

# Step 1: Prepare Airtable API Credentials
st.header("Step 1: Airtable API Credentials")
api_key = st.text_input("Enter your Airtable API Key", type="password")
base_id = st.text_input("Enter your Airtable Base ID")
table_name = st.text_input("Enter your Airtable Table Name")

if api_key and base_id and table_name:
    api = Api(api_key)
    table = api.table(base_id, table_name)
    st.success("Airtable API initialized successfully")

# Step 2: Data Preprocessing
st.header("Step 2: Upload CSV File")
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("CSV Data Preview:")
    st.write(df.head())

    # Perform any necessary data cleaning and validation
    required_field = st.text_input("Enter the required field name for validation")
    if required_field:
        df.dropna(subset=[required_field], inplace=True)
        st.success("Data cleaned successfully")

# Step 3: Design Airtable Table Structure
st.header("Step 3: Map CSV Columns to Airtable Fields")
field_mapping = {}
if uploaded_file:
    for col in df.columns:
        airtable_field = st.text_input(f"Map CSV column '{col}' to Airtable field")
        if airtable_field:
            field_mapping[col] = airtable_field

# Step 4: Create Airtable Table (if necessary)
# This step is optional and depends on your specific requirements

# Step 5: Data Import
st.header("Step 5: Import Data to Airtable")
if st.button("Start Import"):
    if api_key and base_id and table_name and uploaded_file and field_mapping:
        for index, row in df.iterrows():
            record = {field_mapping[col]: row[col] for col in df.columns if col in field_mapping}
            try:
                table.create(record)
                st.success(f"Record {index} inserted successfully")
            except Exception as e:
                st.error(f"Error inserting record {index}: {e}")
    else:
        st.error("Please complete all steps before starting the import")