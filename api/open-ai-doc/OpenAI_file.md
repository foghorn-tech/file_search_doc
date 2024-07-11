# Open AI File

## Upload File
```python
from openai import OpenAI
client = OpenAI()

client.files.create(
  file=open("mydata.jsonl", "rb"),
  purpose="fine-tune"
)
```

## Retrieve File

```python
from openai import OpenAI
client = OpenAI()
file = client.files.retrieve("file-abc123")
```

## Retrieve File Content
```python
from openai import OpenAI
client = OpenAI()

content = client.files.content("file-abc123")
```

