# How to Import Content into Notion

## Use Python Client

1. **Set Up Notion API Connection**
   - Configure the connection to the Notion API.

2. **Prompt for Target ID and ID Type**
   - Ask the user to input the target ID and specify whether it's a database or a page.

3. **Handle Based on ID Type**
   - **If Database ID:**
     - Retrieve and display the database properties.
     - Prompt the user to input values for each property.
     - Ask the user whether to place content in properties or child blocks.
     - Collect the page content from user input.
   - **If Page ID:**
     - Directly prompt the user to input subpage content.

4. **Format Data**
   - Prompt the user to input values for each property.
   - Format the data according to the Notion API requirements, based on the ID type and user input.

5. **Interact with Notion API**
   - If a database ID is provided, use it to interact with the database.
   - Use the formatted data to create a new page or subpage via the Notion API.
