# Upload file

## Request body 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| file | file | Required | The File object (not file name) to be uploaded.| 
| purpose | string | Required | The intended purpose of the uploaded file.                    Use "assistants" for                   Assistants and                   Message files,                   "vision" for Assistants image file inputs, "batch" for                   Batch API, and "fine-tune"                   for Fine-tuning.| 

## Returns 
The uploaded object. 

**Example request**
```python
from openai import OpenAI
client = OpenAI()
client.files.create(
  file=open("mydata.jsonl", "rb"),
  purpose="fine-tune"
)
```

**Response**
```python
{
  "id": "file-abc123",
  "object": "file",
  "bytes": 120000,
  "created_at": 1677610602,
  "filename": "mydata.jsonl",
  "purpose": "fine-tune",
}
```
