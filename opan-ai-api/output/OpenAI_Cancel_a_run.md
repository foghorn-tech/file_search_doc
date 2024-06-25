# [Cancel a run Beta](/docs/api-reference/runs/cancelRun)
post https://api.openai.com/v1/threads/{thread_id}/runs/{run_id}/cancel 
Cancels a run that is in_progress. 
## Path parameters 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| thread_id | string | Required | The ID of the thread to which this run belongs.| 
| run_id | string | Required | The ID of the run to cancel.| 
## Returns 
The modified
                [run](/docs/api-reference/runs/object) object
                matching the specified ID. 

**Example request**
```python
from openai import OpenAI
client = OpenAI()
run = client.beta.threads.runs.cancel(
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
  "created_at": 1699076126,
  "assistant_id": "asst_abc123",
  "thread_id": "thread_abc123",
  "status": "cancelling",
  "started_at": 1699076126,
  "expires_at": 1699076726,
  "cancelled_at": null,
  "failed_at": null,
  "completed_at": null,
  "last_error": null,
  "model": "gpt-4-turbo",
  "instructions": "You summarize books.",
  "tools": [
    {
      "type": "file_search"
    }
  ],
  "tool_resources": {
    "file_search": {
      "vector_store_ids": ["vs_123"]
    }
  },
  "metadata": {},
  "usage": null,
  "temperature": 1.0,
  "top_p": 1.0,
  "response_format": "auto",
  "tool_choice": "auto",
  "parallel_tool_calls": true
}
```
