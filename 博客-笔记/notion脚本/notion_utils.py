import requests
import json


def format_json(s):
    return json.dumps(json.loads(s), indent=4, ensure_ascii=False)


class NotionApiRequest:

    host = "https://api.notion.com"
    version = "v1"
    base_url = f"{host}/{version}"

    def __init__(self, integration_token, notion_version):
        """
        integration_token
        notion_version：notion的版本，年月日，如 2021-08-16
        """
        self.integration_token = integration_token
        self.notion_version = notion_version

    def get_headers(self):
        """构造请求头"""
        return {
            "Notion-Version": f"{self.notion_version}",
            "Authorization": f"Bearer {self.integration_token}",
        }

    def query_database(self, database_id, filter=None, sorts=None, start_cursor=None, page_size=None):
        """
        查询database
        参数：database_id
        """
        if sorts is None:
            sorts = []
        if filter is None:
            filter = {}
        url = f"{self.base_url}/databases/{database_id}/query"
        params = {
            "filter": filter,
            "sorts": sorts,
            "start_cursor": start_cursor,
            "page_size": page_size,
        }
        res = requests.post(url, headers=self.get_headers(), data=params)
        return format_json(res.text)

    def create_database(self, parent, title=None, properties=None):
        """
        创建一个database
        参数：
        """
        url = f'{self.base_url}/databases'
        params = {

        }
        res = requests.post(url, headers=self.get_headers(), data=params)
        return format_json(res.text)

    def update_database(self, database_id, title=None, properties=None):
        """
        更新database
        参数：
            database_id
        """
        url = f'{self.base_url}/databases/{database_id}'

    def query_block_children(self, block_id, params):
        """
        查询block的子节点
        参数：block_id
        """
        url = f"{self.base_url}/blocks/{block_id}/children"
        res = requests.get(url, headers=self.get_headers())
        return format_json(res.text)


class NotionUtils:
    def __init__(self) -> None:
        pass


