from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QSS-语法声明-边框的圆角 - PyQt5中文网")
        self.resize(600, 500)
        self.func_list()

    def func_list(self):
        self.func()

    def func(self):
        label1 = QLabel('标签', self)
        label1.move(100, 100)
        label1.resize(200, 200)
        label1.setStyleSheet('background-color:green;')

        '''边框圆角
        border-radius
        border-top-left-radius
        border-top-right-radius
        border-bottom-left-radius
        border-bottom-right-radius
        '''
        '''
        QLabel{
            border-radius:50px;
            border-top-left-radius:50px;
            border-top-right-radius:50px;
            border-bottom-left-radius:50px;
            border-bottom-right-radius:50px;
        }
        '''

        '''边框图片：使用四条线把图片border-image.png裁剪成9份，除了4个角，其他部分按照下面策略排版
        repeat  重复
        round  平铺
        stretch  拉伸
        border-image:url(border-image.png) 55px 55px 55px 55px repeat
        border-image:url(border-image.png) 33.33% repeat
        '''

        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()

    with open('base4.qss', 'r', encoding='UTF-8') as f:
        qApp.setStyleSheet(f.read())

    window.show()
    sys.exit(app.exec_())
