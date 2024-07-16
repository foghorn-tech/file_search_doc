import pandas as pd
import urllib.parse

# Load the CSV file
df = pd.read_csv('path_to_your_file.csv')

# Convert the DataFrame to a markdown table
markdown_table = df.to_markdown(index=False)

# Encode the title and content for the Obsidian URL
title = "Imported CSV Data"
encoded_title = urllib.parse.quote(title)
encoded_content = urllib.parse.quote(markdown_table)

# Create the Obsidian URL
obsidian_url = f"obsidian://new?name={encoded_title}&content={encoded_content}"

# Print the URL (or you can use it directly in your application)
print(obsidian_url)