# [Retrieve file content](/docs/api-reference/files/retrieve-contents)
get https://api.openai.com/v1/files/{file_id}/content 
Returns the contents of the specified file. 
## Path parameters 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| file_id | string | Required | The ID of the file to use for this request.| 
## Returns 
The file content. 

**Example request**
```python
from openai import OpenAI
client = OpenAI()
content = client.files.content("file-abc123")
```
