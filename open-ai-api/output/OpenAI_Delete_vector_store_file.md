# [Delete vector store file Beta](/docs/api-reference/vector-stores-files/deleteFile)
delete https://api.openai.com/v1/vector_stores/{vector_store_id}/files/{file_id} 
Delete a vector store file. This will remove the file from the vector
          store but the file itself will not be deleted. To delete the file, use
          the
          [delete file](/docs/api-reference/files/delete) endpoint. 
## Path parameters 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| vector_store_id | string | Required | The ID of the vector store that the file belongs to.| 
| file_id | string | Required | The ID of the file to delete.| 
## Returns 
Deletion status 

**Example request**
```python
from openai import OpenAI
client = OpenAI()
deleted_vector_store_file = client.beta.vector_stores.files.delete(
    vector_store_id="vs_abc123",
    file_id="file-abc123"
)
print(deleted_vector_store_file)
```

**Response**
```python
{
  id: "file-abc123",
  object: "vector_store.file.deleted",
  deleted: true
}
```
