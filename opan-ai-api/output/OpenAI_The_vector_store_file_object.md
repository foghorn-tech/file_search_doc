# [The vector store file object Beta](/docs/api-reference/vector-stores-files/file-object)
A list of files attached to a vector store. 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| id | string | Optional | The identifier, which can be referenced in API endpoints.| 
| object | string | Optional | The object type, which is always vector_store.file.| 
| usage_bytes | integer | Optional | The total vector store usage in bytes. Note that this may be                 different from the original file size.| 
| created_at | integer | Optional | The Unix timestamp (in seconds) for when the vector store file                 was created.| 
| vector_store_id | string | Optional | The ID of the                 vector store                 that the File is                 attached to.| 
| status | string | Optional | The status of the vector store file, which can be either                 in_progress, completed,                 cancelled, or failed. The status                 completed indicates that the vector store file is                 ready for use.| 
| last_error | object or null | Optional | The last error associated with this vector store file. Will be                 null if there are no errors.| 
| chunking_strategy | object | Optional | The strategy used to chunk the file.| 

**The vector store file object**
```python
{
  "id": "file-abc123",
  "object": "vector_store.file",
  "usage_bytes": 1234,
  "created_at": 1698107661,
  "vector_store_id": "vs_abc123",
  "status": "completed",
  "last_error": null,
  "chunking_strategy": {
    "type": "static",
    "static": {
      "max_chunk_size_tokens": 800,
      "chunk_overlap_tokens": 400
    }
  }
}
```
