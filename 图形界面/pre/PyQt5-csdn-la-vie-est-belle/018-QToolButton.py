import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QToolButton


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        # 请注意不能在QToolButton实例化的时候直接传入文本字符串，因为该控件没有相应的初始化函数。
        # 也就是说这样做是错误的：self.test_button = QToolButton('Test', self)
        # 如果要设置文本的话得通过setText()方法。但是setText()方法和setIcon()方法都使用的话，只会显示图标。
        self.test_button = QToolButton(self)                        # 1
        self.test_button.setCheckable(True)
        self.test_button.setIcon(QIcon('f:/project/PythonDemo/004-GUI编程/PyQt5-csdn-la-vie-est-belle/button.png'))
        self.test_button.toggled.connect(self.button_state_func)
        self.test_button.isCheckable()

    def button_state_func(self):
        print(self.test_button.isChecked())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
