import pandas as pd
import urllib.parse

# Load the CSV file
csv_file_path = 'path/to/your/file.csv'
data = pd.read_csv(csv_file_path)

# Convert CSV Data to Markdown
def convert_to_markdown(data):
    markdown = '| ' + ' | '.join(data.columns) + ' |\n'
    markdown += '| ' + ' | '.join(['---'] * len(data.columns)) + ' |\n'
    for index, row in data.iterrows():
        markdown += '| ' + ' | '.join(map(str, row.values)) + ' |\n'
    return markdown

markdown_content = convert_to_markdown(data)

# Create a New Note in Obsidian
note_title = 'Imported CSV Data'
encoded_title = urllib.parse.quote(note_title)
encoded_content = urllib.parse.quote(markdown_content)

obsidian_uri = f'obsidian://new?name={encoded_title}&content={encoded_content}'
print(obsidian_uri)