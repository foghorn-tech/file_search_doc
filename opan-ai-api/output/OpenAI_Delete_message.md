# [Delete message Beta](/docs/api-reference/messages/deleteMessage)
delete https://api.openai.com/v1/threads/{thread_id}/messages/{message_id} 
Deletes a message. 
## Path parameters 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| thread_id | string | Required | The ID of the thread to which this message belongs.| 
| message_id | string | Required | The ID of the message to delete.| 
## Returns 
Deletion status 

**Example request**
```python
from openai import OpenAI
client = OpenAI()
deleted_message = client.beta.threads.messages.delete(
  message_id="msg_abc12",
  thread_id="thread_abc123",
)
print(deleted_message)
```

**Response**
```python
{
  "id": "msg_abc123",
  "object": "thread.message.deleted",
  "deleted": true
}
```
