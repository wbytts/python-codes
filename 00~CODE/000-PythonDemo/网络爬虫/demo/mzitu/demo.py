import requests

url = "https://www.mzitu.com/"
headers = {
            'User-Agent': 'User-Agent,Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        }

response = requests.get(url, headers=headers)

print(response.content.decode("utf-8"))