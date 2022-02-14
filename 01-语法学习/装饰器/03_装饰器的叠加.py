def line1(func):
    def inner():
        print('------------------')
        func()
        print('------------------')

    return inner


def line2(func):
    def inner():
        print('******************')
        func()
        print('******************')

    return inner


@line1
@line1
@line2
def print_content():
    print('HelloWorld')


print_content()
'''
装饰器叠加规则：
    从上到下装饰，从下到上执行
'''
