import os
import pandas as pd
from pyairtable import Api, Table

# Initialize the Airtable client with the API key
api = Api(os.environ['AIRTABLE_API_KEY'])

# Load the CSV file into a DataFrame
csv_file_path = 'path_to_your_csv_file.csv'
df = pd.read_csv(csv_file_path)

# Define the Airtable base and table
base_id = os.environ['APP_BASE_ID']
table_name = 'YourTableName'
table = Table(api, base_id, table_name)

# Convert DataFrame to a list of dictionaries
records = df.to_dict(orient='records')

# Insert data into the Airtable table
for record in records:
    table.create(record)