# [The batch object](/docs/api-reference/batch/object)
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| id | string | Optional | | 
| object | string | Optional | The object type, which is always batch.| 
| endpoint | string | Optional | The OpenAI API endpoint used by the batch.| 
| errors | object | Optional | | 
| input_file_id | string | Optional | The ID of the input file for the batch.| 
| completion_window | string | Optional | The time frame within which the batch should be processed.| 
| status | string | Optional | The current status of the batch.| 
| output_file_id | string | Optional | The ID of the file containing the outputs of successfully                 executed requests.| 
| error_file_id | string | Optional | The ID of the file containing the outputs of requests with                 errors.| 
| created_at | integer | Optional | The Unix timestamp (in seconds) for when the batch was created.| 
| in_progress_at | integer | Optional | The Unix timestamp (in seconds) for when the batch started                 processing.| 
| expires_at | integer | Optional | The Unix timestamp (in seconds) for when the batch will expire.| 
| finalizing_at | integer | Optional | The Unix timestamp (in seconds) for when the batch started                 finalizing.| 
| completed_at | integer | Optional | The Unix timestamp (in seconds) for when the batch was                 completed.| 
| failed_at | integer | Optional | The Unix timestamp (in seconds) for when the batch failed.| 
| expired_at | integer | Optional | The Unix timestamp (in seconds) for when the batch expired.| 
| cancelling_at | integer | Optional | The Unix timestamp (in seconds) for when the batch started                 cancelling.| 
| cancelled_at | integer | Optional | The Unix timestamp (in seconds) for when the batch was                 cancelled.| 
| request_counts | object | Optional | The request counts for different statuses within the batch.| 
| metadata | map | Optional | Set of 16 key-value pairs that can be attached to an object.                 This can be useful for storing additional information about the                 object in a structured format. Keys can be a maximum of 64                 characters long and values can be a maxium of 512 characters                 long.| 

**The batch object**
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
