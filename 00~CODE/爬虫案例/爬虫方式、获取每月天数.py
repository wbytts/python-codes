import requests
import re

year = input("请输入年份:")
month = input("请输入月份:")

# 请求 http://wannianli.tianqi.com，这里面有每个月的天数，我们要爬取它
response = requests.get(
    f"http://wannianli.tianqi.com/{year}/{month}/",
    headers={
        "User-Agent": "User-Agent,Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    })

# 通过正则表达式找到天数
days = int(re.findall(r'<li class="full" id="i1(\d+)">', response.text)[-1][-2:])

print(f"{year}年{month}月的天数是: {days}")
