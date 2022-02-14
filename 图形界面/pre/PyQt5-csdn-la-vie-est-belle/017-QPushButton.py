import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.test_button = QPushButton('Test', self)
        # 按钮有标记和非标记两种状态，这两种状态下的按钮显示的样子不同。
        # 通过setCheckable(True)方法可以将按钮设置为一个可标记的按钮，那此时该按钮就拥有了标记和非标记两种状态了。
        # 可以通过isCheckable()方法来判断该按钮是否是可标记的；
        self.test_button.setCheckable(True)                         # 1
        # 通过setIcon()方法给按钮设置一个图标，传入的参数为QIcon()；
        self.test_button.setIcon(QIcon('f:/project/PythonDemo/004-GUI编程/PyQt5-csdn-la-vie-est-belle/button.png'))               # 2
        # toggled信号是专门用来配合按钮标记状态变化的，也就是说按钮标记状态发生变化就会发出toggled信号。
        # 在这里将toggled信号和自定义的槽函数连接了起来；
        self.test_button.toggled.connect(self.button_state_func)    # 3

    def button_state_func(self):
        """
         通过isChecked()方法来判断按钮是否为标记状态，若是则返回True，不是则返回False。
         所以该槽函数会在按钮标记状态发生改变的时候启动，并打印True和False。
        """
        print(self.test_button.isChecked())                         # 4


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
