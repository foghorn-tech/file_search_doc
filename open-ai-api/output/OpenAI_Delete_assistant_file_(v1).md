# [Delete assistant file (v1) Legacy](/docs/api-reference/assistants-v1/deleteAssistantFile)
delete https://api.openai.com/v1/assistants/{assistant_id}/files/{file_id} 
Delete an assistant file. 
## Path parameters 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| assistant_id | string | Required | The ID of the assistant that the file belongs to.| 
| file_id | string | Required | The ID of the file to delete.| 
## Returns 
Deletion status 

**Example request**
```python
from openai import OpenAI
client = OpenAI()
deleted_assistant_file = client.beta.assistants.files.delete(
    assistant_id="asst_abc123",
    file_id="file-abc123"
)
print(deleted_assistant_file)
```

**Response**
```python
{
  id: "file-abc123",
  object: "assistant.file.deleted",
  deleted: true
}
```
