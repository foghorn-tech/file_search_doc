import os
from notion_client import Client

notion = Client(auth="secret_7CPY1LriHRRQVYWXtD8sUgVLu2UVvHefrfqQ51v9X8c")


db = notion.databases.retrieve(database_id="72d2da107202431abe2a8beb455ba8d2")
print(db)

# Search for an item
# result = notion.databases.query(database_id="72d2da107202431abe2a8beb455ba8d2")
# print(result)
# # # store the database id in a variable for future use
# #
# Create a new page
# new_subpage = {
#     "parent": {"page_id": "087fa6ecfc5d4350adc021cb27b1255f"},
#     "properties": {
#         "title": {"title": [{"text": {"content": "page"}}]},
#     },
#     "children": [
#         {
#             "object": "block",
#             "type": "paragraph",
#             "paragraph": {
#                 "rich_text": [{"type": "text", "text": {"content": "page content"}}]
#             },
#         },
#         {
#             "object": "block",
#             "type": "heading_2",
#             "heading_2": {
#                 "rich_text": [{"type": "text", "text": {"content": "page sub title"}}]
#             },
#         },
#     ],
# }
# response = notion.pages.create(**new_subpage)
# print(response)
# print("You were added to the People database!")

# # Query page
# page_id = "087fa6ecfc5d4350adc021cb27b1255f"
# page = notion.pages.retrieve(page_id=page_id)
# print(page)

#
#
# # Query a database
# name = input("\n\nEnter the name of the person to search in People: ")
# results = notion.databases.query(
#     **{
#         "database_id": database_id,
#         "filter": {"property": "Name", "rich_text": {"contains": name}},
#     }
# ).get("results")
#
# no_of_results = len(results)
#
# if no_of_results == 0:
#     print("No results found.")
#     sys.exit()
#
# print(f"No of results found: {len(results)}")
#
# result = results[0]
#
# print(f"The first result is a {result['object']} with id {result['id']}.")
# print(f"This was created on {result['created_time']}")