# [The fine-tuning job event object](/docs/api-reference/fine-tuning/event-object)
Fine-tuning job event object 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| id | string | Optional | | 
| created_at | integer | Optional | | 
| level | string | Optional | | 
| message | string | Optional | | 
| object | string | Optional | | 

**The fine-tuning job event object**
```python
{
  "object": "fine_tuning.job.event",
  "id": "ftevent-abc123"
  "created_at": 1677610602,
  "level": "info",
  "message": "Created fine-tuning job"
}
```
