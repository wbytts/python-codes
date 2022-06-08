import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, \
    QHBoxLayout, QVBoxLayout
from qt_material import apply_stylesheet

class Demo(QWidget):

    def __init__(self):
        super(Demo, self).__init__()

        self.user_label = QLabel('Username:', self)
        self.pwd_label = QLabel('Password:', self)
        self.user_line = QLineEdit(self)
        self.pwd_line = QLineEdit(self)
        self.login_button = QPushButton('Log in', self)
        self.signin_button = QPushButton('Sign in', self)

        # 实例化三个布局管理器分别用来管理QLabel，QLineEdit和QPushButton
        self.label_v_layout = QVBoxLayout()  # 1
        self.line_v_layout = QVBoxLayout()  # 2
        self.button_h_layout = QHBoxLayout()  # 3
        # 这两个布局管理器用来管理1-3中的布局，
        # 它们添加的不是QLabel、QLineEdit或者QPushButton控件，而是通过addLayout()方法添加布局管理器。
        # 第4行的水平布局管理器将self.label_v_layout垂直布局和self.line_vlayout垂直布局这两个布局管理器从左到右依次水平摆放。
        # 第5行的垂直布局管理器将self.label_line_h_layout和self.button_h_layout垂直从上到下摆放；
        self.label_line_h_layout = QHBoxLayout()  # 4
        self.all_v_layout = QVBoxLayout()  # 5

        # 添加控件用addWidght()，添加布局用addLayout()
        self.label_v_layout.addWidget(self.user_label)  # 6
        self.label_v_layout.addWidget(self.pwd_label)
        self.line_v_layout.addWidget(self.user_line)
        self.line_v_layout.addWidget(self.pwd_line)
        self.button_h_layout.addWidget(self.login_button)
        self.button_h_layout.addWidget(self.signin_button)
        self.label_line_h_layout.addLayout(self.label_v_layout)  # 7
        self.label_line_h_layout.addLayout(self.line_v_layout)
        self.all_v_layout.addLayout(self.label_line_h_layout)
        self.all_v_layout.addLayout(self.button_h_layout)

        self.setLayout(self.all_v_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_teal.xml')
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
