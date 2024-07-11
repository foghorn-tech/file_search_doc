# AirTable

Airtable's Python client: [https://github.com/gtalarico/pyairtable](https://github.com/gtalarico/pyairtable).

## Init the Airtable client with the API key.

```python
import os
from pyairtable import Api
api = Api(os.environ['AIRTABLE_API_KEY'])
```

## Get Exist table
```python
table = api.table(os.environ['APP_BASE_ID'], os.environ['TABLE_ID'])
```
Response:
```json
{
    "id": "rec5eR7IzKSAOBHCz",
    "createdTime": "2017-03-14T22:04:31.000Z",
    "fields": {
        "Name": "Alice",
        "Email": "alice@example.com"
    }
}
```

## Insert data into the table.

```python
table.create({"Name": "Bob"})
```

Response:
```json
{
    "id": "recwAcQdqwe21asdf",
    "createdTime": "...",
    "fields": {"Name": "Bob"}
}
```

## Update data in the table.

```python
table.update("recwAcQdqwe21asdf", {"Name": "Robert"})
```
Response:

```json
{
    "id": "recwAcQdqwe21asdf",
    "createdTime": "...",
    "fields": {"Name": "Robert"}
}
```