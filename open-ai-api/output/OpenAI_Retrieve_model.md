# [Retrieve model](/docs/api-reference/models/retrieve)
get https://api.openai.com/v1/models/{model} 
Retrieves a model instance, providing basic information about the
          model such as the owner and permissioning. 
## Path parameters 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| model | string | Required | The ID of the model to use for this request| 
## Returns 
The [model](/docs/api-reference/models/object) object
                matching the specified ID. 

**Example request**
```python
from openai import OpenAI
client = OpenAI()
client.models.retrieve("gpt-3.5-turbo-instruct")
```

**Response**
```python
{
  "id": "gpt-3.5-turbo-instruct",
  "object": "model",
  "created": 1686935002,
  "owned_by": "openai"
}
```
