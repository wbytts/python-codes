import requests
import json

# 外卖后台服务地址
base_url = 'http://localhost:8080/delivery-api'

params = {
    # 订单编号
    'orderCode': 'SZ0001202104281824320001',
}
res = requests.post(base_url + '/pay/mochasoft-newpay', json=params)

json_obj = json.loads(res.text)
if 'data' in json_obj and json_obj['data']:
    json_obj['data'] = json.loads(json_obj['data'])
print(json.dumps(json_obj, indent=4, ensure_ascii=False))
