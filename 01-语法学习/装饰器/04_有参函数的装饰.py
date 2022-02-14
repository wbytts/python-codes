def zsq(func):
    # 万能形参，可以接收所有形式的传参
    def inner(*args, **kwargs):
        print('-----------------')
        func(*args, **kwargs)  # 这里是解包

    return inner


@zsq
def pnum(num):
    print(num)


pnum(10)
