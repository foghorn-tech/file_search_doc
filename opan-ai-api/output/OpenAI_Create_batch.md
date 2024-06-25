# [Create batch](/docs/api-reference/batch/create)
post https://api.openai.com/v1/batches 
Creates and executes a batch from an uploaded file of requests 
## Request body 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| input_file_id | string | Required | The ID of an uploaded file that contains requests for the new                   batch.                                     See                   upload file for                   how to upload a file.                                     Your input file must be formatted as a                   JSONL file, and must be uploaded with the purpose batch.                   The file can contain up to 50,000 requests, and can be up to                   100 MB in size.| 
| endpoint | string | Required | The endpoint to be used for all requests in the batch.                   Currently /v1/chat/completions,                   /v1/embeddings, and                   /v1/completions are supported. Note that                   /v1/embeddings batches are also restricted to a                   maximum of 50,000 embedding inputs across all requests in the                   batch.| 
| completion_window | string | Required | The time frame within which the batch should be processed.                   Currently only 24h is supported.| 
| metadata | object or null | Optional | Optional custom metadata for the batch.| 
## Returns 
The created
                [Batch](/docs/api-reference/batch/object) object. 

**Example request**
```python
from openai import OpenAI
client = OpenAI()
client.batches.create(
  input_file_id="file-abc123",
  endpoint="/v1/chat/completions",
  completion_window="24h"
)
```

**Response**
```python
{
  "id": "batch_abc123",
  "object": "batch",
  "endpoint": "/v1/chat/completions",
  "errors": null,
  "input_file_id": "file-abc123",
  "completion_window": "24h",
  "status": "validating",
  "output_file_id": null,
  "error_file_id": null,
  "created_at": 1711471533,
  "in_progress_at": null,
  "expires_at": null,
  "finalizing_at": null,
  "completed_at": null,
  "failed_at": null,
  "expired_at": null,
  "cancelling_at": null,
  "cancelled_at": null,
  "request_counts": {
    "total": 0,
    "completed": 0,
    "failed": 0
  },
  "metadata": {
    "customer_id": "user_123456789",
    "batch_description": "Nightly eval job",
  }
}
```
