# Create a Database

### Description

Creates a database as a subpage in the specified parent page, with the specified properties schema. Currently, the parent of a new database must be a Notion page or database.

### Param

- **parent** `json required`
  - A page parent.

- **title** `array`
  - Title of database as it appears in Notion. An array of rich text objects.

- **properties** `json required`
  - Property schema of database. The keys are the names of properties as they appear in Notion and the values are property schema objects.

### Database properties

| Field        | Type             | Description                                                                                                                      | Example value |
|--------------|------------------|----------------------------------------------------------------------------------------------------------------------------------|---------------|
| id           | string           | An identifier for the property, usually a short string of random letters and symbols.                                            | "fy:{"        |
|              |                  | Some automatically generated property types have special human-readable IDs. For example, all Title properties have an id of "title". |               |
| name         | string           | The name of the property as it appears in Notion.                                                                                |               |
| description  | string           | The description of a property as it appears in Notion.                                                                           |               |
| type         | string (enum)    | The type that controls the behavior of the property. Possible values are:                                                        | "rich_text"   |
|              |                  | - "checkbox"                                                                                                                     |               |
|              |                  | - "created_by"                                                                                                                   |               |
|              |                  | - "created_time"                                                                                                                 |               |
|              |                  | - "date"                                                                                                                         |               |
|              |                  | - "email"                                                                                                                        |               |
|              |                  | - "files"                                                                                                                        |               |
|              |                  | - "formula"                                                                                                                      |               |
|              |                  | - "last_edited_by"                                                                                                               |               |
|              |                  | - "last_edited_time"                                                                                                             |               |
|              |                  | - "multi_select"                                                                                                                 |               |
|              |                  | - "number"                                                                                                                       |               |
|              |                  | - "people"                                                                                                                       |               |
|              |                  | - "phone_number"                                                                                                                 |               |
|              |                  | - "relation"                                                                                                                     |               |
|              |                  | - "rich_text"                                                                                                                    |               |
|              |                  | - "rollup"                                                                                                                       |               |
|              |                  | - "select"                                                                                                                       |               |
|              |                  | - "status"                                                                                                                       |               |
|              |                  | - "title"                                                                                                                        |               |
|              |                  | - "url"                                                                                                                          |               |

### Code Implementation

```python
database = notion.databases.create(
    parent={"type": "workspace", "workspace": True},
    title="Grocery List",
    properties={
        "Name": {"title": {}},
        "Description": {"rich_text": {}},
        "Category": {"select": {"options": [
            {"name": "Fruit"},
            {"name": "Vegetable"},
            {"name": "Dairy"},
        ]}},
        "Price": {"number": {}},
        "In stock": {"checkbox": {}},
    }
)
```
