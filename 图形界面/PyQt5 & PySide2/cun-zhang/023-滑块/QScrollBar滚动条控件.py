from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QScrollBar滚动条控件 - PyQt5中文网")
        self.resize(600, 500)
        self.func_list()

    def func_list(self):
        self.func()

    def func(self):
        slider1 = QScrollBar(self)
        slider1.resize(20, 480)
        slider1.move(580, 0)

        slider2 = QScrollBar(self)
        slider2.resize(580, 20)
        slider2.move(0, 480)
        slider2.setOrientation(Qt.Horizontal)
        slider2.setPageStep(50)  # 设置步长，同时调整滚动条宽度


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())
