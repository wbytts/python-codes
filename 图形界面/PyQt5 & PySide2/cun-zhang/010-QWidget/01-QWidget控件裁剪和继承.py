from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("控件")
        self.resize(600, 500)
        self.func_list()

    def func_list(self):
        self.func()

    def func(self):
        label = QLabel(self)
        label.resize(150, 80)
        label.move(50, 450)
        label.setStyleSheet('background-color:green')
        print(label.parent())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    print(window)
    # window.setObjectName('1111')
    # print(window.objectName())
    print(window.parent())

    window.show()
    sys.exit(app.exec_())
