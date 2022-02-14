def get_zsq(s):
    def zsq(func):
        # 万能形参，可以接收所有形式的传参
        def inner(*args, **kwargs):
            print(s)
            res = func(*args, **kwargs)  # 这里是解包
            return res

        return inner

    return zsq


'''
理解：
    把 @ 后面的整个当做一个装饰器
    @ 后面可以有函数调用，表达式等，只要最后结果是一个装饰器即可

'''


@get_zsq('-----')
def pnum(num):
    print(num)


pnum(10)
