# [Retrieve run step (v1) Legacy](/docs/api-reference/runs-v1/getRunStep)
get https://api.openai.com/v1/threads/{thread_id}/runs/{run_id}/steps/{step_id} 
Retrieves a run step. 
## Path parameters 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| thread_id | string | Required | The ID of the thread to which the run and run step belongs.| 
| run_id | string | Required | The ID of the run to which the run step belongs.| 
| step_id | string | Required | The ID of the run step to retrieve.| 
## Returns 
The
                [run step](/docs/api-reference/runs-v1/step-object)
                object matching the specified ID. 

**Example request**
```python
from openai import OpenAI
client = OpenAI()
run_step = client.beta.threads.runs.steps.retrieve(
    thread_id="thread_abc123",
    run_id="run_abc123",
    step_id="step_abc123"
)
print(run_step)
```

**Response**
```python
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
```
