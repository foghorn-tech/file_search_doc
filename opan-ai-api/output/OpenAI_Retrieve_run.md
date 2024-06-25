# [Retrieve run Beta](/docs/api-reference/runs/getRun)
get https://api.openai.com/v1/threads/{thread_id}/runs/{run_id} 
Retrieves a run. 
## Path parameters 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| thread_id | string | Required | The ID of the                   thread that was run.| 
| run_id | string | Required | The ID of the run to retrieve.| 
## Returns 
The [run](/docs/api-reference/runs/object) object
                matching the specified ID. 

**Example request**
```python
from openai import OpenAI
client = OpenAI()
run = client.beta.threads.runs.retrieve(
  thread_id="thread_abc123",
  run_id="run_abc123"
)
print(run)
```

**Response**
```python
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
  "tool_choice": "auto",
  "parallel_tool_calls": true
}
```
