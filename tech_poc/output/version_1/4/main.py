import csv
import urllib.parse

# Step 1: Prepare the CSV File
csv_file_path = 'path_to_your_csv_file.csv'

# Step 2: Parse the CSV File
with open(csv_file_path, mode='r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    headers = next(csv_reader)
    rows = [row for row in csv_reader]

# Step 3: Format the Data
markdown_content = '| ' + ' | '.join(headers) + ' |\n'
markdown_content += '| ' + ' | '.join(['---'] * len(headers)) + ' |\n'
for row in rows:
    markdown_content += '| ' + ' | '.join(row) + ' |\n'

# Step 4: Create the Obsidian Note
note_title = 'Imported CSV Data'
encoded_title = urllib.parse.quote(note_title)
encoded_content = urllib.parse.quote(markdown_content)
obsidian_uri = f'obsidian://new?name={encoded_title}&content={encoded_content}'

# Step 5: Open the URI
import webbrowser
webbrowser.open(obsidian_uri)