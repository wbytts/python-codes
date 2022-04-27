"""

"""
from PyQt5.Qt import *
import sys

class MySignal(QObject):
    sendmsg = pyqtSignal(str)   # 声明一个信号对象

    def send_msg(self):
        self.sendmsg.emit('hello world')  # 使用信号去发射一个文本

    def get_msg(self, str):
        print('你好' + str)

mysignal = MySignal()
mysignal.sendmsg.connect(mysignal.get_msg)  # 使用对象中的信号去链接槽中的方法
mysignal.send_msg()   # 执行信号中的方法 ， 之后槽函数就能处理对应的信号数据


# def myslot():
#     print('AAAAAAAAAAA')
#
# btn.pressed.connect(myslot)
