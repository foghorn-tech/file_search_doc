# [The thread object (v1) Legacy](/docs/api-reference/threads-v1/object)
Represents a thread that contains
          [messages](/docs/api-reference/messages-v1). 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| id | string | Optional | The identifier, which can be referenced in API endpoints.| 
| object | string | Optional | The object type, which is always thread.| 
| created_at | integer | Optional | The Unix timestamp (in seconds) for when the thread was created.| 
| metadata | map | Optional | Set of 16 key-value pairs that can be attached to an object.                 This can be useful for storing additional information about the                 object in a structured format. Keys can be a maximum of 64                 characters long and values can be a maxium of 512 characters                 long.| 

**The thread object (v1)**
```python
{
  "id": "thread_abc123",
  "object": "thread",
  "created_at": 1698107661,
  "metadata": {}
}
```
