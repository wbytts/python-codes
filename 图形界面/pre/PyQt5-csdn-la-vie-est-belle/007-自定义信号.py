import sys
# 需要先导入pyqtSignal
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QLabel


class Demo(QWidget):
    # 实例化一个自定义的信号
    my_signal = pyqtSignal()

    def __init__(self):
        super(Demo, self).__init__()
        self.label = QLabel('Hello World', self)
        # 将自定义的信号连接到自定义的槽函数上
        self.my_signal.connect(self.change_text)

    def change_text(self):
        if self.label.text() == 'Hello World':
            self.label.setText('Hello PyQt5')
        else:
            self.label.setText('Hello World')

    def mousePressEvent(self, QMouseEvent):
        """
        mousePressEvent()方法是许多控件自带的，这里来自于QWidget。
        方法用来监测鼠标是否有按下。现在鼠标若被按下，则会发出自定义的信号。
        """
        self.my_signal.emit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
