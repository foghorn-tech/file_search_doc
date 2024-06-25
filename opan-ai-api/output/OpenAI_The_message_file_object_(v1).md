# [The message file object (v1) Legacy](/docs/api-reference/messages-v1/file-object)
A list of files attached to a message. 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| id | string | Optional | The identifier, which can be referenced in API endpoints.| 
| object | string | Optional | The object type, which is always                 thread.message.file.| 
| created_at | integer | Optional | The Unix timestamp (in seconds) for when the message file was                 created.| 
| message_id | string | Optional | The ID of the                 message that the                 File is attached to.| 

**The message file object (v1)**
```python
{
  "id": "file-abc123",
  "object": "thread.message.file",
  "created_at": 1698107661,
  "message_id": "message_QLoItBbqwyAJEzlTy4y9kOMM",
  "file_id": "file-abc123"
}
```
