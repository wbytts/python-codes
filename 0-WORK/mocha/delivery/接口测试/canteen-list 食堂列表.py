import requests
import json

# 外卖后台服务地址
base_url = 'http://localhost:8080/delivery-api'


res = requests.get(base_url + '/foreign/canteen/v1/list')

json_obj = json.loads(res.text)
# 增加缩进，美化json输出
print(json.dumps(json_obj, indent=4, ensure_ascii=False))



