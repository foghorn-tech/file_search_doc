# [List vector store files in a batch Beta](/docs/api-reference/vector-stores-file-batches/listBatchFiles)
get https://api.openai.com/v1/vector_stores/{vector_store_id}/file_batches/{batch_id}/files 
Returns a list of vector store files in a batch. 
## Path parameters 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| vector_store_id | string | Required | The ID of the vector store that the files belong to.| 
| batch_id | string | Required | The ID of the file batch that the files belong to.| 
## Query parameters 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| limit | integer | Optional | A limit on the number of objects to be returned. Limit can                   range between 1 and 100, and the default is 20.| 
| order | string | Optional | Sort order by the created_at timestamp of the                   objects. asc for ascending order and                   desc for descending order.| 
| after | string | Optional | A cursor for use in pagination. after is an                   object ID that defines your place in the list. For instance,                   if you make a list request and receive 100 objects, ending                   with obj_foo, your subsequent call can include after=obj_foo                   in order to fetch the next page of the list.| 
| before | string | Optional | A cursor for use in pagination. before is an                   object ID that defines your place in the list. For instance,                   if you make a list request and receive 100 objects, ending                   with obj_foo, your subsequent call can include before=obj_foo                   in order to fetch the previous page of the list.| 
| filter | string | Optional | Filter by file status. One of in_progress,                   completed, failed,                   cancelled.| 
## Returns 
A list of
                [vector store file](/docs/api-reference/vector-stores-files/file-object)
                objects. 

**Example request**
```python
from openai import OpenAI
client = OpenAI()
vector_store_files = client.beta.vector_stores.file_batches.list_files(
  vector_store_id="vs_abc123",
  batch_id="vsfb_abc123"
)
print(vector_store_files)
```

**Response**
```python
{
  "object": "list",
  "data": [
    {
      "id": "file-abc123",
      "object": "vector_store.file",
      "created_at": 1699061776,
      "vector_store_id": "vs_abc123"
    },
    {
      "id": "file-abc456",
      "object": "vector_store.file",
      "created_at": 1699061776,
      "vector_store_id": "vs_abc123"
    }
  ],
  "first_id": "file-abc123",
  "last_id": "file-abc456",
  "has_more": false
}
```
