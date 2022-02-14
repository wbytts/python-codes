import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QHBoxLayout


class Demo(QWidget):

    def __init__(self):
        super(Demo, self).__init__()
        self.user_label = QLabel('Username:', self)
        # QLineEdit控件就是一个用来进行单行文本输入的框
        self.user_line = QLineEdit(self)
        # 实例化一个水平布局管理器
        self.h_layout = QHBoxLayout()
        # 将QLabel和QLineEdit控件添加到水平布局管理器中，先添加的出现在左边
        self.h_layout.addWidget(self.user_label)
        self.h_layout.addWidget(self.user_line)
        # 将self.h_layout设为整个窗口的最终布局方式
        self.setLayout(self.h_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
