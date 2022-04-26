from pywebio.input import *
from pywebio.output import *
from pywebio.pin import *
from pywebio import start_server


def input_input():
    # input的合法性校验
    # 自定义校验函数

    def check_age(n):
        if n < 1:
            return "Too Small!@"
        if n > 100:
            return "Too Big!@"
        else:
            pass

    myAge = input('please input your age:', type=NUMBER, validate=check_age, help_text='must in 1,100')
    print('myAge is:', myAge)


if __name__ == '__main__':
    start_server(
        applications=[input_input, ],
        debug=True,
        auto_open_webbrowser=True,
        remote_access=True,
    )
