# [List assistant files (v1) Legacy](/docs/api-reference/assistants-v1/listAssistantFiles)
get https://api.openai.com/v1/assistants/{assistant_id}/files 
Returns a list of assistant files. 
## Path parameters 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| assistant_id | string | Required | The ID of the assistant the file belongs to.| 
## Query parameters 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| limit | integer | Optional | A limit on the number of objects to be returned. Limit can                   range between 1 and 100, and the default is 20.| 
| order | string | Optional | Sort order by the created_at timestamp of the                   objects. asc for ascending order and                   desc for descending order.| 
| after | string | Optional | A cursor for use in pagination. after is an                   object ID that defines your place in the list. For instance,                   if you make a list request and receive 100 objects, ending                   with obj_foo, your subsequent call can include after=obj_foo                   in order to fetch the next page of the list.| 
| before | string | Optional | A cursor for use in pagination. before is an                   object ID that defines your place in the list. For instance,                   if you make a list request and receive 100 objects, ending                   with obj_foo, your subsequent call can include before=obj_foo                   in order to fetch the previous page of the list.| 
## Returns 
A list of
                [assistant file](/docs/api-reference/assistants-v1/file-object)
                objects. 

**Example request**
```python
from openai import OpenAI
client = OpenAI()
assistant_files = client.beta.assistants.files.list(
  assistant_id="asst_abc123"
)
print(assistant_files)
```

**Response**
```python
{
  "object": "list",
  "data": [
    {
      "id": "file-abc123",
      "object": "assistant.file",
      "created_at": 1699060412,
      "assistant_id": "asst_abc123"
    },
    {
      "id": "file-abc456",
      "object": "assistant.file",
      "created_at": 1699060412,
      "assistant_id": "asst_abc123"
    }
  ],
  "first_id": "file-abc123",
  "last_id": "file-abc456",
  "has_more": false
}
```
