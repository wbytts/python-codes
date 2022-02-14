import requests
import json

url = "https://gitbook.cn/activities?page=%d&type=new&isSelected=false"

for i in range(100):
    res = requests.get(url % (i+1))
    res_json = json.loads(res.text)
    print(res_json)
    for item in res_json['data']:
        print(item)
