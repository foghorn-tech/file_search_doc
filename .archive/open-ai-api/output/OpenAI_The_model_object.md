# [The model object](/docs/api-reference/models/object)
Describes an OpenAI model offering that can be used with the API. 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| id | string | Optional | The model identifier, which can be referenced in the API                 endpoints.| 
| created | integer | Optional | The Unix timestamp (in seconds) when the model was created.| 
| object | string | Optional | The object type, which is always "model".| 
| owned_by | string | Optional | The organization that owns the model.| 

**The model object**
```python
{
  "id": "davinci",
  "object": "model",
  "created": 1686935002,
  "owned_by": "openai"
}
```
