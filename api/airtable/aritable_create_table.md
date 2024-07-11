# Create Airtable Table

## Parameters

| name        | type   | description                                                                                                                  |
|-------------|--------|------------------------------------------------------------------------------------------------------------------------------|
| baseId      | string | The ID of the base where the table will be created.                                                                          |
| name        | string | The name of the table.                                                                                                       |
| fields      | array  | An array of objects representing the fields of the table. Each object should have the following properties: "singleLineText" | "email" | "url" | "multilineText" | "number" | "percent" | "currency" | "singleSelect" | "multipleSelects" | "singleCollaborator" | "multipleCollaborators" | "multipleRecordLinks" | "date" | "dateTime" | "phoneNumber" | "multipleAttachments" | "checkbox" | "formula" | "createdTime" | "rollup" | "count" | "lookup" | "multipleLookupValues" | "autoNumber" | "barcode" | "rating" | "richText" | "duration" | "lastModifiedTime" | "button" | "createdBy" | "lastModifiedBy" | "externalSyncSource" | "aiText" |
| description | string | A description of the table. (optional)                                                                                       |


```python
fields = [ {
    "description": "Name of the apartment",
    "name": "Name",
    "type": "singleLineText"
  },
  {
    "name": "Address",
    "type": "singleLineText"
  },
  {
    "name": "Visited",
    "options": {
      "color": "greenBright",
      "icon": "check"
    },
    "type": "checkbox"
  }]
table = api.base(os.environ['APP_BASE_ID']).create_table('test2', fields, description="This is a test table")
```

## Response

```json
{
  "description": "A to-do list of places to visit",
  "fields": [
    {
      "description": "Name of the apartment",
      "id": "fld1VnoyuotSTyxW1",
      "name": "Name",
      "type": "singleLineText"
    },
    {
      "id": "fldoi0c3GaRQJ3xnI",
      "name": "Address",
      "type": "singleLineText"
    },
    {
      "id": "fldumZe00w09RYTW6",
      "name": "Visited",
      "options": {
        "color": "redBright",
        "icon": "star"
      },
      "type": "checkbox"
    }
  ],
  "id": "tbltp8DGLhqbUmjK1",
  "name": "Apartments",
  "primaryFieldId": "fld1VnoyuotSTyxW1",
  "views": [
    {
      "id": "viwQpsuEDqHFqegkp",
      "name": "Grid view",
      "type": "grid"
    }
  ]
}
```