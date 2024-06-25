# [List message files (v1) Legacy](/docs/api-reference/messages-v1/listMessageFiles)
get https://api.openai.com/v1/threads/{thread_id}/messages/{message_id}/files 
Returns a list of message files. 
## Path parameters 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| thread_id | string | Required | The ID of the thread that the message and files belong to.| 
| message_id | string | Required | The ID of the message that the files belongs to.| 
## Query parameters 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| limit | integer | Optional | A limit on the number of objects to be returned. Limit can                   range between 1 and 100, and the default is 20.| 
| order | string | Optional | Sort order by the created_at timestamp of the                   objects. asc for ascending order and                   desc for descending order.| 
| after | string | Optional | A cursor for use in pagination. after is an                   object ID that defines your place in the list. For instance,                   if you make a list request and receive 100 objects, ending                   with obj_foo, your subsequent call can include after=obj_foo                   in order to fetch the next page of the list.| 
| before | string | Optional | A cursor for use in pagination. before is an                   object ID that defines your place in the list. For instance,                   if you make a list request and receive 100 objects, ending                   with obj_foo, your subsequent call can include before=obj_foo                   in order to fetch the previous page of the list.| 
## Returns 
A list of
                [message file](/docs/api-reference/messages-v1/file-object)
                objects. 

**Example request**
```python
from openai import OpenAI
client = OpenAI()
message_files = client.beta.threads.messages.files.list(
  thread_id="thread_abc123",
  message_id="msg_abc123"
)
print(message_files)
```

**Response**
```python
{
  "object": "list",
  "data": [
    {
      "id": "file-abc123",
      "object": "thread.message.file",
      "created_at": 1699061776,
      "message_id": "msg_abc123"
    },
    {
      "id": "file-abc123",
      "object": "thread.message.file",
      "created_at": 1699061776,
      "message_id": "msg_abc123"
    }
  ],
  "first_id": "file-abc123",
  "last_id": "file-abc123",
  "has_more": false
}
```
