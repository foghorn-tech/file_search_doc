# [Retrieve vector store file batch Beta](/docs/api-reference/vector-stores-file-batches/getBatch)
get https://api.openai.com/v1/vector_stores/{vector_store_id}/file_batches/{batch_id} 
Retrieves a vector store file batch. 
## Path parameters 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| vector_store_id | string | Required | The ID of the vector store that the file batch belongs to.| 
| batch_id | string | Required | The ID of the file batch being retrieved.| 
## Returns 
The
                [vector store file batch](/docs/api-reference/vector-stores-file-batches/batch-object)
                object. 

**Example request**
```python
from openai import OpenAI
client = OpenAI()
vector_store_file_batch = client.beta.vector_stores.file_batches.retrieve(
  vector_store_id="vs_abc123",
  batch_id="vsfb_abc123"
)
print(vector_store_file_batch)
```

**Response**
```python
{
  "id": "vsfb_abc123",
  "object": "vector_store.file_batch",
  "created_at": 1699061776,
  "vector_store_id": "vs_abc123",
  "status": "in_progress",
  "file_counts": {
    "in_progress": 1,
    "completed": 1,
    "failed": 0,
    "cancelled": 0,
    "total": 0,
  }
}
```
