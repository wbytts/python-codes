from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle('让窗口居中显示')
        self.resize(500, 500)
        self.move_center()

    def move_center(self):
        # 获取屏幕坐标系
        screen = QDesktopWidget().screenGeometry()
        # 获取窗口坐标系
        size = self.geometry()
        # 计算坐标
        new_left = (screen.width() - size.width()) / 2
        new_top = (screen.height() - size.height()) / 2
        # 移动窗口到屏幕中间
        self.move(new_left, new_top)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
