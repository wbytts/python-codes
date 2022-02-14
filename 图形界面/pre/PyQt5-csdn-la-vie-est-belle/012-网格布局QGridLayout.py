import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, \
    QGridLayout, QVBoxLayout, QHBoxLayout

"""
当使用该布局管理器的时候，你可以把整个窗体想象成带有坐标的，然后只用把各个控件放在相应的坐标就好了

这里混合使用QVBoxLayout、QHBoxLayout和QGridLayout来完成布局。
"""

class Demo(QWidget):

    def __init__(self):
        super(Demo, self).__init__()

        self.user_label = QLabel('Username:', self)
        self.pwd_label = QLabel('Password:', self)
        self.user_line = QLineEdit(self)
        self.pwd_line = QLineEdit(self)
        self.login_button = QPushButton('Log in', self)
        self.signin_button = QPushButton('Sign in', self)

        # 实例化一个QGridLayout布局管理器
        self.grid_layout = QGridLayout()  # 1
        self.h_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()

        # QGridLayout的addWidget()方法遵循如下语法形式
        # addWidget(widget, row, column, rowSpan, columnSpan)
        #       widget就是要添加的控件；
        #       row为第几行，0代表第一行；
        #       column为第几列，0代表第一列；
        #       rowSpan表示要让这个控件去占用几行(默认一行)；
        #       columnSpan表示要让这个控件去占用几列(默认一列)。
        # 因为默认都是一行一列，所以一般可以少些最后两个参数
        self.grid_layout.addWidget(self.user_label, 0, 0, 1, 1)  # 2
        self.grid_layout.addWidget(self.user_line, 0, 1, 1, 1)
        self.grid_layout.addWidget(self.pwd_label, 1, 0, 1, 1)
        self.grid_layout.addWidget(self.pwd_line, 1, 1, 1, 1)
        self.h_layout.addWidget(self.login_button)
        self.h_layout.addWidget(self.signin_button)

        # 最后，程序用垂直布局管理器将一个网格布局和一个水平布局添加进去
        self.v_layout.addLayout(self.grid_layout)  # 3
        self.v_layout.addLayout(self.h_layout)  # 4

        self.setLayout(self.v_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
