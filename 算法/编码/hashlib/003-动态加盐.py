import hashlib

user = input("请输入账号：")
pwd = input("请输入密码：")

md5 = hashlib.md5(user.encode('utf-8'))  # user每次都变
md5.update(pwd.encode('utf-8'))
print(md5.hexdigest())
