# [Delete file](/docs/api-reference/files/delete)
delete https://api.openai.com/v1/files/{file_id} 
Delete a file. 
## Path parameters 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| file_id | string | Required | The ID of the file to use for this request.| 
## Returns 
Deletion status. 

**Example request**
```python
from openai import OpenAI
client = OpenAI()
client.files.delete("file-abc123")
```

**Response**
```python
{
  "id": "file-abc123",
  "object": "file",
  "deleted": true
}
```
