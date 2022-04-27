from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("获取和设置控件尺寸、大小以及控件大小尺寸限定")
        # self.resize(600,500)
        self.func_list()

    def func_list(self):
        self.func()

    def func(self):
        label = QLabel(self)
        # label.resize(60, 30)
        # label.move(50, 200)
        label.setGeometry(50, 200, 60, 30)
        label.setText('标')
        # label.adjustSize()
        label.setFixedSize(52, 50)

        label.setStyleSheet('background-color:green')

        label.setContentsMargins(50, 0, 0, 0)
        print(label.getContentsMargins())
        print(label.contentsRect())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()

    # 最小大小
    window.setMinimumSize(200, 200)
    # 最大大小
    window.setMaximumSize(500, 600)
    print(window.maximumHeight())

    window.show()
    sys.exit(app.exec_())
