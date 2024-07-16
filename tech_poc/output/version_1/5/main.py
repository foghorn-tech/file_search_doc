import os
import csv
from notion_client import Client

# Initialize Notion client
notion = Client(auth=os.getenv("NOTION_TOKEN"))

# Define the database ID
database_id = "your_database_id_here"

# Function to create a new page in the Notion database
def create_page(notion, database_id, row):
    properties = {
        "Name": {
            "title": [
                {
                    "text": {
                        "content": row["Name"]
                    }
                }
            ]
        },
        "Description": {
            "rich_text": [
                {
                    "text": {
                        "content": row["Description"]
                    }
                }
            ]
        },
        "Category": {
            "select": {
                "name": row["Category"]
            }
        },
        "Price": {
            "number": float(row["Price"])
        },
        "In stock": {
            "checkbox": row["In stock"].lower() == "true"
        }
    }

    notion.pages.create(parent={"database_id": database_id}, properties=properties)

# Read CSV file and import data into Notion
csv_file_path = "path_to_your_csv_file.csv"

with open(csv_file_path, mode='r', encoding='utf-8-sig') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        create_page(notion, database_id, row)