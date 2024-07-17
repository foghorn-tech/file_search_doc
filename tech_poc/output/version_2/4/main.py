import csv
import urllib.parse
import webbrowser

# Step 2: Parse the CSV Data
with open('yourfile.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    headers = csv_reader.fieldnames
    rows = [row for row in csv_reader]

# Step 3: Format the Data for Obsidian
markdown_table = '| ' + ' | '.join(headers) + ' |\n'
markdown_table += '| ' + ' | '.join(['---'] * len(headers)) + ' |\n'
for row in rows:
    markdown_table += '| ' + ' | '.join(row.values()) + ' |\n'

# Step 4: Create the Obsidian URL
title = "Imported CSV Data"
content = markdown_table
encoded_title = urllib.parse.quote(title)
encoded_content = urllib.parse.quote(content)
obsidian_url = f"obsidian://new?name={encoded_title}&content={encoded_content}"

# Step 5: Import the Data into Obsidian
webbrowser.open(obsidian_url)