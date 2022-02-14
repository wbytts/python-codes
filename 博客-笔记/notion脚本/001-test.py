import requests
import json
from notion_utils import NotionApiRequest

NAR = NotionApiRequest("secret_73m9zLMIECUxfIBQxriXRUuDVIiQ7EdxxwqPulOdDmr", "2021-08-16")
# print(NAR.query_block_children("89db9ecc31c54c50a254b9168b34f948"))
print(NAR.query_database('644d782bf49a47f28379ece1af463c47'))


# page_params = {
#         "parent": {"type": "database_id", "database_id": "9bcf00dc-e55c-4279-9f3b-177dc325aa18"},
#         "properties": {
#             "来源": {"url": url},
#             "标题": {"title": [{"type": "text", "text": {"content": '标题啦啦啦'}}]},
#             "描述": {"rich_text": [{"type": "text", "text": {"content": content}}]},
#         },
#         "children": [
#             {
#             "object": "block",
#             "type": "paragraph",
#             "paragraph": {
#                 "text": [{ "type": "text", "text": { "content": content } }]
#             }
#             }
#         ]
#     }



