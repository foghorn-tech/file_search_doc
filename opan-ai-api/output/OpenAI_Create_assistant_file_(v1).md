# [Create assistant file (v1) Legacy](/docs/api-reference/assistants-v1/createAssistantFile)
post https://api.openai.com/v1/assistants/{assistant_id}/files 
Create an [assistant](/docs/api-reference/assistants-v1) file by attaching a
          [File](/docs/api-reference/files) to an
          [assistant](/docs/api-reference/assistants-v1). 
## Path parameters 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| assistant_id | string | Required | The ID of the assistant for which to create a File.| 
## Request body 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| file_id | string | Required | A File ID (with                   purpose="assistants") that the assistant should                   use. Useful for tools like retrieval and                   code_interpreter that can access files.| 
## Returns 
An
                [assistant file](/docs/api-reference/assistants-v1/file-object)
                object. 

**Example request**
```python
from openai import OpenAI
client = OpenAI()
assistant_file = client.beta.assistants.files.create(
  assistant_id="asst_abc123",
  file_id="file-abc123"
)
print(assistant_file)
```

**Response**
```python
{
  "id": "file-abc123",
  "object": "assistant.file",
  "created_at": 1699055364,
  "assistant_id": "asst_abc123"
}
```
