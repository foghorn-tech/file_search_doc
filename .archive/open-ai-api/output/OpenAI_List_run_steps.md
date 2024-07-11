# [List run steps Beta](/docs/api-reference/run-steps/listRunSteps)
get https://api.openai.com/v1/threads/{thread_id}/runs/{run_id}/steps 
Returns a list of run steps belonging to a run. 
## Path parameters 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| thread_id | string | Required | The ID of the thread the run and run steps belong to.| 
| run_id | string | Required | The ID of the run the run steps belong to.| 
## Query parameters 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| limit | integer | Optional | A limit on the number of objects to be returned. Limit can                   range between 1 and 100, and the default is 20.| 
| order | string | Optional | Sort order by the created_at timestamp of the                   objects. asc for ascending order and                   desc for descending order.| 
| after | string | Optional | A cursor for use in pagination. after is an                   object ID that defines your place in the list. For instance,                   if you make a list request and receive 100 objects, ending                   with obj_foo, your subsequent call can include after=obj_foo                   in order to fetch the next page of the list.| 
| before | string | Optional | A cursor for use in pagination. before is an                   object ID that defines your place in the list. For instance,                   if you make a list request and receive 100 objects, ending                   with obj_foo, your subsequent call can include before=obj_foo                   in order to fetch the previous page of the list.| 
## Returns 
A list of
                [run step](/docs/api-reference/runs/step-object)
                objects. 

**Example request**
```python
from openai import OpenAI
client = OpenAI()
run_steps = client.beta.threads.runs.steps.list(
    thread_id="thread_abc123",
    run_id="run_abc123"
)
print(run_steps)
```

**Response**
```python
{
  "object": "list",
  "data": [
    {
      "id": "step_abc123",
      "object": "thread.run.step",
      "created_at": 1699063291,
      "run_id": "run_abc123",
      "assistant_id": "asst_abc123",
      "thread_id": "thread_abc123",
      "type": "message_creation",
      "status": "completed",
      "cancelled_at": null,
      "completed_at": 1699063291,
      "expired_at": null,
      "failed_at": null,
      "last_error": null,
      "step_details": {
        "type": "message_creation",
        "message_creation": {
          "message_id": "msg_abc123"
        }
      },
      "usage": {
        "prompt_tokens": 123,
        "completion_tokens": 456,
        "total_tokens": 579
      }
    }
  ],
  "first_id": "step_abc123",
  "last_id": "step_abc456",
  "has_more": false
}
```
