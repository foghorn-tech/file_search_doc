# [Delete vector store Beta](/docs/api-reference/vector-stores/delete)
delete https://api.openai.com/v1/vector_stores/{vector_store_id} 
Delete a vector store. 
## Path parameters 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| vector_store_id | string | Required | The ID of the vector store to delete.| 
## Returns 
Deletion status 

**Example request**
```python
from openai import OpenAI
client = OpenAI()
deleted_vector_store = client.beta.vector_stores.delete(
  vector_store_id="vs_abc123"
)
print(deleted_vector_store)
```

**Response**
```python
{
  id: "vs_abc123",
  object: "vector_store.deleted",
  deleted: true
}
```
