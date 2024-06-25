# [Modify vector store Beta](/docs/api-reference/vector-stores/modify)
post https://api.openai.com/v1/vector_stores/{vector_store_id} 
Modifies a vector store. 
## Path parameters 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| vector_store_id | string | Required | The ID of the vector store to modify.| 
## Request body 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| name | string or null | Optional | The name of the vector store.| 
| expires_after | object | Optional | The expiration policy for a vector store.| 
| metadata | map | Optional | Set of 16 key-value pairs that can be attached to an object.                   This can be useful for storing additional information about                   the object in a structured format. Keys can be a maximum of 64                   characters long and values can be a maxium of 512 characters                   long.| 
## Returns 
The modified
                [vector store](/docs/api-reference/vector-stores/object)
                object. 

**Example request**
```python
from openai import OpenAI
client = OpenAI()
vector_store = client.beta.vector_stores.update(
  vector_store_id="vs_abc123",
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
