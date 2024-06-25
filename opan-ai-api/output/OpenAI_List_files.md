# [List files](/docs/api-reference/files/list)
get https://api.openai.com/v1/files 
Returns a list of files that belong to the user's organization. 
## Query parameters 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| purpose | string | Optional | Only return files with the given purpose.| 
## Returns 
A list of
                [File](/docs/api-reference/files/object) objects. 

**Example request**
```python
from openai import OpenAI
client = OpenAI()
client.files.list()
```

**Response**
```python
{
  "data": [
    {
      "id": "file-abc123",
      "object": "file",
      "bytes": 175,
      "created_at": 1613677385,
      "filename": "salesOverview.pdf",
      "purpose": "assistants",
    },
    {
      "id": "file-abc123",
      "object": "file",
      "bytes": 140,
      "created_at": 1613779121,
      "filename": "puppy.jsonl",
      "purpose": "fine-tune",
    }
  ],
  "object": "list"
}
```
