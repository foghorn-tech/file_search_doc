import os
import csv
from notion_client import Client

# Initialize the Notion client with your API token
notion = Client(auth=os.getenv("NOTION_TOKEN"))

# Define the database ID where the data will be imported
database_id = "your_database_id_here"

# Function to create a new page in the Notion database
def create_page(properties):
    new_page = {
        "parent": {"database_id": database_id},
        "properties": properties
    }
    notion.pages.create(**new_page)

# Open and read the CSV file
with open('your_file.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        # Map CSV headers to Notion database properties
        properties = {
            "Name": {"title": [{"text": {"content": row["Name"]}}]},
            "Tags": {"multi_select": [{"name": tag} for tag in row["Tags"].split(",")]}
            # Add more properties as needed
        }
        create_page(properties)

print("Data imported successfully.")