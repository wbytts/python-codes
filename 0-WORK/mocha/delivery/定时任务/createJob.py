import requests

base_url = "http://127.0.0.1:8081/delivery-task"

res = requests.get(base_url + "/quartz/createJob")
print(res.text)
