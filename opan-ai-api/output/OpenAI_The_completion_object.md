# [The completion object Legacy](/docs/api-reference/completions/object)
Represents a completion response from the API. Note: both the streamed
          and non-streamed response objects share the same shape (unlike the
          chat endpoint). 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| id | string | Optional | A unique identifier for the completion.| 
| choices | array | Optional | The list of completion choices the model generated for the input                 prompt.| 
| created | integer | Optional | The Unix timestamp (in seconds) of when the completion was                 created.| 
| model | string | Optional | The model used for completion.| 
| system_fingerprint | string | Optional | This fingerprint represents the backend configuration that the                 model runs with.                                 Can be used in conjunction with the seed request                 parameter to understand when backend changes have been made that                 might impact determinism.| 
| object | string | Optional | The object type, which is always "text_completion"| 
| usage | object | Optional | Usage statistics for the completion request.| 

**The completion object**
```python
{
  "id": "cmpl-uqkvlQyYK7bGYrRHQ0eXlWi7",
  "object": "text_completion",
  "created": 1589478378,
  "model": "gpt-4-turbo",
  "choices": [
    {
      "text": "\n\nThis is indeed a test",
      "index": 0,
      "logprobs": null,
      "finish_reason": "length"
    }
  ],
  "usage": {
    "prompt_tokens": 5,
    "completion_tokens": 7,
    "total_tokens": 12
  }
}
```
