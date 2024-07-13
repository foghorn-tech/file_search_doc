# Notion


Notion's Python client: https://github.com/ramnes/notion-sdk-py

## Usage

```python
import os
from notion_client import Client

notion = Client(auth=os.environ["NOTION_TOKEN"])
```

