# [Create vector store file batch Beta](/docs/api-reference/vector-stores-file-batches/createBatch)
post https://api.openai.com/v1/vector_stores/{vector_store_id}/file_batches 
Create a vector store file batch. 
## Path parameters 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| vector_store_id | string | Required | The ID of the vector store for which to create a File Batch.| 
## Request body 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| file_ids | array | Required | A list of File IDs                   that the vector store should use. Useful for tools like                   file_search that can access files.| 
| chunking_strategy | object | Optional | The chunking strategy used to chunk the file(s). If not set,                   will use the auto strategy.| 
## Returns 
A
                [vector store file batch](/docs/api-reference/vector-stores-file-batches/batch-object)
                object. 

**Example request**
```python
from openai import OpenAI
client = OpenAI()
vector_store_file_batch = client.beta.vector_stores.file_batches.create(
  vector_store_id="vs_abc123",
  file_ids=["file-abc123", "file-abc456"]
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
