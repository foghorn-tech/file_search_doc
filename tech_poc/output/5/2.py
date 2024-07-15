import os
import csv
from notion_client import Client

# Step 1: Prepare Notion API Credentials
notion = Client(auth=os.environ["NOTION_TOKEN"])

# Step 2: Read and Parse the CSV File
with open('yourfile.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    data = [row for row in csv_reader]

# Step 3: Define the Notion Database Schema
database = notion.databases.create(
    parent={"type": "workspace", "workspace": True},
    title=[{"type": "text", "text": {"content": "Your Database Title"}}],
    properties={
        "Name": {"title": {}},
        "Description": {"rich_text": {}},
        "Category": {"select": {"options": [
            {"name": "Option1"},
            {"name": "Option2"},
        ]}},
        "Price": {"number": {}},
        "In stock": {"checkbox": {}},
    }
)

# Step 4: Insert Data into Notion Database
for row in data:
    notion.pages.create(
        parent={"database_id": database['id']},
        properties={
            "Name": {"title": [{"text": {"content": row["Name"]}}]},
            "Description": {"rich_text": [{"text": {"content": row["Description"]}}]},
            "Category": {"select": {"name": row["Category"]}},
            "Price": {"number": float(row["Price"])},
            "In stock": {"checkbox": row["In stock"].lower() == 'true'},
        }
    )

# Step 5: Handle Errors and Exceptions
try:
    # Insert data code here
    pass
except Exception as e:
    print(f"An error occurred: {e}")