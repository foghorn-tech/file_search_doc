# [The request input object](/docs/api-reference/batch/request-input)
The per-line object of the batch input file 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| custom_id | string | Optional | A developer-provided per-request id that will be used to match                 outputs to inputs. Must be unique for each request in a batch.| 
| method | string | Optional | The HTTP method to be used for the request. Currently only                 POST is supported.| 
| url | string | Optional | The OpenAI API relative URL to be used for the request.                 Currently /v1/chat/completions,                 /v1/embeddings, and                 /v1/completions are supported.| 

**The request input object**
```python
{"custom_id": "request-1", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "gpt-3.5-turbo", "messages": [{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "What is 2+2?"}]}}
```
