import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        # 首先在初始化函数中将窗口大小设置为宽300，长300
        self.resize(300, 300)
        # 其次将窗口名称设置为 000
        self.setWindowTitle('000')
        self.button = QPushButton('Start', self)
        self.button.clicked.connect(self.change_text)
        # 信号和槽连接，可以看到信号还是clicked，而槽函数多了两个
        self.button.clicked.connect(self.change_window_size)
        self.button.clicked.connect(self.change_window_title)

    def change_text(self):
        print('change text')
        self.button.setText('Stop')
        self.button.clicked.disconnect(self.change_text)

    def change_window_size(self):
        """修改窗口大小的槽函数"""
        print('change window size')
        self.resize(500, 500)
        self.button.clicked.disconnect(self.change_window_size)

    def change_window_title(self):
        """修改窗口名称的槽函数"""
        print('change window title')
        self.setWindowTitle('window title changed')
        self.button.clicked.disconnect(self.change_window_title)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
