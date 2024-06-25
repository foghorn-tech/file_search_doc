# [Retrieve message Beta](/docs/api-reference/messages/getMessage)
get https://api.openai.com/v1/threads/{thread_id}/messages/{message_id} 
Retrieve a message. 
## Path parameters 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| thread_id | string | Required | The ID of the                   thread to which this                   message belongs.| 
| message_id | string | Required | The ID of the message to retrieve.| 
## Returns 
The
                [message](/docs/api-reference/threads/messages/object)
                object matching the specified ID. 

**Example request**
```python
from openai import OpenAI
client = OpenAI()
message = client.beta.threads.messages.retrieve(
  message_id="msg_abc123",
  thread_id="thread_abc123",
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
  "attachments": [],
  "metadata": {}
}
```
