import requests

url = 'https://fanyi.baidu.com/v2transapi'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/86.0.4240.111 Safari/537.36'
}

form_data = {
    'from': 'zh',
    'to': 'en',
    'transtype': 'realtime',
    # 'simple_means_flag': 3,
    # 'sign': 232427.485594,
    'token': 'ba0d48943a1ecfc7f25a9db9dc4bb67d',
    'domain': 'common',
    'query': '你好',
}

res = requests.post(url=url, headers=headers, data=form_data)

print(res.json())
