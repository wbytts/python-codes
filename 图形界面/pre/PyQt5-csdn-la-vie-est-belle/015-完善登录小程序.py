import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QLabel, QLineEdit, QPushButton, \
    QGridLayout, QVBoxLayout, QHBoxLayout, QMessageBox

USER_PWD = {
        'root': '123'
    }

class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(300, 100)
        self.setFixedSize(300, 100)
        self.setWindowTitle('用户登录')

        self.user_label = QLabel('用户名:', self)
        self.pwd_label = QLabel('密码:', self)
        self.user_line = QLineEdit(self)
        self.pwd_line = QLineEdit(self)
        self.login_button = QPushButton('登录', self)
        self.signin_button = QPushButton('注册', self)

        self.grid_layout = QGridLayout()
        self.h_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()

        self.lineedit_init()            # 单行文本输入框
        self.pushbutton_init()          # 按钮
        self.layout_init()

        self.signin_page = SigninPage()     # 实例化SigninPage()

    def layout_init(self):
        self.grid_layout.addWidget(self.user_label, 0, 0, 1, 1)
        self.grid_layout.addWidget(self.user_line, 0, 1, 1, 1)
        self.grid_layout.addWidget(self.pwd_label, 1, 0, 1, 1)
        self.grid_layout.addWidget(self.pwd_line, 1, 1, 1, 1)
        self.h_layout.addWidget(self.login_button)
        self.h_layout.addWidget(self.signin_button)
        self.v_layout.addLayout(self.grid_layout)
        self.v_layout.addLayout(self.h_layout)

        self.setLayout(self.v_layout)

    def lineedit_init(self):
        self.user_line.setPlaceholderText('请输入用户名')
        self.pwd_line.setPlaceholderText('请输入密码')

        self.user_line.textChanged.connect(self.check_input_func)
        self.pwd_line.textChanged.connect(self.check_input_func)

    def check_input_func(self):
        if self.user_line.text() and self.pwd_line.text():
            self.login_button.setEnabled(True)
        else:
            self.login_button.setEnabled(False)

    def pushbutton_init(self):
        self.login_button.setEnabled(False)
        self.login_button.clicked.connect(self.check_login_func)
        self.signin_button.clicked.connect(self.show_signin_page_func)

    def check_login_func(self):
        if USER_PWD.get(self.user_line.text()) == self.pwd_line.text():
            QMessageBox.information(self, '信息', '登陆成功！')
        else:
            QMessageBox.critical(self, '错误', '用户名或密码错误！')

        self.user_line.clear()
        self.pwd_line.clear()

    def show_signin_page_func(self):
        self.signin_page.exec_()


class SigninPage(QDialog):
    def __init__(self):
        super(SigninPage, self).__init__()
        self.setWindowTitle('用户注册')
        self.signin_user_label = QLabel('用户名:', self)
        self.signin_pwd_label = QLabel('密码:', self)
        self.signin_pwd2_label = QLabel('再次输入密码:', self)
        self.signin_user_line = QLineEdit(self)
        self.signin_pwd_line = QLineEdit(self)
        self.signin_pwd2_line = QLineEdit(self)
        self.signin_button = QPushButton('注册', self)

        self.user_h_layout = QHBoxLayout()
        self.pwd_h_layout = QHBoxLayout()
        self.pwd2_h_layout = QHBoxLayout()
        self.all_v_layout = QVBoxLayout()

        self.lineedit_init()            # 单行文本输入框
        self.pushbutton_init()          # 按钮
        self.layout_init()

    def layout_init(self):
        self.user_h_layout.addWidget(self.signin_user_label)
        self.user_h_layout.addWidget(self.signin_user_line)
        self.pwd_h_layout.addWidget(self.signin_pwd_label)
        self.pwd_h_layout.addWidget(self.signin_pwd_line)
        self.pwd2_h_layout.addWidget(self.signin_pwd2_label)
        self.pwd2_h_layout.addWidget(self.signin_pwd2_line)

        self.all_v_layout.addLayout(self.user_h_layout)
        self.all_v_layout.addLayout(self.pwd_h_layout)
        self.all_v_layout.addLayout(self.pwd2_h_layout)
        self.all_v_layout.addWidget(self.signin_button)

        self.setLayout(self.all_v_layout)

    def lineedit_init(self):
        self.signin_user_line.textChanged.connect(self.check_input_func)
        self.signin_pwd_line.textChanged.connect(self.check_input_func)
        self.signin_pwd2_line.textChanged.connect(self.check_input_func)


    def check_input_func(self):
        if self.signin_user_line.text() and self.signin_pwd_line.text() and self.signin_pwd2_line.text():
            self.signin_button.setEnabled(True)
        else:
            self.signin_button.setEnabled(False)

    def pushbutton_init(self):
        self.signin_button.setEnabled(False)
        self.signin_button.clicked.connect(self.check_signin_func)


    def check_signin_func(self):
        if self.signin_pwd_line.text() != self.signin_pwd2_line.text():
            QMessageBox.critical(self, '错误', '两次输入的密码不一致！')
        elif self.signin_user_line.text() not in USER_PWD:
            USER_PWD[self.signin_user_line.text()] = self.signin_pwd_line.text()
            QMessageBox.information(self, '信息', '注册成功')
            self.close()
        else:
            QMessageBox.critical(self, '错误', '用户名已存在！')

        self.signin_user_line.clear()
        self.signin_pwd_line.clear()
        self.signin_pwd2_line.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
