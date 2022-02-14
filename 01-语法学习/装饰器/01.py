def checkLogin(fn):
    def inner():
        print("登录验证......")
        fn()

    return inner


@checkLogin  # 相当于 fss = checkLogin(fss)
def fss():
    print("发说说")


@checkLogin  # 相当于 ftp = checkLogin(ftp)
def ftp():
    print("发图片")


btn_index = int(input("请输入:"))

if btn_index == 1:
    fss()
else:
    ftp()
