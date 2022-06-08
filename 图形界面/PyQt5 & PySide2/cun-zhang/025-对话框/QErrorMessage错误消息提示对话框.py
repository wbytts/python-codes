from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("展示控件对话框-QErrorMessage错误消息提示 - PyQt5中文网")
        self.resize(600, 500)
        self.func_list()

    def func_list(self):
        self.func()

    def func(self):
        err = QErrorMessage(self)
        err.setWindowTitle('错误消息')  # 窗口标题
        err.showMessage('下载中遇到错误，错误代码123456')
        err.showMessage('下载中遇到错误，错误代码123456')
        err.showMessage('下载中遇到错误，错误代码123456')
        err.showMessage('下载中遇到错误，错误代码1111')
        err.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())
