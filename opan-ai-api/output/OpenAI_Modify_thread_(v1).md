# [Modify thread (v1) Legacy](/docs/api-reference/threads-v1/modifyThread)
post https://api.openai.com/v1/threads/{thread_id} 
Modifies a thread. 
## Path parameters 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| thread_id | string | Required | The ID of the thread to modify. Only the                   metadata can be modified.| 
## Request body 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| metadata | map | Optional | Set of 16 key-value pairs that can be attached to an object.                   This can be useful for storing additional information about                   the object in a structured format. Keys can be a maximum of 64                   characters long and values can be a maxium of 512 characters                   long.| 
## Returns 
The modified
                [thread](/docs/api-reference/threads-v1/object)
                object matching the specified ID. 

**Example request**
```python
from openai import OpenAI
client = OpenAI()
my_updated_thread = client.beta.threads.update(
  "thread_abc123",
  metadata={
    "modified": "true",
    "user": "abc123"
  }
)
print(my_updated_thread)
```

**Response**
```python
{
  "id": "thread_abc123",
  "object": "thread",
  "created_at": 1699014083,
  "metadata": {
    "modified": "true",
    "user": "abc123"
  }
}
```
