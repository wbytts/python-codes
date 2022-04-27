from PyQt5.Qt import *
import sys

"""
同级控件中后创建的控件会覆盖先创建的控件
    lower() 将控件放在最底层
    raise_() 将控件放到最上层
    a.stackUnder(b) 将a放到b的下面
"""


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("控件层级关系 - PyQt5中文网")
        self.resize(600, 500)
        self.func_list()

    def func_list(self):
        self.func()

    def func(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()

    label1 = QLabel(window)
    label1.setText('标签1')
    label1.resize(100, 100)
    label1.move(50, 50)
    label1.setStyleSheet('background-color:green')

    label2 = QLabel(window)
    label2.setText('标签2')
    label2.resize(100, 100)
    label2.move(80, 80)
    label2.setStyleSheet('background-color:red')

    # label2.lower()
    # label1.raise_()
    label2.stackUnder(label1)

    window.show()
    sys.exit(app.exec_())
