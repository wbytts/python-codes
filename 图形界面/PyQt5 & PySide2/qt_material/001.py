from PyQt5.Qt import *
from qt_material import apply_stylesheet  # qt_material 必须在PySide或PyQt之后引入
import sys

"""
'dark_amber.xml',
'dark_blue.xml',
'dark_cyan.xml',
'dark_lightgreen.xml',
'dark_pink.xml',
'dark_purple.xml',
'dark_red.xml',
'dark_teal.xml',
'dark_yellow.xml',
'light_amber.xml',
'light_blue.xml',
'light_cyan.xml',
'light_cyan_500.xml',
'light_lightgreen.xml',
'light_pink.xml',
'light_purple.xml',
'light_red.xml',
'light_teal.xml',
'light_yellow.xml'
"""


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("登陆")
        self.resize(400, 200)
        self.func_list()

    def func_list(self):
        self.func()
        self.msgs()

    def func(self):
        self.led_name = QLineEdit(self)
        self.led_name.move(150, 50)
        self.btn1 = QPushButton('账号(aaa)', self)
        self.btn1.move(60, 49)
        self.led_name.setPlaceholderText('请输入账号')
        self.led_psd = QLineEdit(self)
        self.led_psd.move(150, 100)
        self.btn2 = QPushButton('密码(123)', self)
        self.btn2.move(60, 99)
        self.led_psd.setPlaceholderText('请输入密码')
        self.led_psd.setEchoMode(QLineEdit.Password)
        self.led_psd.setClearButtonEnabled(True)  # 有内容的时候才会显示
        self.btn_login = QPushButton(self)
        self.btn_login.setText('点击登陆')
        self.btn_login.move(150, 150)

        self.btn_login.clicked.connect(self.msgs)

    def msgs(self):
        # 获取账号和密码
        name = self.led_name.text()
        psd = self.led_psd.text()
        # 判断账号密码的正确性
        if name != 'aaa':
            self.led_name.setText('')
            self.led_psd.setText('')
            self.led_name.setFocus()
            print('账号错误')
            return None
        if psd != '123':
            self.led_psd.setText('')
            self.led_psd.setFocus()
            print('密码错误')
            return None
        print('验证通过')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_lightgreen.xml')
    window = Window()

    window.show()
    sys.exit(app.exec_())
