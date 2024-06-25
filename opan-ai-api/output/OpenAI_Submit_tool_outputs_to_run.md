# [Submit tool outputs to run Beta](/docs/api-reference/runs/submitToolOutputs)
post https://api.openai.com/v1/threads/{thread_id}/runs/{run_id}/submit_tool_outputs 
When a run has the status: "requires_action" and
          required_action.type is submit_tool_outputs,
          this endpoint can be used to submit the outputs from the tool calls
          once they're all completed. All outputs must be submitted in a single
          request. 
## Path parameters 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| thread_id | string | Required | The ID of the                   thread to which this                   run belongs.| 
| run_id | string | Required | The ID of the run that requires the tool output submission.| 
## Request body 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| tool_outputs | array | Required | A list of tools for which the outputs are being submitted.| 
| stream | boolean or null | Optional | If true, returns a stream of events that happen                   during the Run as server-sent events, terminating when the Run                   enters a terminal state with a                   data: [DONE] message.| 
## Returns 
The modified
                [run](/docs/api-reference/runs/object) object
                matching the specified ID. 

**Example request**
```python
from openai import OpenAI
client = OpenAI()
run = client.beta.threads.runs.submit_tool_outputs(
  thread_id="thread_123",
  run_id="run_123",
  tool_outputs=[
    {
      "tool_call_id": "call_001",
      "output": "70 degrees and sunny."
    }
  ]
)
print(run)
```

**Response**
```python
{
  "id": "run_123",
  "object": "thread.run",
  "created_at": 1699075592,
  "assistant_id": "asst_123",
  "thread_id": "thread_123",
  "status": "queued",
  "started_at": 1699075592,
  "expires_at": 1699076192,
  "cancelled_at": null,
  "failed_at": null,
  "completed_at": null,
  "last_error": null,
  "model": "gpt-4-turbo",
  "instructions": null,
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "get_current_weather",
        "description": "Get the current weather in a given location",
        "parameters": {
          "type": "object",
          "properties": {
            "location": {
              "type": "string",
              "description": "The city and state, e.g. San Francisco, CA"
            },
            "unit": {
              "type": "string",
              "enum": ["celsius", "fahrenheit"]
            }
          },
          "required": ["location"]
        }
      }
    }
  ],
  "metadata": {},
  "usage": null,
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
