from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("窗口事件")
        self.resize(600, 500)
        self.func_list()

    # 窗口事件
    def showEvent(self, event: QShowEvent) -> None:
        print('窗口打开')

    def closeEvent(self, event: QCloseEvent) -> None:
        print('窗口关闭')

    def moveEvent(self, event: QMoveEvent) -> None:
        print('窗口移动')

    def resizeEvent(self, event: QResizeEvent) -> None:
        print('窗口缩放')  # 缩放的同时，其实也算是移动

    def func_list(self):
        self.func()

    def func(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()

    # window.setMouseTracking(True)

    window.show()
    sys.exit(app.exec_())
