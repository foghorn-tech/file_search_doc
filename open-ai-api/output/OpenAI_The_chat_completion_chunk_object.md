# [The chat completion chunk object](/docs/api-reference/chat/streaming)
Represents a streamed chunk of a chat completion response returned by
          model, based on the provided input. 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| id | string | Optional | A unique identifier for the chat completion. Each chunk has the                 same ID.| 
| choices | array | Optional | A list of chat completion choices. Can contain more than one                 elements if n is greater than 1. Can also be empty                 for the last chunk if you set                 stream_options: {"include_usage": true}.| 
| created | integer | Optional | The Unix timestamp (in seconds) of when the chat completion was                 created. Each chunk has the same timestamp.| 
| model | string | Optional | The model to generate the completion.| 
| service_tier | string or null | Optional | The service tier used for processing the request. This field is                 only included if the service_tier parameter is                 specified in the request.| 
| system_fingerprint | string | Optional | This fingerprint represents the backend configuration that the                 model runs with. Can be used in conjunction with the                 seed request parameter to understand when backend                 changes have been made that might impact determinism.| 
| object | string | Optional | The object type, which is always                 chat.completion.chunk.| 
| usage | object | Optional | An optional field that will only be present when you set                 stream_options: {"include_usage": true} in your                 request. When present, it contains a null value except for the                 last chunk which contains the token usage statistics for the                 entire request.| 

**The chat completion chunk object**
```python
{"id":"chatcmpl-123","object":"chat.completion.chunk","created":1694268190,"model":"gpt-3.5-turbo-0125", "system_fingerprint": "fp_44709d6fcb", "choices":[{"index":0,"delta":{"role":"assistant","content":""},"logprobs":null,"finish_reason":null}]}
{"id":"chatcmpl-123","object":"chat.completion.chunk","created":1694268190,"model":"gpt-3.5-turbo-0125", "system_fingerprint": "fp_44709d6fcb", "choices":[{"index":0,"delta":{"content":"Hello"},"logprobs":null,"finish_reason":null}]}
....
{"id":"chatcmpl-123","object":"chat.completion.chunk","created":1694268190,"model":"gpt-3.5-turbo-0125", "system_fingerprint": "fp_44709d6fcb", "choices":[{"index":0,"delta":{},"logprobs":null,"finish_reason":"stop"}]}
```
