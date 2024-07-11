# [The fine-tuning job checkpoint object](/docs/api-reference/fine-tuning/checkpoint-object)
The fine_tuning.job.checkpoint object represents a model
          checkpoint for a fine-tuning job that is ready to use. 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| id | string | Optional | The checkpoint identifier, which can be referenced in the API                 endpoints.| 
| created_at | integer | Optional | The Unix timestamp (in seconds) for when the checkpoint was                 created.| 
| fine_tuned_model_checkpoint | string | Optional | The name of the fine-tuned checkpoint model that is created.| 
| step_number | integer | Optional | The step number that the checkpoint was created at.| 
| metrics | object | Optional | Metrics at the step number during the fine-tuning job.| 
| fine_tuning_job_id | string | Optional | The name of the fine-tuning job that this checkpoint was created                 from.| 
| object | string | Optional | The object type, which is always "fine_tuning.job.checkpoint".| 

**The fine-tuning job checkpoint object**
```python
{
  "object": "fine_tuning.job.checkpoint",
  "id": "ftckpt_qtZ5Gyk4BLq1SfLFWp3RtO3P",
  "created_at": 1712211699,
  "fine_tuned_model_checkpoint": "ft:gpt-3.5-turbo-0125:my-org:custom_suffix:9ABel2dg:ckpt-step-88",
  "fine_tuning_job_id": "ftjob-fpbNQ3H1GrMehXRf8cO97xTN",
  "metrics": {
    "step": 88,
    "train_loss": 0.478,
    "train_mean_token_accuracy": 0.924,
    "valid_loss": 10.112,
    "valid_mean_token_accuracy": 0.145,
    "full_valid_loss": 0.567,
    "full_valid_mean_token_accuracy": 0.944
  },
  "step_number": 88
}
```
