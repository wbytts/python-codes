from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("控件内容区域获取和设置")
        self.resize(600, 500)
        self.func_list()

    def func_list(self):
        self.func()

    def func(self):
        label = QLabel(self)
        label.resize(150, 150)
        label.move(50, 50)
        label.setText('标签学习')
        label.setStyleSheet('background-color:green')
        # 设置内容边距
        # 顺序：左上右下
        label.setContentsMargins(50, 20, 0, 0)
        print(label.getContentsMargins())
        print(label.contentsRect())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())
