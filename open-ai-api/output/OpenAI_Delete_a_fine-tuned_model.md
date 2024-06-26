# [Delete a fine-tuned model](/docs/api-reference/models/delete)
delete https://api.openai.com/v1/models/{model} 
Delete a fine-tuned model. You must have the Owner role in your
          organization to delete a model. 
## Path parameters 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| model | string | Required | The model to delete| 
## Returns 
Deletion status. 

**Example request**
```python
from openai import OpenAI
client = OpenAI()
client.models.delete("ft:gpt-3.5-turbo:acemeco:suffix:abc123")
```

**Response**
```python
{
  "id": "ft:gpt-3.5-turbo:acemeco:suffix:abc123",
  "object": "model",
  "deleted": true
}
```
