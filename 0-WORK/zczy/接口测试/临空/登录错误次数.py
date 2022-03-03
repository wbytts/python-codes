import requests

base_url = 'http://192.168.87.29:18089'
req_path = '/airport-frontend-server/user/errorTimes'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
}

res = requests.post(base_url + req_path, data={'account': '18856490832'}, headers=headers)
print(res.text)
