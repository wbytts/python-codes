from PyQt5.Qt import *
import sys
from qt_material import apply_stylesheet

'''
制作一个登陆界面，包含账号密码和登陆按钮
拥有密码清空和占位提示字符
验证账号和密码的正确性
如果账号错误，清空表单内容，焦点回到账号栏
如果密码错误，清空密码栏，焦点回到密码栏
'''


# class Check_Msg():
#     NAME_ERROR = 1
#     PSD_ERROR = 2
#     SUCCESS = 3
#     @staticmethod   # 本方法不需要实例化，所以直接设置成静态方法
#     def check_login(name,psd):
#         if name != 'aaa':
#             return Check_Msg.NAME_ERROR
#         if psd != '123':
#             return Check_Msg.PSD_ERROR
#         return Check_Msg.SUCCESS

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

    # def msgs(self):
    #     name = self.led_name.text()
    #     psd = self.led_psd.text()
    #     state = Check_Msg.check_login(name,psd)  # 返回的是登陆状态，后面只要判断状态就可以了
    #     if state == 1:
    #         self.led_name.setText('')
    #         self.led_psd.setText('')
    #         self.led_name.setFocus()
    #         print('账号错误')
    #         return None
    #     if state == 2:
    #         self.led_psd.setText('')
    #         self.led_psd.setFocus()
    #         print('密码错误')
    #         return None
    #     if state == 3:
    #         print('登陆成功')

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
    apply_stylesheet(app, theme='dark_teal.xml')
    window = Window()

    window.show()
    sys.exit(app.exec_())
