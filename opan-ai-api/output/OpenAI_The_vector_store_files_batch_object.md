# [The vector store files batch object Beta](/docs/api-reference/vector-stores-file-batches/batch-object)
A batch of files attached to a vector store. 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| id | string | Optional | The identifier, which can be referenced in API endpoints.| 
| object | string | Optional | The object type, which is always                 vector_store.file_batch.| 
| created_at | integer | Optional | The Unix timestamp (in seconds) for when the vector store files                 batch was created.| 
| vector_store_id | string | Optional | The ID of the                 vector store                 that the File is                 attached to.| 
| status | string | Optional | The status of the vector store files batch, which can be either                 in_progress, completed,                 cancelled or failed.| 
| file_counts | object | Optional | | 

**The vector store files batch object**
```python
{
  "id": "vsfb_123",
  "object": "vector_store.files_batch",
  "created_at": 1698107661,
  "vector_store_id": "vs_abc123",
  "status": "completed",
  "file_counts": {
    "in_progress": 0,
    "completed": 100,
    "failed": 0,
    "cancelled": 0,
    "total": 100
  }
}
```
