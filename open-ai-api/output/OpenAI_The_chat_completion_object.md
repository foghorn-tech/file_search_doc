# [The chat completion object](/docs/api-reference/chat/object)
Represents a chat completion response returned by model, based on the
          provided input. 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| id | string | Optional | A unique identifier for the chat completion.| 
| choices | array | Optional | A list of chat completion choices. Can be more than one if                 n is greater than 1.| 
| created | integer | Optional | The Unix timestamp (in seconds) of when the chat completion was                 created.| 
| model | string | Optional | The model used for the chat completion.| 
| service_tier | string or null | Optional | The service tier used for processing the request. This field is                 only included if the service_tier parameter is                 specified in the request.| 
| system_fingerprint | string | Optional | This fingerprint represents the backend configuration that the                 model runs with.                                 Can be used in conjunction with the seed request                 parameter to understand when backend changes have been made that                 might impact determinism.| 
| object | string | Optional | The object type, which is always chat.completion.| 
| usage | object | Optional | Usage statistics for the completion request.| 

**The chat completion object**
```python
{
  "id": "chatcmpl-123",
  "object": "chat.completion",
  "created": 1677652288,
  "model": "gpt-3.5-turbo-0125",
  "system_fingerprint": "fp_44709d6fcb",
  "choices": [{
    "index": 0,
    "message": {
      "role": "assistant",
      "content": "\n\nHello there, how may I assist you today?",
    },
    "logprobs": null,
    "finish_reason": "stop"
  }],
  "usage": {
    "prompt_tokens": 9,
    "completion_tokens": 12,
    "total_tokens": 21
  }
}
```
