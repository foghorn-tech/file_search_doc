# [List runs (v1) Legacy](/docs/api-reference/runs-v1/listRuns)
get https://api.openai.com/v1/threads/{thread_id}/runs 
Returns a list of runs belonging to a thread. 
## Path parameters 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| thread_id | string | Required | The ID of the thread the run belongs to.| 
## Query parameters 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| limit | integer | Optional | A limit on the number of objects to be returned. Limit can                   range between 1 and 100, and the default is 20.| 
| order | string | Optional | Sort order by the created_at timestamp of the                   objects. asc for ascending order and                   desc for descending order.| 
| after | string | Optional | A cursor for use in pagination. after is an                   object ID that defines your place in the list. For instance,                   if you make a list request and receive 100 objects, ending                   with obj_foo, your subsequent call can include after=obj_foo                   in order to fetch the next page of the list.| 
| before | string | Optional | A cursor for use in pagination. before is an                   object ID that defines your place in the list. For instance,                   if you make a list request and receive 100 objects, ending                   with obj_foo, your subsequent call can include before=obj_foo                   in order to fetch the previous page of the list.| 
## Returns 
A list of
                [run](/docs/api-reference/runs-v1/object) objects. 

**Example request**
```python
from openai import OpenAI
client = OpenAI()
runs = client.beta.threads.runs.list(
  "thread_abc123"
)
print(runs)
```

**Response**
```python
{
  "object": "list",
  "data": [
    {
      "id": "run_abc123",
      "object": "thread.run",
      "created_at": 1699075072,
      "assistant_id": "asst_abc123",
      "thread_id": "thread_abc123",
      "status": "completed",
      "started_at": 1699075072,
      "expires_at": null,
      "cancelled_at": null,
      "failed_at": null,
      "completed_at": 1699075073,
      "last_error": null,
      "model": "gpt-4-turbo",
      "instructions": null,
      "incomplete_details": null,
      "tools": [
        {
          "type": "code_interpreter"
        }
      ],
      "file_ids": [
        "file-abc123",
        "file-abc456"
      ],
      "metadata": {},
      "usage": {
        "prompt_tokens": 123,
        "completion_tokens": 456,
        "total_tokens": 579
      },
      "temperature": 1.0,
      "top_p": 1.0,
      "max_prompt_tokens": 1000,
      "max_completion_tokens": 1000,
      "truncation_strategy": {
        "type": "auto",
        "last_messages": null
      },
      "response_format": "auto",
      "tool_choice": "auto"
    },
    {
      "id": "run_abc456",
      "object": "thread.run",
      "created_at": 1699063290,
      "assistant_id": "asst_abc123",
      "thread_id": "thread_abc123",
      "status": "completed",
      "started_at": 1699063290,
      "expires_at": null,
      "cancelled_at": null,
      "failed_at": null,
      "completed_at": 1699063291,
      "last_error": null,
      "model": "gpt-4-turbo",
      "instructions": null,
      "incomplete_details": null,
      "tools": [
        {
          "type": "code_interpreter"
        }
      ],
      "file_ids": [
        "file-abc123",
        "file-abc456"
      ],
      "metadata": {},
      "usage": {
        "prompt_tokens": 123,
        "completion_tokens": 456,
        "total_tokens": 579
      },
      "temperature": 1.0,
      "top_p": 1.0,
      "max_prompt_tokens": 1000,
      "max_completion_tokens": 1000,
      "truncation_strategy": {
        "type": "auto",
        "last_messages": null
      },
      "response_format": "auto",
      "tool_choice": "auto"
    }
  ],
  "first_id": "run_abc123",
  "last_id": "run_abc456",
  "has_more": false
}
```
