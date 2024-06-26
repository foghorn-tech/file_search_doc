# [List fine-tuning events](/docs/api-reference/fine-tuning/list-events)
get https://api.openai.com/v1/fine_tuning/jobs/{fine_tuning_job_id}/events 
Get status updates for a fine-tuning job. 
## Path parameters 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| fine_tuning_job_id | string | Required | The ID of the fine-tuning job to get events for.| 
## Query parameters 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| after | string | Optional | Identifier for the last event from the previous pagination                   request.| 
| limit | integer | Optional | Number of events to retrieve.| 
## Returns 
A list of fine-tuning event objects. 

**Example request**
```python
from openai import OpenAI
client = OpenAI()
client.fine_tuning.jobs.list_events(
  fine_tuning_job_id="ftjob-abc123",
  limit=2
)
```

**Response**
```python
{
  "object": "list",
  "data": [
    {
      "object": "fine_tuning.job.event",
      "id": "ft-event-ddTJfwuMVpfLXseO0Am0Gqjm",
      "created_at": 1692407401,
      "level": "info",
      "message": "Fine tuning job successfully completed",
      "data": null,
      "type": "message"
    },
    {
      "object": "fine_tuning.job.event",
      "id": "ft-event-tyiGuB72evQncpH87xe505Sv",
      "created_at": 1692407400,
      "level": "info",
      "message": "New fine-tuned model created: ft:gpt-3.5-turbo:openai::7p4lURel",
      "data": null,
      "type": "message"
    }
  ],
  "has_more": true
}
```
