# [Upload file](/docs/api-reference/files/create)
post https://api.openai.com/v1/files 
Upload a file that can be used across various endpoints. Individual
          files can be up to 512 MB, and the size of all files uploaded by one
          organization can be up to 100 GB. 
The Assistants API supports files up to 2 million tokens and of
          specific file types. See the
          [Assistants Tools guide](/docs/assistants/tools) for
          details. 
The Fine-tuning API only supports .jsonl files. The input
          also has certain required formats for fine-tuning
          [chat](/docs/api-reference/fine-tuning/chat-input) or
          [completions](/docs/api-reference/fine-tuning/completions-input)
          models. 
The Batch API only supports .jsonl files up to 100 MB in
          size. The input also has a specific required
          [format](/docs/api-reference/batch/request-input). 
Please
          [contact us](https://help.openai.com/)
          if you need to increase these storage limits. 
## Request body 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| file | file | Required | The File object (not file name) to be uploaded.| 
| purpose | string | Required | The intended purpose of the uploaded file.                    Use "assistants" for                   Assistants and                   Message files,                   "vision" for Assistants image file inputs, "batch" for                   Batch API, and "fine-tune"                   for Fine-tuning.| 
## Returns 
The uploaded
                [File](/docs/api-reference/files/object) object. 

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
