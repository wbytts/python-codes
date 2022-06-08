from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QSS-语法声明-外边距和内边距设置 - PyQt5中文网")
        self.resize(600, 500)
        self.func_list()

    def func_list(self):
        self.func()

    def func(self):
        label1 = QLabel('外边距和内边距设置', self)
        label1.resize(200, 200)

        '''外边距(px/em)
        margin
        margin-top
        margin-right
        margin-bottom
        margin-left

        QLabel{
            border-width:10px;
            border-color:red;
            border-style:solid;
            margin-top:10px;
            margin-left:100px;
            background-color:green;
        }
        '''

        '''内边距(px/em)
        padding
        padding-top
        padding-right
        padding-bottom
        padding-left

        QLabel{
            border-width:10px;
            border-color:red;
            border-style:solid;
            padding-bottom:10px;
            padding-right:100px;
            background-color:green;
        }
        '''


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()

    with open('base5.qss', 'r', encoding='UTF-8') as f:
        qApp.setStyleSheet(f.read())

    window.show()
    sys.exit(app.exec_())
