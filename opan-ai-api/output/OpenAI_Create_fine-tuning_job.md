# [Create fine-tuning job](/docs/api-reference/fine-tuning/create)
post https://api.openai.com/v1/fine_tuning/jobs 
Creates a fine-tuning job which begins the process of creating a new
          model from a given dataset. 
Response includes details of the enqueued job including job status and
          the name of the fine-tuned models once complete. 
[Learn more about fine-tuning](/docs/guides/fine-tuning) 
## Request body 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| model | string | Required | The name of the model to fine-tune. You can select one of the                   supported models.| 
| training_file | string | Required | The ID of an uploaded file that contains training data.                    See                   upload file for                   how to upload a file.                                     Your dataset must be formatted as a JSONL file. Additionally,                   you must upload your file with the purpose                   fine-tune.                                     The contents of the file should differ depending on if the                   model uses the                   chat                   or                   completions                   format.                                     See the                   fine-tuning guide for                   more details.| 
| hyperparameters | object | Optional | The hyperparameters used for the fine-tuning job.| 
| suffix | string or null | Optional | A string of up to 18 characters that will be added to your                   fine-tuned model name.                                     For example, a suffix of "custom-model-name"                   would produce a model name like                   ft:gpt-3.5-turbo:openai:custom-model-name:7p4lURel.| 
| validation_file | string or null | Optional | The ID of an uploaded file that contains validation data.                    If you provide this file, the data is used to generate                   validation metrics periodically during fine-tuning. These                   metrics can be viewed in the fine-tuning results file. The                   same data should not be present in both train and validation                   files.                                     Your dataset must be formatted as a JSONL file. You must                   upload your file with the purpose fine-tune.                                     See the                   fine-tuning guide for                   more details.| 
| integrations | array or null | Optional | A list of integrations to enable for your fine-tuning job.| 
| seed | integer or null | Optional | The seed controls the reproducibility of the job. Passing in                   the same seed and job parameters should produce the same                   results, but may differ in rare cases. If a seed is not                   specified, one will be generated for you.| 
## Returns 
A
                [fine-tuning.job](/docs/api-reference/fine-tuning/object)
                object. 

**Example request**
```python
from openai import OpenAI
client = OpenAI()
client.fine_tuning.jobs.create(
  training_file="file-abc123",
  model="gpt-3.5-turbo"
)
```

**Response**
```python
{
  "object": "fine_tuning.job",
  "id": "ftjob-abc123",
  "model": "gpt-3.5-turbo-0125",
  "created_at": 1614807352,
  "fine_tuned_model": null,
  "organization_id": "org-123",
  "result_files": [],
  "status": "queued",
  "validation_file": null,
  "training_file": "file-abc123",
}
```
