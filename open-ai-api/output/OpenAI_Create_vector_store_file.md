# [Create vector store file Beta](/docs/api-reference/vector-stores-files/createFile)
post https://api.openai.com/v1/vector_stores/{vector_store_id}/files 
Create a [vector store](/docs/api-reference/vector-stores/object) file by attaching a
          [File](/docs/api-reference/files) to a
          [vector store](/docs/api-reference/vector-stores/object). 
## Path parameters 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| vector_store_id | string | Required | The ID of the vector store for which to create a File.| 
## Request body 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| file_id | string | Required | A File ID that the                   vector store should use. Useful for tools like                   file_search that can access files.| 
| chunking_strategy | object | Optional | The chunking strategy used to chunk the file(s). If not set,                   will use the auto strategy.| 
## Returns 
A
                [vector store file](/docs/api-reference/vector-stores-files/file-object)
                object. 

**Example request**
```python
from openai import OpenAI
client = OpenAI()
vector_store_file = client.beta.vector_stores.files.create(
  vector_store_id="vs_abc123",
  file_id="file-abc123"
)
print(vector_store_file)
```

**Response**
```python
{
  "id": "file-abc123",
  "object": "vector_store.file",
  "created_at": 1699061776,
  "usage_bytes": 1234,
  "vector_store_id": "vs_abcd",
  "status": "completed",
  "last_error": null
}
```
