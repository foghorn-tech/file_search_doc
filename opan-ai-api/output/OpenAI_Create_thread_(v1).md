# [Create thread (v1) Legacy](/docs/api-reference/threads-v1/createThread)
post https://api.openai.com/v1/threads 
Create a thread. 
## Request body 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| messages | array | Optional | A list of                   messages to                   start the thread with.| 
| metadata | map | Optional | Set of 16 key-value pairs that can be attached to an object.                   This can be useful for storing additional information about                   the object in a structured format. Keys can be a maximum of 64                   characters long and values can be a maxium of 512 characters                   long.| 
## Returns 
A [thread](/docs/api-reference/threads-v1) object. 

**Example request**
```python
from openai import OpenAI
client = OpenAI()
empty_thread = client.beta.threads.create()
print(empty_thread)
```

**Response**
```python
{
  "id": "thread_abc123",
  "object": "thread",
  "created_at": 1699012949,
  "metadata": {}
}
```
