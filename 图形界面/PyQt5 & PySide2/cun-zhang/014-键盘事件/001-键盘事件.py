from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("鼠标事件")
        self.resize(600, 500)
        self.func_list()

    # 键盘事件
    # QKeyEvent

    def keyPressEvent(self, e: QKeyEvent):
        print('键盘按下: key=', e.key())
        if e.key() == Qt.Key_5:
            print('QQQQQ')
        if e.modifiers() == Qt.ControlModifier and e.key() == Qt.Key_C:
            print('Ctrl + C')
        if e.modifiers() == Qt.ControlModifier | Qt.ShiftModifier and e.key() == Qt.Key_C:
            print('Ctrl + Shift + C')

    def keyReleaseEvent(self, e: QKeyEvent):
        print('键盘抬起~~~')

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
