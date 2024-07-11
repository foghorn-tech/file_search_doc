# [Retrieve batch](/docs/api-reference/batch/retrieve)
get https://api.openai.com/v1/batches/{batch_id} 
Retrieves a batch. 
## Path parameters 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| batch_id | string | Required | The ID of the batch to retrieve.| 
## Returns 
The [Batch](/docs/api-reference/batch/object) object
                matching the specified ID. 

**Example request**
```python
from openai import OpenAI
client = OpenAI()
client.batches.retrieve("batch_abc123")
```

**Response**
```python
{
  "id": "batch_abc123",
  "object": "batch",
  "endpoint": "/v1/completions",
  "errors": null,
  "input_file_id": "file-abc123",
  "completion_window": "24h",
  "status": "completed",
  "output_file_id": "file-cvaTdG",
  "error_file_id": "file-HOWS94",
  "created_at": 1711471533,
  "in_progress_at": 1711471538,
  "expires_at": 1711557933,
  "finalizing_at": 1711493133,
  "completed_at": 1711493163,
  "failed_at": null,
  "expired_at": null,
  "cancelling_at": null,
  "cancelled_at": null,
  "request_counts": {
    "total": 100,
    "completed": 95,
    "failed": 5
  },
  "metadata": {
    "customer_id": "user_123456789",
    "batch_description": "Nightly eval job",
  }
}
```
