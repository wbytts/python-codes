import requests
from faker import Faker
import json

headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6",
    "content-type": "application/json;charset=UTF-8",
    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "tokenid": "zb_public:c46e49b7-57ed-4f35-872c-5aea7d1db878",
    "x-requested-with": "XMLHttpRequest",
    "cookie": "JSESSIONID=zb_public:c46e49b7-57ed-4f35-872c-5aea7d1db878; Webstorm-23fed1c5=58b893e0-a985-42d0-87ef-1b86ae564ab3",
    #"Referer": "http://localhost:8080/project/addFillIn?activeUrl=%2Fproject%2FprojectFillIn&uniqueId=8&keepAlive=true",
    #"Referrer-Policy": "strict-origin-when-cross-origin",
}


dev_host = "http://172.20.21.49:8003"
test_host = "http://172.20.20.58:8003"
vue_host = "http://localhost:8080"

url = f"{dev_host}/zb-public/projectBaseNew/submitProjectBaseInfo"

data = {
    "projectId": 88,
    "deptId": 1
}

data = json.dumps(data)
res = requests.post(url, headers=headers, data=data)
print(res.text)
