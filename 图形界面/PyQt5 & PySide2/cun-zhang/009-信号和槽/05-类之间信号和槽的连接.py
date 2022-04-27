from PyQt5.Qt import *
import sys

class MySignal(QObject):
    sendmsg = pyqtSignal(str, int, int)

    def send_msg(self):
        self.sendmsg.emit('hello', 2, 9)


class Myslot(QObject):
    def get_msg(self, str, a, b):
        print('你好' + str)
        print(a + b)


mysignal = MySignal()
myslot = Myslot()
mysignal.sendmsg.connect(myslot.get_msg)
mysignal.send_msg()
