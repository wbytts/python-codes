from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QSS-前景设置-字体和文本设置 - PyQt5中文网")
        self.resize(600, 500)
        self.func_list()

    def func_list(self):
        self.func()

    def func(self):
        label1 = QLabel('字体设置字体设置字体设置', self)
        label1.resize(200, 200)

        str = '《PyQt5中文网》原创全套PyQt5视频教程，Qt Designer+PyUIC教程 \n pyqtgraph教程，以及pyqt5布局、控件、信号、槽、扩展应用和打包上线相关知识，此外还分享一些PyQt5常见问题和pyqt漂亮gui界面模板资源，从入门到精通一站式学习python可视化编程技术。'
        text1 = QTextEdit(str, self)
        text1.move(150, 150)
        text1.resize(200, 300)

        '''文本字体
        font
        font-size
        font-style:normal(标准字体)  italic(斜体)  oblique()
        font-weight:normal(标准字体==400)  bold(加粗字体==700)  bolder(更粗字体)  lighter(更细字体)  100-900
        color
        '''


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()

    with open('base8.qss', 'r', encoding='UTF-8') as f:
        qApp.setStyleSheet(f.read())

    window.show()
    sys.exit(app.exec_())
