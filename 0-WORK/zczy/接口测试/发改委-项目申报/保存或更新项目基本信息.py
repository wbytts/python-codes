import requests
from faker import Faker
import json

fak = Faker()

# host = 'http://172.20.20.58:8003'
host = "http://172.20.21.49:8003"

url = f"{host}/zb-public/projectBase/saveOrUpdateProjectBaseInfo"

headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6",
    "content-type": "application/json;charset=UTF-8",
    "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"96\", \"Google Chrome\";v=\"96\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "tokenid": "zb_public:66e73bf7-12a8-4d00-8295-045594c3af76",
    "x-requested-with": "XMLHttpRequest",
    "cookie": "JSESSIONID=zb_public:66e73bf7-12a8-4d00-8295-045594c3af76; Webstorm-23fed1c5=58b893e0-a985-42d0-87ef-1b86ae564ab3",
    "Referer": "http://localhost:8080/project/addFillIn?activeUrl=%2Fproject%2FprojectFillIn&uniqueId=8&keepAlive=true",
    "Referrer-Policy": "strict-origin-when-cross-origin"
}


pyload = {
    "projectName": "test-十四五",
    "projectType": 5,
    "provinceName": "内蒙古自治区",
    "provinceCode": "150000",
    "cityName": "呼伦贝尔市",
    "cityCode": "150700",
    "areaName": "鄂伦春自治旗",
    "areaCode": "150723",
    "totalPlannedInvestment": "123",
    "projectContentSize": "123",
    "detailedAddress": fak.address(),
    #"projectUnitProperty": "12312",
    #"projectProperty": 1,
    "cumulativeInvestmentCompletion": "123",
    "constructionCycleStartTime": "2021-12-12T16:00:00.000Z",
    "constructionCycleEndTime": "2021-12-29T16:00:00.000Z",
    "actualStartTime": "2021-12-05T16:00:00.000Z",
    "actualEndTime": "2021-12-27T16:00:00.000Z",
    # "deptId": "123",
    "responsibleName": fak.first_name_female(),
    "responsiblePhoneNumber": "15052501111",
    "responsibleFixedNumber": "",
    "responsibleEmail": fak.email(),
    "concatName": fak.first_name_female(),
    "concatPhoneNumber": "15052501111",
    "concatFixedNumber": "",
    "concatEmail": fak.email(),
    "remark": "11111",
    "investor": "1111",
    #"monitorPlatformCode": 1,
    "projectStartTime": '2021-12-12',
    "projectEndTime": '2021-12-21',
}

# 删除字段【投资主体】【监管平台代码】【计划开工时间】【计划竣工时间】【备注】


pyload = json.dumps(pyload)

res = requests.post(url, headers=headers, data=pyload, timeout=3000)

print(res.text)
with open("./res.json", mode="w", encoding="utf8") as f:
    f.write(res.text)
