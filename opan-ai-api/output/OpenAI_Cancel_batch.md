# [Cancel batch](/docs/api-reference/batch/cancel)
post https://api.openai.com/v1/batches/{batch_id}/cancel 
Cancels an in-progress batch. The batch will be in status
          cancelling for up to 10 minutes, before changing to
          cancelled, where it will have partial results (if any)
          available in the output file. 
## Path parameters 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| batch_id | string | Required | The ID of the batch to cancel.| 
## Returns 
The [Batch](/docs/api-reference/batch/object) object
                matching the specified ID. 

**Example request**
```python
from openai import OpenAI
client = OpenAI()
client.batches.cancel("batch_abc123")
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
  "status": "cancelling",
  "output_file_id": null,
  "error_file_id": null,
  "created_at": 1711471533,
  "in_progress_at": 1711471538,
  "expires_at": 1711557933,
  "finalizing_at": null,
  "completed_at": null,
  "failed_at": null,
  "expired_at": null,
  "cancelling_at": 1711475133,
  "cancelled_at": null,
  "request_counts": {
    "total": 100,
    "completed": 23,
    "failed": 1
  },
  "metadata": {
    "customer_id": "user_123456789",
    "batch_description": "Nightly eval job",
  }
}
```
