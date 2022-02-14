import urllib.request
import urllib.parse
from http import cookiejar

headers = {
    'User-Agent': 'User-Agent,Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
}

login_url = "..."
target_url = "https://i-beta.cnblogs.com/posts"

login_form_data = {
    "username": "xxx",
    "password": "xxx",
    # ......其他参数
}

# 转码
login_form_data = urllib.parse(login_form_data).encode("utf-8")

# 发送请求，拿到response里的cookie

cookie_jar = cookiejar.CookieJar()
# 定义有添加cookie功能的处理器
cookie_handler = urllib.request.HTTPCookieProcessor(cookie_jar)
# 根据处理器生成openner
openner = urllib.request.build_opener(cookie_handler)

# 带着参数，发送post请求
login_request = urllib.request.Request(login_url, headers=headers, data=login_form_data)
# 如果登录成功，cookiejar会自动保存cookie
openner.open(login_request)

target_request = urllib.request.Request(target_url, headers=headers)
response = openner.open(target_request)
data = response.read()
print(data)
