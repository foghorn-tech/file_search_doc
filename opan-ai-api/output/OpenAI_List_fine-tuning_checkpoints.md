# [List fine-tuning checkpoints](/docs/api-reference/fine-tuning/list-checkpoints)
get https://api.openai.com/v1/fine_tuning/jobs/{fine_tuning_job_id}/checkpoints 
List checkpoints for a fine-tuning job. 
## Path parameters 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| fine_tuning_job_id | string | Required | The ID of the fine-tuning job to get checkpoints for.| 
## Query parameters 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| after | string | Optional | Identifier for the last checkpoint ID from the previous                   pagination request.| 
| limit | integer | Optional | Number of checkpoints to retrieve.| 
## Returns 
A list of fine-tuning
                [checkpoint objects](/docs/api-reference/fine-tuning/checkpoint-object)
                for a fine-tuning job. 

**Example request**
```python
curl https://api.openai.com/v1/fine_tuning/jobs/ftjob-abc123/checkpoints \
  -H "Authorization: Bearer $OPENAI_API_KEY"
```

**Response**
```python
{
  "object": "list"
  "data": [
    {
      "object": "fine_tuning.job.checkpoint",
      "id": "ftckpt_zc4Q7MP6XxulcVzj4MZdwsAB",
      "created_at": 1519129973,
      "fine_tuned_model_checkpoint": "ft:gpt-3.5-turbo-0125:my-org:custom-suffix:96olL566:ckpt-step-2000",
      "metrics": {
        "full_valid_loss": 0.134,
        "full_valid_mean_token_accuracy": 0.874
      },
      "fine_tuning_job_id": "ftjob-abc123",
      "step_number": 2000,
    },
    {
      "object": "fine_tuning.job.checkpoint",
      "id": "ftckpt_enQCFmOTGj3syEpYVhBRLTSy",
      "created_at": 1519129833,
      "fine_tuned_model_checkpoint": "ft:gpt-3.5-turbo-0125:my-org:custom-suffix:7q8mpxmy:ckpt-step-1000",
      "metrics": {
        "full_valid_loss": 0.167,
        "full_valid_mean_token_accuracy": 0.781
      },
      "fine_tuning_job_id": "ftjob-abc123",
      "step_number": 1000,
    },
  ],
  "first_id": "ftckpt_zc4Q7MP6XxulcVzj4MZdwsAB",
  "last_id": "ftckpt_enQCFmOTGj3syEpYVhBRLTSy",
  "has_more": true
}
```
