import os
import pandas as pd
from pyairtable import Api, Table

# Initialize Airtable client
api = Api(os.environ['AIRTABLE_API_KEY'])

# Load CSV data into a DataFrame
csv_file_path = 'path_to_your_csv_file.csv'
df = pd.read_csv(csv_file_path)

# Define your Airtable base and table
base_id = 'your_base_id'
table_name = 'your_table_name'
table = Table(api, base_id, table_name)

# Convert DataFrame to a list of dictionaries
records = df.to_dict(orient='records')

# Insert data into Airtable
for record in records:
    table.create(record)