# [Create vector store Beta](/docs/api-reference/vector-stores/create)
post https://api.openai.com/v1/vector_stores 
Create a vector store. 
## Request body 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| file_ids | array | Optional | A list of File IDs                   that the vector store should use. Useful for tools like                   file_search that can access files.| 
| name | string | Optional | The name of the vector store.| 
| expires_after | object | Optional | The expiration policy for a vector store.| 
| chunking_strategy | object | Optional | The chunking strategy used to chunk the file(s). If not set,                   will use the auto strategy. Only applicable if                   file_ids is non-empty.| 
| metadata | map | Optional | Set of 16 key-value pairs that can be attached to an object.                   This can be useful for storing additional information about                   the object in a structured format. Keys can be a maximum of 64                   characters long and values can be a maxium of 512 characters                   long.| 
## Returns 
A
                [vector store](/docs/api-reference/vector-stores/object)
                object. 

**Example request**
```python
from openai import OpenAI
client = OpenAI()
vector_store = client.beta.vector_stores.create(
  name="Support FAQ"
)
print(vector_store)
```

**Response**
```python
{
  "id": "vs_abc123",
  "object": "vector_store",
  "created_at": 1699061776,
  "name": "Support FAQ",
  "bytes": 139920,
  "file_counts": {
    "in_progress": 0,
    "completed": 3,
    "failed": 0,
    "cancelled": 0,
    "total": 3
  }
}
```
