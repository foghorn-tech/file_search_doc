# [Retrieve assistant Beta](/docs/api-reference/assistants/getAssistant)
get https://api.openai.com/v1/assistants/{assistant_id} 
Retrieves an assistant. 
## Path parameters 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| assistant_id | string | Required | The ID of the assistant to retrieve.| 
## Returns 
The
                [assistant](/docs/api-reference/assistants/object)
                object matching the specified ID. 

**Example request**
```python
from openai import OpenAI
client = OpenAI()
my_assistant = client.beta.assistants.retrieve("asst_abc123")
print(my_assistant)
```

**Response**
```python
{
  "id": "asst_abc123",
  "object": "assistant",
  "created_at": 1699009709,
  "name": "HR Helper",
  "description": null,
  "model": "gpt-4-turbo",
  "instructions": "You are an HR bot, and you have access to files to answer employee questions about company policies.",
  "tools": [
    {
      "type": "file_search"
    }
  ],
  "metadata": {},
  "top_p": 1.0,
  "temperature": 1.0,
  "response_format": "auto"
}
```
