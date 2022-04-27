from PyQt5.Qt import *
import sys

"""
信号名 = pyqtSignal(类型1, 类型2, 类型3)
信号名 = pyqtSignal([参数类型])
信号名 = pyqtSignal([参数1类型, 参数2类型])
信号名 = pyqtSignal([...], [...], ...)  # 多种信号参数

self.信号名[...].emit(参数列表...)
"""


class Btn(QPushButton):
    rightSignal = pyqtSignal([str], [str, int])

    def mousePressEvent(self, evt):
        super().mousePressEvent(evt)
        if evt.button() == Qt.RightButton:
            self.rightSignal[str, int].emit(self.text(), 555)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("自定义信号实现多种参数传递")
        self.resize(600, 500)
        self.func_list()

    def func_list(self):
        self.func()

    def func(self):
        btn = Btn(self)
        btn.setText('按钮')
        btn.move(200, 100)

        def btn_press(str, a):
            print('鼠标被按下' + '====' + str)
            print(a)

        btn.rightSignal[str, int].connect(btn_press)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())
