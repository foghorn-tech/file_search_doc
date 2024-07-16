import os
import pandas as pd
from pyairtable import Api, Table

# Initialize Airtable client
api = Api(os.environ['AIRTABLE_API_KEY'])

# Load CSV data into DataFrame
df = pd.read_csv('path_to_your_csv_file.csv')

# Define your Airtable base and table
base_id = os.environ['APP_BASE_ID']
table_name = os.environ['TABLE_NAME']
table = Table(api, base_id, table_name)

# Insert data into Airtable
for index, row in df.iterrows():
    record = row.to_dict()
    table.create(record)