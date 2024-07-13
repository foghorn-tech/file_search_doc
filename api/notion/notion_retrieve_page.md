# Retrieve page 


## Description

Retrieve a page by ID.

## Code Implementation

```python
page_id = "087fa6ecfc5d4350adc021cb27b1255f"
page = notion.pages.retrieve(page_id=page_id)
print(page)
```