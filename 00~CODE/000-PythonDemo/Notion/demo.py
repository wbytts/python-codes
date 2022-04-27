import notion
from notion.client import NotionClient
import settings
from settings import page_ids

# 初始化 Notion 客户端
client = NotionClient(token_v2 = settings.token_v2)

page = client.get_block(page_ids['TEST'])






