import streamlit as st
import pandas as pd
from pyairtable import Table
import os

# Set up environment variables
AIRTABLE_API_KEY = os.getenv('AIRTABLE_API_KEY')
BASE_ID = os.getenv('BASE_ID')
TABLE_NAME = os.getenv('TABLE_NAME')

# Streamlit app
st.title("CSV to Airtable Importer")

# File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read the CSV file
    df = pd.read_csv(uploaded_file)
    st.write("CSV Data Preview:")
    st.write(df.head())

    # Initialize Airtable client
    table = Table(AIRTABLE_API_KEY, BASE_ID, TABLE_NAME)

    # Insert data into Airtable
    if st.button("Upload to Airtable"):
        for index, row in df.iterrows():
            record = row.to_dict()
            try:
                table.create(record)
                st.success(f"Record {index + 1} inserted successfully.")
            except Exception as e:
                st.error(f"Error inserting record {index + 1}: {e}")

        st.write("Data upload complete.")