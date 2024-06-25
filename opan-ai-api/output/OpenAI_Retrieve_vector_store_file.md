# [Retrieve vector store file Beta](/docs/api-reference/vector-stores-files/getFile)
get https://api.openai.com/v1/vector_stores/{vector_store_id}/files/{file_id} 
Retrieves a vector store file. 
## Path parameters 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| vector_store_id | string | Required | The ID of the vector store that the file belongs to.| 
| file_id | string | Required | The ID of the file being retrieved.| 
## Returns 
The
                [vector store file](/docs/api-reference/vector-stores-files/file-object)
                object. 

**Example request**
```python
from openai import OpenAI
client = OpenAI()
vector_store_file = client.beta.vector_stores.files.retrieve(
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
  "vector_store_id": "vs_abcd",
  "status": "completed",
  "last_error": null
}
```
