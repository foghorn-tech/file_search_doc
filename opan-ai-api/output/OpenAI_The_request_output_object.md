# [The request output object](/docs/api-reference/batch/request-output)
The per-line object of the batch output and error files 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| id | string | Optional | | 
| custom_id | string | Optional | A developer-provided per-request id that will be used to match                 outputs to inputs.| 
| response | object or null | Optional | | 
| error | object or null | Optional | For requests that failed with a non-HTTP error, this will                 contain more information on the cause of the failure.| 

**The request output object**
```python
{"id": "batch_req_wnaDys", "custom_id": "request-2", "response": {"status_code": 200, "request_id": "req_c187b3", "body": {"id": "chatcmpl-9758Iw", "object": "chat.completion", "created": 1711475054, "model": "gpt-3.5-turbo", "choices": [{"index": 0, "message": {"role": "assistant", "content": "2 + 2 equals 4."}, "finish_reason": "stop"}], "usage": {"prompt_tokens": 24, "completion_tokens": 15, "total_tokens": 39}, "system_fingerprint": null}}, "error": null}
```
