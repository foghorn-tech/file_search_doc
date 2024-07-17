import os
import csv
import pandas as pd
import time
from notion_client import Client

# Initialize Notion client
notion = Client(auth=os.environ["NOTION_TOKEN"])

# Read the CSV file using pandas
data = pd.read_csv('yourfile.csv')

# Prepare data for Notion
def format_data_for_notion(row):
    return {
        "Name": {"title": [{"text": {"content": row["Name"]}}]},
        "Description": {"rich_text": [{"text": {"content": row["Description"]}}]},
        # Add other properties as needed
    }

formatted_data = [format_data_for_notion(row) for index, row in data.iterrows()]

# Retrieve Notion database ID
database_id = "your_database_id"

# Insert data into Notion database
for item in formatted_data:
    try:
        notion.pages.create(
            parent={"database_id": database_id},
            properties=item
        )
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(1)  # Wait before retrying