from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('事件机制')
        self.resize(600, 450)
        self.move(300, 300)


class Btn(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.move(60, 60)
        self.resize(50, 35)
        self.setText('按钮控件')
        self.setStyleSheet('background-color:green')

    def event(self, evt):
        print(evt, '事件机制')
        return super().event(evt)  # 对下分发

    def mousePressEvent(self, evt):
        print("鼠标按下事件")
        return super().mousePressEvent(evt)  # 事件继续分发


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    btn = Btn(window)


    def myslot():
        print('~~~~~~~~~~')


    btn.pressed.connect(myslot)

    window.show()
    sys.exit(app.exec_())
