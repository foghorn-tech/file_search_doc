# How to import content into Notion

## Use Python Client
- Set up Notion API connection
- Prompt user to input target ID and ID type (database or page)
- If database ID:
  - Retrieve and display database properties
  - Prompt user to input values for each property
  - Ask user where to place content (properties or child blocks)
  - Get page content from user input
- If page ID:
  - Directly prompt user to input subpage content
- Prompt user to input values for each property
- Format data into Notion API required structure based on ID type and user input
- if user provider database ID, use the database ID to interact with the database
- Use formatted data to create new page or subpage via Notion API
