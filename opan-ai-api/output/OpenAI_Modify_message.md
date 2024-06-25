# [Modify message Beta](/docs/api-reference/messages/modifyMessage)
post https://api.openai.com/v1/threads/{thread_id}/messages/{message_id} 
Modifies a message. 
## Path parameters 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| thread_id | string | Required | The ID of the thread to which this message belongs.| 
| message_id | string | Required | The ID of the message to modify.| 
## Request body 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| metadata | map | Optional | Set of 16 key-value pairs that can be attached to an object.                   This can be useful for storing additional information about                   the object in a structured format. Keys can be a maximum of 64                   characters long and values can be a maxium of 512 characters                   long.| 
## Returns 
The modified
                [message](/docs/api-reference/threads/messages/object)
                object. 

**Example request**
```python
from openai import OpenAI
client = OpenAI()
message = client.beta.threads.messages.update(
  message_id="msg_abc12",
  thread_id="thread_abc123",
  metadata={
    "modified": "true",
    "user": "abc123",
  },
)
print(message)
```

**Response**
```python
{
  "id": "msg_abc123",
  "object": "thread.message",
  "created_at": 1699017614,
  "assistant_id": null,
  "thread_id": "thread_abc123",
  "run_id": null,
  "role": "user",
  "content": [
    {
      "type": "text",
      "text": {
        "value": "How does AI work? Explain it in simple terms.",
        "annotations": []
      }
    }
  ],
  "file_ids": [],
  "metadata": {
    "modified": "true",
    "user": "abc123"
  }
}
```
