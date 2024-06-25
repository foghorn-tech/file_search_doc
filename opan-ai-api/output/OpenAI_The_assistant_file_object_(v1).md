# [The assistant file object (v1) Legacy](/docs/api-reference/assistants-v1/file-object)
A list of [Files](/docs/api-reference/files) attached to an
          assistant. 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| id | string | Optional | The identifier, which can be referenced in API endpoints.| 
| object | string | Optional | The object type, which is always assistant.file.| 
| created_at | integer | Optional | The Unix timestamp (in seconds) for when the assistant file was                 created.| 
| assistant_id | string | Optional | The assistant ID that the file is attached to.| 

**The assistant file object (v1)**
```python
{
  "id": "file-abc123",
  "object": "assistant.file",
  "created_at": 1699055364,
  "assistant_id": "asst_abc123"
}
```
