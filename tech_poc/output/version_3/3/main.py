import streamlit as st
import pandas as pd
from pyairtable import Api
import os

# Streamlit app
st.title('CSV to Airtable Importer')

# Step 1: Prepare Airtable API Credentials
st.header('Step 1: Prepare Airtable API Credentials')
api_key = st.text_input('Enter your Airtable API Key', type='password')
base_id = st.text_input('Enter your Airtable Base ID')
table_name = st.text_input('Enter your Airtable Table Name')

if api_key and base_id and table_name:
    api = Api(api_key)
    table = api.table(base_id, table_name)
    st.success('Airtable API initialized successfully!')

# Step 2: Data Preprocessing
st.header('Step 2: Data Preprocessing')
uploaded_file = st.file_uploader('Upload your CSV file', type='csv')

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write('Data Preview:')
    st.dataframe(df.head())

    # Step 3: Design Airtable Table Structure
    st.header('Step 3: Design Airtable Table Structure')
    st.write('Map your CSV columns to Airtable fields:')
    field_mapping = {}
    for col in df.columns:
        field = st.text_input(f'Map CSV column "{col}" to Airtable field', key=col)
        if field:
            field_mapping[col] = field

    if field_mapping:
        st.write('Field Mapping:')
        st.json(field_mapping)

        # Step 5: Data Import
        st.header('Step 5: Data Import')
        if st.button('Start Import'):
            try:
                for index, row in df.iterrows():
                    record = {field_mapping[col]: row[col] for col in df.columns}
                    table.create(record)
                st.success('Data imported successfully!')
            except Exception as e:
                st.error(f"Error importing data: {e}")

        # Step 7: Verification
        st.header('Step 7: Verification')
        if st.button('Verify Data'):
            try:
                records = table.all()
                st.write('Imported Records:')
                for record in records:
                    st.json(record['fields'])
            except Exception as e:
                st.error(f"Error fetching data: {e}")