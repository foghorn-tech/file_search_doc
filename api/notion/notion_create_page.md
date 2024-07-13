## Create new page 

### Create new page in page

Creates a new page that is a child of an existing page, If the new page is a child of an existing page,title is the only valid property in the properties body param.


```python
content = "content"
new_subpage = {
    "parent": {"page_id": "087fa6ecfc5d4350adc021cb27b1255f"},
    "properties": {
        "title": {"title": [{"text": {"content": content}}]},
    }
}
response = notion.pages.create(**new_subpage)
```

### Create new page in database

If the new page is a child of an existing database, the keys of the properties object body param must match the parent database's properties.

```python
your_name = "John Doe"
new_page = {
    "Name": {"title": [{"text": {"content": your_name}}]},
    "Tags": {"type": "multi_select", "multi_select": [{"name": "python"}]},
}
notion.pages.create(parent={"database_id": database_id}, properties=new_page)
print("You were added to the People database!")
```