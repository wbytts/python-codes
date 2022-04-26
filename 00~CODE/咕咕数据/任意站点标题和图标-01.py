
import requests
import json

x = 'https://juejin.cn/post/6844903476263125000'

url = f"https://api.gugudata.com/websitetools/favicon?appkey=3C448YHSXD6Q&url={x}"
payload = {}
headers = {}
response = requests.request("GET", url, headers=headers, data = payload)

res_json = json.loads(response.text)

print(res_json)
