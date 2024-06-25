# [List fine-tuning jobs](/docs/api-reference/fine-tuning/list)
get https://api.openai.com/v1/fine_tuning/jobs 
List your organization's fine-tuning jobs 
## Query parameters 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| after | string | Optional | Identifier for the last job from the previous pagination                   request.| 
| limit | integer | Optional | Number of fine-tuning jobs to retrieve.| 
## Returns 
A list of paginated
                [fine-tuning job](/docs/api-reference/fine-tuning/object)
                objects. 

**Example request**
```python
from openai import OpenAI
client = OpenAI()
client.fine_tuning.jobs.list()
```

**Response**
```python
{
  "object": "list",
  "data": [
    {
      "object": "fine_tuning.job.event",
      "id": "ft-event-TjX0lMfOniCZX64t9PUQT5hn",
      "created_at": 1689813489,
      "level": "warn",
      "message": "Fine tuning process stopping due to job cancellation",
      "data": null,
      "type": "message"
    },
    { ... },
    { ... }
  ], "has_more": true
}
```
