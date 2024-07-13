# Query a database

## Params

- **database_id** (string, required): Identifier for a Notion database.
- **filter_properties** (string): A list of page property value IDs associated with the database. Use this param to limit the response to a specific page property value or values for pages that meet the `filter` criteria.
- **filter** (json): When supplied, limits which pages are returned based on the [filter conditions](https://developers.notion.com/reference/post-database-query#post-database-query-filter).
- **sorts** (array): When supplied, orders the results based on the provided [sort criteria](https://developers.notion.com/reference/post-database-query#post-database-query-sort).
- **start_cursor** (string): When supplied, returns a page of results starting after the cursor provided. If not supplied, this endpoint will return the first page of results.
- **page_size** (int32, defaults to 100): The number of items from the full list desired in the response. Maximum: 100.


## Code Implementation

```python
name = input("\n\nEnter the name of the person to search in People: ")
results = notion.databases.query(
    **{
        "database_id": database_id,
        "filter": {"property": "Name", "rich_text": {"contains": name}},
    }
).get("results")

no_of_results = len(results)

if no_of_results == 0:
    print("No results found.")
    sys.exit()

print(f"No of results found: {len(results)}")
```