"""
装饰器的执行时间，是立即执行
"""


def check(fn):
    print('装饰器执行...')

    def inner():
        print('执行之前的操作')
        fn()
        print('执行之后的操作')

    return inner


@check
def fss():
    print('发说说')


fss()
