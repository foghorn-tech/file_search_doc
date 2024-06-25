# [Create message Beta](/docs/api-reference/messages/createMessage)
post https://api.openai.com/v1/threads/{thread_id}/messages 
Create a message. 
## Path parameters 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| thread_id | string | Required | The ID of the                   thread to create a                   message for.| 
## Request body 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| role | string | Required | The role of the entity that is creating the message. Allowed                   values include:                    user: Indicates the message is sent by an                     actual user and should be used in most cases to represent                     user-generated messages.                     assistant: Indicates the message is generated                     by the assistant. Use this value to insert messages from the                     assistant into the conversation.| 
| content | string or array | Required | | 
| attachments | array or null | Optional | A list of files attached to the message, and the tools they                   should be added to.| 
| metadata | map | Optional | Set of 16 key-value pairs that can be attached to an object.                   This can be useful for storing additional information about                   the object in a structured format. Keys can be a maximum of 64                   characters long and values can be a maxium of 512 characters                   long.| 
## Returns 
A
                [message](/docs/api-reference/messages/object)
                object. 

**Example request**
```python
from openai import OpenAI
client = OpenAI()
thread_message = client.beta.threads.messages.create(
  "thread_abc123",
  role="user",
  content="How does AI work? Explain it in simple terms.",
)
print(thread_message)
```

**Response**
```python
{
  "id": "msg_abc123",
  "object": "thread.message",
  "created_at": 1713226573,
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
