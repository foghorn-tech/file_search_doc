# [Retrieve thread Beta](/docs/api-reference/threads/getThread)
get https://api.openai.com/v1/threads/{thread_id} 
Retrieves a thread. 
## Path parameters 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| thread_id | string | Required | The ID of the thread to retrieve.| 
## Returns 
The
                [thread](/docs/api-reference/threads/object) object
                matching the specified ID. 

**Example request**
```python
from openai import OpenAI
client = OpenAI()
my_thread = client.beta.threads.retrieve("thread_abc123")
print(my_thread)
```

**Response**
```python
{
  "id": "thread_abc123",
  "object": "thread",
  "created_at": 1699014083,
  "metadata": {},
  "tool_resources": {
    "code_interpreter": {
      "file_ids": []
    }
  }
}
```
