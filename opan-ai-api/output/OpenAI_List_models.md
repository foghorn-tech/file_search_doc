# [List models](/docs/api-reference/models/list)
get https://api.openai.com/v1/models 
Lists the currently available models, and provides basic information
          about each one such as the owner and availability. 
## Returns 
A list of
                [model](/docs/api-reference/models/object) objects. 

**Example request**
```python
from openai import OpenAI
client = OpenAI()
client.models.list()
```

**Response**
```python
{
  "object": "list",
  "data": [
    {
      "id": "model-id-0",
      "object": "model",
      "created": 1686935002,
      "owned_by": "organization-owner"
    },
    {
      "id": "model-id-1",
      "object": "model",
      "created": 1686935002,
      "owned_by": "organization-owner",
    },
    {
      "id": "model-id-2",
      "object": "model",
      "created": 1686935002,
      "owned_by": "openai"
    },
  ],
  "object": "list"
}
```
