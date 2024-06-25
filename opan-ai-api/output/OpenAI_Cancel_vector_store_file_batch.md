# [Cancel vector store file batch Beta](/docs/api-reference/vector-stores-file-batches/cancelBatch)
post https://api.openai.com/v1/vector_stores/{vector_store_id}/file_batches/{batch_id}/cancel 
Cancel a vector store file batch. This attempts to cancel the
          processing of files in this batch as soon as possible. 
## Path parameters 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| vector_store_id | string | Required | The ID of the vector store that the file batch belongs to.| 
| batch_id | string | Required | The ID of the file batch to cancel.| 
## Returns 
The modified vector store file batch object. 

**Example request**
```python
from openai import OpenAI
client = OpenAI()
deleted_vector_store_file_batch = client.beta.vector_stores.file_batches.cancel(
    vector_store_id="vs_abc123",
    file_batch_id="vsfb_abc123"
)
print(deleted_vector_store_file_batch)
```

**Response**
```python
{
  "id": "vsfb_abc123",
  "object": "vector_store.file_batch",
  "created_at": 1699061776,
  "vector_store_id": "vs_abc123",
  "status": "cancelling",
  "file_counts": {
    "in_progress": 12,
    "completed": 3,
    "failed": 0,
    "cancelled": 0,
    "total": 15,
  }
}
```
