from PyQt5.Qt import *
import sys

"""
控件.信号.connect(槽函数)
"""


class Btn(QPushButton):
    rightSignal = pyqtSignal()  # 先定义好一个信号，然后寻找这个信号所属事件

    def mousePressEvent(self, evt):
        super().mousePressEvent(evt)
        # print(evt.button())  # QMouseEvent
        # if evt.button() == 2:
        if evt.button() == Qt.RightButton:
            print('鼠标右键被按下-mousePressEvent事件')  # 这是用来测试右键是否生效，不是槽函数功能
            self.rightSignal.emit()  # 通过emit函数来把之定义的信号发射出去
        pass


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("自定义信号的原理和方法")
        self.resize(600, 500)
        self.func_list()

    def func_list(self):
        self.func()

    def func(self):
        # btn = QPushButton(self)
        btn = Btn(self)
        btn.setText('按钮')
        btn.move(200, 100)

        def btn_press():
            print('鼠标右键被按下-槽函数')

        # btn.pressed.connect(btn_press)
        btn.rightSignal.connect(btn_press)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())
