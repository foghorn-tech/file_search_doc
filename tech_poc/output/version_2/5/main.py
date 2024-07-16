import os
import csv
import pandas as pd
import time
from notion_client import Client

# Set up Notion API connection
notion = Client(auth=os.environ["NOTION_TOKEN"])

# Read the CSV file using pandas
csv_data = pd.read_csv('yourfile.csv').to_dict(orient='records')

# Function to map CSV data to Notion properties
def map_csv_to_notion(csv_row):
    return {
        "Name": {"title": [{"text": {"content": csv_row["Name"]}}]},
        "Description": {"rich_text": [{"text": {"content": csv_row["Description"]}}]},
        # Add more mappings as needed
    }

# Create Notion pages or database entries
for row in csv_data:
    try:
        notion.pages.create(
            parent={"database_id": "your_database_id"},
            properties=map_csv_to_notion(row)
        )
    except Exception as e:
        print(f"Error creating page for row {row}: {e}")
        time.sleep(1)  # Wait before retrying