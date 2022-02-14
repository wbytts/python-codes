'''
内部函数、外部函数
内部函数中使用了外部函数的变量
把整个内部函数作为外部函数的返回值
'''


def out():
    a = 3
    def inner():
        a = 4

    inner()

    print(a)


out()

