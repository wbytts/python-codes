from PyQt5.Qt import *
import sys

'''
setPlaceholderText()
placeholderText()

文本内容限定（18-150）：
QValidator.Acceptable
QValidator.Intermediate
QValidator.Invalid
'''


class Validator(QValidator):
    def validate(self, num, pos):
        print(num, pos)
        try:
            if 18 <= int(num) <= 150:
                return (QValidator.Acceptable, num, pos)
            elif 1 <= int(num) <= 14:
                return (QValidator.Intermediate, num, pos)
            else:
                return (QValidator.Invalid, num, pos)
        except:
            if len(num) == 0:
                return (QValidator.Intermediate, num, pos)
            return (QValidator.Invalid, num, pos)

    def fixup(self, v_str):
        print('XXX', v_str)
        try:
            if int(v_str) < 18:
                return '18'
        except:
            return '18'


class My_int(QIntValidator):
    def fixup(self, v_str):
        print('XXX', v_str)
        try:
            if int(v_str) < 18:
                return '18'
        except:
            return '18'


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QLineEdit-验证器 - PyQt5中文网")
        self.resize(600, 500)
        self.func_list()

    def func_list(self):
        self.func()

    def func(self):
        led = QLineEdit(self)
        led.move(150, 150)

        led1 = QLineEdit(self)
        led1.move(150, 220)

        validator = Validator()  # 这个抽象类需要子类化
        led.setValidator(validator)

        # validator2 = My_int(18,150)
        # led.setValidator(validator2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())
