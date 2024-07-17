import streamlit as st
import pandas as pd
from pyairtable import Api, Table
import os

# Streamlit app title
st.title("CSV to Airtable Importer")

# Step 1: Prepare Airtable API Credentials
st.header("Step 1: Prepare Airtable API Credentials")
api_key = st.text_input("Enter your Airtable API Key", type="password")
base_id = st.text_input("Enter your Airtable Base ID")
table_name = st.text_input("Enter your Airtable Table Name")

# Step 2: Upload CSV File
st.header("Step 2: Upload CSV File")
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Step 3: Read and Preprocess the CSV Data
    df = pd.read_csv(uploaded_file)
    st.write("CSV Data Preview:")
    st.write(df.head())

    # Step 4: Initialize the Airtable Client
    if api_key and base_id and table_name:
        api = Api(api_key)
        table = Table(api, base_id, table_name)

        # Step 5: Check for Existing Table
        try:
            table.all()
        except Exception as e:
            st.error("Table does not exist. Please create the table manually in Airtable.")
            st.stop()

        # Step 6: Map CSV Data to Airtable Fields
        st.header("Step 6: Map CSV Data to Airtable Fields")
        field_mapping = {}
        for col in df.columns:
            airtable_field = st.text_input(f"Map CSV column '{col}' to Airtable field", col)
            field_mapping[col] = airtable_field

        df = df.rename(columns=field_mapping)

        # Step 7: Import Data into Airtable
        st.header("Step 7: Import Data into Airtable")
        if st.button("Start Import"):
            try:
                for index, row in df.iterrows():
                    record = row.to_dict()
                    table.create(record)
                st.success("Data imported successfully!")
            except Exception as e:
                st.error(f"Error importing record {index}: {e}")

            # Step 9: Verify the Data Import
            st.header("Step 9: Verify the Data Import")
            records = table.all()
            st.write("Imported Records:")
            st.write(records)