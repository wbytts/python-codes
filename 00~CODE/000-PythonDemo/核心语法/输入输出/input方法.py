"""

Python3中：
    input()  这个函数等待用户输入,返回字符串
    input(s)  可以设置输入时的提示信息

Python2.7+中：
    input()、input(s)：会把输入的内容当做代码来处理
    raw_input()：接收到的内容当做字符串返回

"""

n = int(input('请输入一个数字:'))
print(n * n)
