# [The message object (v1) Legacy](/docs/api-reference/messages-v1/object)
Represents a message within a
          [thread](/docs/api-reference/threads-v1). 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| id | string | Optional | The identifier, which can be referenced in API endpoints.| 
| object | string | Optional | The object type, which is always thread.message.| 
| created_at | integer | Optional | The Unix timestamp (in seconds) for when the message was                 created.| 
| thread_id | string | Optional | The thread ID that                 this message belongs to.| 
| status | string | Optional | The status of the message, which can be either                 in_progress, incomplete, or                 completed.| 
| incomplete_details | object or null | Optional | On an incomplete message, details about why the message is                 incomplete.| 
| completed_at | integer or null | Optional | The Unix timestamp (in seconds) for when the message was                 completed.| 
| incomplete_at | integer or null | Optional | The Unix timestamp (in seconds) for when the message was marked                 as incomplete.| 
| role | string | Optional | The entity that produced the message. One of                 user or assistant.| 
| content | array | Optional | The content of the message in array of text and/or images.| 
| assistant_id | string or null | Optional | If applicable, the ID of the                 assistant that                 authored this message.| 
| run_id | string or null | Optional | The ID of the                 run associated with                 the creation of this message. Value is null when                 messages are created manually using the create message or create                 thread endpoints.| 
| file_ids | array | Optional | A list of file IDs that                 the assistant should use. Useful for tools like retrieval and                 code_interpreter that can access files. A maximum of 10 files                 can be attached to a message.| 
| metadata | map | Optional | Set of 16 key-value pairs that can be attached to an object.                 This can be useful for storing additional information about the                 object in a structured format. Keys can be a maximum of 64                 characters long and values can be a maxium of 512 characters                 long.| 

**The message object (v1)**
```python
{
  "id": "msg_abc123",
  "object": "thread.message",
  "created_at": 1698983503,
  "thread_id": "thread_abc123",
  "role": "assistant",
  "content": [
    {
      "type": "text",
      "text": {
        "value": "Hi! How can I help you today?",
        "annotations": []
      }
    }
  ],
  "file_ids": [],
  "assistant_id": "asst_abc123",
  "run_id": "run_abc123",
  "metadata": {}
}
```
