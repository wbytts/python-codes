from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle('识别系统 - 吴承希')
        self.setFixedSize(1500, 800)  # 设置主窗口固定大小，不可调整
        self.set_ui()  # 设置界面UI

    def set_ui(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
