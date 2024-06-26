# [Retrieve fine-tuning job](/docs/api-reference/fine-tuning/retrieve)
get https://api.openai.com/v1/fine_tuning/jobs/{fine_tuning_job_id} 
Get info about a fine-tuning job. 
[Learn more about fine-tuning](/docs/guides/fine-tuning) 
## Path parameters 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| fine_tuning_job_id | string | Required | The ID of the fine-tuning job.| 
## Returns 
The
                [fine-tuning](/docs/api-reference/fine-tuning/object)
                object with the given ID. 

**Example request**
```python
from openai import OpenAI
client = OpenAI()
client.fine_tuning.jobs.retrieve("ftjob-abc123")
```

**Response**
```python
{
  "object": "fine_tuning.job",
  "id": "ftjob-abc123",
  "model": "davinci-002",
  "created_at": 1692661014,
  "finished_at": 1692661190,
  "fine_tuned_model": "ft:davinci-002:my-org:custom_suffix:7q8mpxmy",
  "organization_id": "org-123",
  "result_files": [
      "file-abc123"
  ],
  "status": "succeeded",
  "validation_file": null,
  "training_file": "file-abc123",
  "hyperparameters": {
      "n_epochs": 4,
      "batch_size": 1,
      "learning_rate_multiplier": 1.0
  },
  "trained_tokens": 5768,
  "integrations": [],
  "seed": 0,
  "estimated_finish": 0
}
```
