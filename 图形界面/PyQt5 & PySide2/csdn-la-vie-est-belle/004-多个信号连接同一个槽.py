import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.button = QPushButton('Start', self)
        # 将pressed和released信号连接搭配change_text()槽函数上
        self.button.pressed.connect(self.change_text)
        self.button.released.connect(self.change_text)

    def change_text(self):
        """
        若当前按钮文本为‘Start’，则将文本改为‘Stop’；若为‘Stop’，则改为‘Start’。
        所以当鼠标点击按钮不放时，发出pressed信号，调用槽函数，将‘Start’文本改为‘Stop’；
        当鼠标放开后释放released信号，再次调用槽函数，将文本改回‘Start’。
        :return:
        """
        if self.button.text() == 'Start':
            self.button.setText('Stop')
        else:
            self.button.setText('Start')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
