# [Create thread and run Beta](/docs/api-reference/runs/createThreadAndRun)
post https://api.openai.com/v1/threads/runs 
Create a thread and run it in one request. 
## Request body 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| assistant_id | string | Required | The ID of the                   assistant to use                   to execute this run.| 
| thread | object | Optional | | 
| model | string | Optional | The ID of the                   Model to be used to                   execute this run. If a value is provided here, it will                   override the model associated with the assistant. If not, the                   model associated with the assistant will be used.| 
| instructions | string or null | Optional | Override the default system message of the assistant. This is                   useful for modifying the behavior on a per-run basis.| 
| tools | array or null | Optional | Override the tools the assistant can use for this run. This is                   useful for modifying the behavior on a per-run basis.| 
| tool_resources | object or null | Optional | A set of resources that are used by the assistant's tools. The                   resources are specific to the type of tool. For example, the                   code_interpreter tool requires a list of file                   IDs, while the file_search tool requires a list                   of vector store IDs.| 
| metadata | map | Optional | Set of 16 key-value pairs that can be attached to an object.                   This can be useful for storing additional information about                   the object in a structured format. Keys can be a maximum of 64                   characters long and values can be a maxium of 512 characters                   long.| 
| temperature | number or null | Optional | What sampling temperature to use, between 0 and 2. Higher                   values like 0.8 will make the output more random, while lower                   values like 0.2 will make it more focused and deterministic.| 
| top_p | number or null | Optional | An alternative to sampling with temperature, called nucleus                   sampling, where the model considers the results of the tokens                   with top_p probability mass. So 0.1 means only the tokens                   comprising the top 10% probability mass are considered.                                     We generally recommend altering this or temperature but not                   both.| 
| stream | boolean or null | Optional | If true, returns a stream of events that happen                   during the Run as server-sent events, terminating when the Run                   enters a terminal state with a                   data: [DONE] message.| 
| max_prompt_tokens | integer or null | Optional | The maximum number of prompt tokens that may be used over the                   course of the run. The run will make a best effort to use only                   the number of prompt tokens specified, across multiple turns                   of the run. If the run exceeds the number of prompt tokens                   specified, the run will end with status                   incomplete. See                   incomplete_details for more info.| 
| max_completion_tokens | integer or null | Optional | The maximum number of completion tokens that may be used over                   the course of the run. The run will make a best effort to use                   only the number of completion tokens specified, across                   multiple turns of the run. If the run exceeds the number of                   completion tokens specified, the run will end with status                   incomplete. See                   incomplete_details for more info.| 
| truncation_strategy | object | Optional | Controls for how a thread will be truncated prior to the run.                   Use this to control the intial context window of the run.| 
| tool_choice | string or object | Optional | Controls which (if any) tool is called by the model.                   none means the model will not call any tools and                   instead generates a message. auto is the default                   value and means the model can pick between generating a                   message or calling one or more tools.                   required means the model must call one or more                   tools before responding to the user. Specifying a particular                   tool like {"type": "file_search"} or                   {"type": "function", "function": {"name":                     "my_function"}}                   forces the model to call that tool.| 
| parallel_tool_calls | boolean | Optional | Whether to enable                   parallel function calling                   during tool use.| 
| response_format | string or object | Optional | Specifies the format that the model must output. Compatible                   with GPT-4o,                   GPT-4 Turbo,                   and all GPT-3.5 Turbo models since                   gpt-3.5-turbo-1106.                                     Setting to { "type": "json_object" } enables JSON                   mode, which guarantees the message the model generates is                   valid JSON.                   Important: when using JSON mode, you                   must also instruct the model to produce JSON                   yourself via a system or user message. Without this, the model                   may generate an unending stream of whitespace until the                   generation reaches the token limit, resulting in a                   long-running and seemingly "stuck" request. Also note that the                   message content may be partially cut off if                   finish_reason="length", which indicates the                   generation exceeded max_tokens or the                   conversation exceeded the max context length.| 
## Returns 
A [run](/docs/api-reference/runs/object) object. 

**Example request**
```python
from openai import OpenAI
client = OpenAI()
run = client.beta.threads.create_and_run(
  assistant_id="asst_abc123",
  thread={
    "messages": [
      {"role": "user", "content": "Explain deep learning to a 5 year old."}
    ]
  }
)
print(run)
```

**Response**
```python
{
  "id": "run_abc123",
  "object": "thread.run",
  "created_at": 1699076792,
  "assistant_id": "asst_abc123",
  "thread_id": "thread_abc123",
  "status": "queued",
  "started_at": null,
  "expires_at": 1699077392,
  "cancelled_at": null,
  "failed_at": null,
  "completed_at": null,
  "required_action": null,
  "last_error": null,
  "model": "gpt-4-turbo",
  "instructions": "You are a helpful assistant.",
  "tools": [],
  "tool_resources": {},
  "metadata": {},
  "temperature": 1.0,
  "top_p": 1.0,
  "max_completion_tokens": null,
  "max_prompt_tokens": null,
  "truncation_strategy": {
    "type": "auto",
    "last_messages": null
  },
  "incomplete_details": null,
  "usage": null,
  "response_format": "auto",
  "tool_choice": "auto",
  "parallel_tool_calls": true
}
```
