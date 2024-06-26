# [The run object (v1) Legacy](/docs/api-reference/runs-v1/object)
Represents an execution run on a
          [thread](/docs/api-reference/threads-v1). 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| id | string | Optional | The identifier, which can be referenced in API endpoints.| 
| object | string | Optional | The object type, which is always thread.run.| 
| created_at | integer | Optional | The Unix timestamp (in seconds) for when the run was created.| 
| thread_id | string | Optional | The ID of the                 thread that was                 executed on as a part of this run.| 
| assistant_id | string | Optional | The ID of the                 assistant used                 for execution of this run.| 
| status | string | Optional | The status of the run, which can be either queued,                 in_progress, requires_action,                 cancelling, cancelled,                 failed, completed, or                 expired.| 
| required_action | object or null | Optional | Details on the action required to continue the run. Will be                 null if no action is required.| 
| last_error | object or null | Optional | The last error associated with this run. Will be                 null if there are no errors.| 
| expires_at | integer or null | Optional | The Unix timestamp (in seconds) for when the run will expire.| 
| started_at | integer or null | Optional | The Unix timestamp (in seconds) for when the run was started.| 
| cancelled_at | integer or null | Optional | The Unix timestamp (in seconds) for when the run was cancelled.| 
| failed_at | integer or null | Optional | The Unix timestamp (in seconds) for when the run failed.| 
| completed_at | integer or null | Optional | The Unix timestamp (in seconds) for when the run was completed.| 
| incomplete_details | object or null | Optional | Details on why the run is incomplete. Will be                 null if the run is not incomplete.| 
| model | string | Optional | The model that the                 assistant used                 for this run.| 
| instructions | string | Optional | The instructions that the                 assistant used                 for this run.| 
| tools | array | Optional | The list of tools that the                 assistant used                 for this run.| 
| file_ids | array | Optional | The list of File IDs the                 assistant used                 for this run.| 
| metadata | map | Optional | Set of 16 key-value pairs that can be attached to an object.                 This can be useful for storing additional information about the                 object in a structured format. Keys can be a maximum of 64                 characters long and values can be a maxium of 512 characters                 long.| 
| usage |  | Optional | | 
| temperature | number or null | Optional | The sampling temperature used for this run. If not set, defaults                 to 1.| 
| top_p | number or null | Optional | The nucleus sampling value used for this run. If not set,                 defaults to 1.| 
| max_prompt_tokens | integer or null | Optional | The maximum number of prompt tokens specified to have been used                 over the course of the run.| 
| max_completion_tokens | integer or null | Optional | The maximum number of completion tokens specified to have been                 used over the course of the run.| 
| truncation_strategy | object | Optional | | 
| tool_choice | string or object | Optional | Controls which (if any) tool is called by the model.                 none means the model will not call any tools and                 instead generates a message. auto is the default                 value and means the model can pick between generating a message                 or calling a tool. Specifying a particular tool like                 {"type": "TOOL_TYPE"} or                 {"type": "function", "function": {"name":                   "my_function"}}                 forces the model to call that tool.| 
| response_format | string or object | Optional | Specifies the format that the model must output. Compatible with                 GPT-4o,                 GPT-4 Turbo,                 and all GPT-3.5 Turbo models since                 gpt-3.5-turbo-1106.                                 Setting to { "type": "json_object" } enables JSON                 mode, which guarantees the message the model generates is valid                 JSON.                 Important: when using JSON mode, you                 must also instruct the model to produce JSON                 yourself via a system or user message. Without this, the model                 may generate an unending stream of whitespace until the                 generation reaches the token limit, resulting in a long-running                 and seemingly "stuck" request. Also note that the message                 content may be partially cut off if                 finish_reason="length", which indicates the                 generation exceeded max_tokens or the conversation                 exceeded the max context length.| 

**The run object (v1)**
```python
{
  "id": "run_abc123",
  "object": "thread.run",
  "created_at": 1698107661,
  "assistant_id": "asst_abc123",
  "thread_id": "thread_abc123",
  "status": "completed",
  "started_at": 1699073476,
  "expires_at": null,
  "cancelled_at": null,
  "failed_at": null,
  "completed_at": 1699073498,
  "last_error": null,
  "model": "gpt-4-turbo",
  "instructions": null,
  "tools": [{"type": "retrieval"}, {"type": "code_interpreter"}],
  "file_ids": [],
  "metadata": {},
  "incomplete_details": null,
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
```
