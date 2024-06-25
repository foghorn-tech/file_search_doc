# [The fine-tuning job object](/docs/api-reference/fine-tuning/object)
The fine_tuning.job object represents a fine-tuning job
          that has been created through the API. 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| id | string | Optional | The object identifier, which can be referenced in the API                 endpoints.| 
| created_at | integer | Optional | The Unix timestamp (in seconds) for when the fine-tuning job was                 created.| 
| error | object or null | Optional | For fine-tuning jobs that have failed, this will                 contain more information on the cause of the failure.| 
| fine_tuned_model | string or null | Optional | The name of the fine-tuned model that is being created. The                 value will be null if the fine-tuning job is still running.| 
| finished_at | integer or null | Optional | The Unix timestamp (in seconds) for when the fine-tuning job was                 finished. The value will be null if the fine-tuning job is still                 running.| 
| hyperparameters | object | Optional | The hyperparameters used for the fine-tuning job. See the                 fine-tuning guide for                 more details.| 
| model | string | Optional | The base model that is being fine-tuned.| 
| object | string | Optional | The object type, which is always "fine_tuning.job".| 
| organization_id | string | Optional | The organization that owns the fine-tuning job.| 
| result_files | array | Optional | The compiled results file ID(s) for the fine-tuning job. You can                 retrieve the results with the                 Files API.| 
| status | string | Optional | The current status of the fine-tuning job, which can be either                 validating_files, queued,                 running, succeeded,                 failed, or cancelled.| 
| trained_tokens | integer or null | Optional | The total number of billable tokens processed by this                 fine-tuning job. The value will be null if the fine-tuning job                 is still running.| 
| training_file | string | Optional | The file ID used for training. You can retrieve the training                 data with the                 Files API.| 
| validation_file | string or null | Optional | The file ID used for validation. You can retrieve the validation                 results with the                 Files API.| 
| integrations | array or null | Optional | A list of integrations to enable for this fine-tuning job.| 
| seed | integer | Optional | The seed used for the fine-tuning job.| 
| estimated_finish | integer or null | Optional | The Unix timestamp (in seconds) for when the fine-tuning job is                 estimated to finish. The value will be null if the fine-tuning                 job is not running.| 

**The fine-tuning job object**
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
