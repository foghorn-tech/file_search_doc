# [Cancel fine-tuning](/docs/api-reference/fine-tuning/cancel)
post https://api.openai.com/v1/fine_tuning/jobs/{fine_tuning_job_id}/cancel 
Immediately cancel a fine-tune job. 
## Path parameters 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| fine_tuning_job_id | string | Required | The ID of the fine-tuning job to cancel.| 
## Returns 
The cancelled
                [fine-tuning](/docs/api-reference/fine-tuning/object)
                object. 

**Example request**
```python
from openai import OpenAI
client = OpenAI()
client.fine_tuning.jobs.cancel("ftjob-abc123")
```

**Response**
```python
{
  "object": "fine_tuning.job",
  "id": "ftjob-abc123",
  "model": "gpt-3.5-turbo-0125",
  "created_at": 1689376978,
  "fine_tuned_model": null,
  "organization_id": "org-123",
  "result_files": [],
  "hyperparameters": {
    "n_epochs":  "auto"
  },
  "status": "cancelled",
  "validation_file": "file-abc123",
  "training_file": "file-abc123"
}
```
