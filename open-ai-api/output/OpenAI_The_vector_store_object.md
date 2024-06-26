# [The vector store object Beta](/docs/api-reference/vector-stores/object)
A vector store is a collection of processed files can be used by the
          file_search tool. 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| id | string | Optional | The identifier, which can be referenced in API endpoints.| 
| object | string | Optional | The object type, which is always vector_store.| 
| created_at | integer | Optional | The Unix timestamp (in seconds) for when the vector store was                 created.| 
| name | string | Optional | The name of the vector store.| 
| usage_bytes | integer | Optional | The total number of bytes used by the files in the vector store.| 
| file_counts | object | Optional | | 
| status | string | Optional | The status of the vector store, which can be either                 expired, in_progress, or                 completed. A status of                 completed indicates that the vector store is ready                 for use.| 
| expires_after | object | Optional | The expiration policy for a vector store.| 
| expires_at | integer or null | Optional | The Unix timestamp (in seconds) for when the vector store will                 expire.| 
| last_active_at | integer or null | Optional | The Unix timestamp (in seconds) for when the vector store was                 last active.| 
| metadata | map | Optional | Set of 16 key-value pairs that can be attached to an object.                 This can be useful for storing additional information about the                 object in a structured format. Keys can be a maximum of 64                 characters long and values can be a maxium of 512 characters                 long.| 

**The vector store object**
```python
{
  "id": "vs_123",
  "object": "vector_store",
  "created_at": 1698107661,
  "usage_bytes": 123456,
  "last_active_at": 1698107661,
  "name": "my_vector_store",
  "status": "completed",
  "file_counts": {
    "in_progress": 0,
    "completed": 100,
    "cancelled": 0,
    "failed": 0,
    "total": 100
  },
  "metadata": {},
  "last_used_at": 1698107661
}
```
