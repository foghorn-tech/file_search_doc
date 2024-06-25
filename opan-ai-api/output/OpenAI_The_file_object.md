# [The file object](/docs/api-reference/files/object)
The File object represents a document that has been
          uploaded to OpenAI. 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| id | string | Optional | The file identifier, which can be referenced in the API                 endpoints.| 
| bytes | integer | Optional | The size of the file, in bytes.| 
| created_at | integer | Optional | The Unix timestamp (in seconds) for when the file was created.| 
| filename | string | Optional | The name of the file.| 
| object | string | Optional | The object type, which is always file.| 
| purpose | string | Optional | The intended purpose of the file. Supported values are                 assistants, assistants_output,                 batch, batch_output,                 fine-tune, fine-tune-results and                 vision.| 
| status | string | Optional | Deprecated. The current status of the file, which can be either                 uploaded, processed, or                 error.| 
| status_details | string | Optional | Deprecated. For details on why a fine-tuning training file                 failed validation, see the error field on                 fine_tuning.job.| 

**The file object**
```python
{
  "id": "file-abc123",
  "object": "file",
  "bytes": 120000,
  "created_at": 1677610602,
  "filename": "salesOverview.pdf",
  "purpose": "assistants",
}
```
