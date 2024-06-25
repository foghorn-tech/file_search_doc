# [Create thread Beta](/docs/api-reference/threads/createThread)
post https://api.openai.com/v1/threads 
Create a thread. 
## Request body 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| messages | array | Optional | A list of                   messages to start                   the thread with.| 
| tool_resources | object or null | Optional | A set of resources that are made available to the assistant's                   tools in this thread. The resources are specific to the type                   of tool. For example, the code_interpreter tool                   requires a list of file IDs, while the                   file_search tool requires a list of vector store                   IDs.| 
| metadata | map | Optional | Set of 16 key-value pairs that can be attached to an object.                   This can be useful for storing additional information about                   the object in a structured format. Keys can be a maximum of 64                   characters long and values can be a maxium of 512 characters                   long.| 
## Returns 
A [thread](/docs/api-reference/threads) object. 

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
  "metadata": {},
  "tool_resources": {}
}
```
