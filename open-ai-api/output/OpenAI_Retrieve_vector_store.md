# [Retrieve vector store Beta](/docs/api-reference/vector-stores/retrieve)
get https://api.openai.com/v1/vector_stores/{vector_store_id} 
Retrieves a vector store. 
## Path parameters 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| vector_store_id | string | Required | The ID of the vector store to retrieve.| 
## Returns 
The
                [vector store](/docs/api-reference/vector-stores/object)
                object matching the specified ID. 

**Example request**
```python
from openai import OpenAI
client = OpenAI()
vector_store = client.beta.vector_stores.retrieve(
  vector_store_id="vs_abc123"
)
print(vector_store)
```

**Response**
```python
{
  "id": "vs_abc123",
  "object": "vector_store",
  "created_at": 1699061776
}
```
