# [Delete thread (v1) Legacy](/docs/api-reference/threads-v1/deleteThread)
delete https://api.openai.com/v1/threads/{thread_id} 
Delete a thread. 
## Path parameters 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| thread_id | string | Required | The ID of the thread to delete.| 
## Returns 
Deletion status 

**Example request**
```python
from openai import OpenAI
client = OpenAI()
response = client.beta.threads.delete("thread_abc123")
print(response)
```

**Response**
```python
{
  "id": "thread_abc123",
  "object": "thread.deleted",
  "deleted": true
}
```
