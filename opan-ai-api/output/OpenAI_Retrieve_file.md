# [Retrieve file](/docs/api-reference/files/retrieve)
get https://api.openai.com/v1/files/{file_id} 
Returns information about a specific file. 
## Path parameters 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| file_id | string | Required | The ID of the file to use for this request.| 
## Returns 
The [File](/docs/api-reference/files/object) object
                matching the specified ID. 

**Example request**
```python
from openai import OpenAI
client = OpenAI()
client.files.retrieve("file-abc123")
```

**Response**
```python
{
  "id": "file-abc123",
  "object": "file",
  "bytes": 120000,
  "created_at": 1677610602,
  "filename": "mydata.jsonl",
  "purpose": "fine-tune",
}
```
