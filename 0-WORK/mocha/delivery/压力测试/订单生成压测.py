import requests
import json

base_url = "http://127.0.0.1:8080/delivery-api"

res = requests.get(base_url + "/foreign/order/findOrderCode")
res = json.loads(res.text)
order_code = res['data']

print(order_code)
