from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QSS-语法声明-边框渐变色设置 - PyQt5中文网")
        self.resize(600, 500)
        self.func_list()

    def func_list(self):
        self.func()

    def func(self):
        label1 = QLabel('标签1', self)
        label1.move(100, 200)
        label1.resize(150, 150)

        '''颜色的线性变化
        background-color:qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 red, stop:0.5 white, stop:1 green)
        x1:0, y1:0  起始点坐标
        x2:1, y2:0  结束点坐标
        stop:0 red  原点为红色
        stop:0.5 white  断点为白色（可多个）
        stop:1 green  终点为绿色
        '''

        '''辐射渐变
        background-color:qradialgradient(cx:0.7, cy:0.7, radius:0.5, fx:0.5, fy:0.5, stop:0 red, stop:0.5 white, stop:1 green)
        cx:0.7, cy:0.7  光源中心点坐标
        radius:0.5  辐射半径
        fx:0.5, fy:0.5  光源位置
        stop:0 red  原点为红色
        stop:0.5 white  断点为白色（可多个）
        stop:1 green  终点为绿色
        '''

        '''角度渐变
        background-color:qconicalgradient(cx:0.7, cy:0.7, angle:5, stop:0 red, stop:0.5 white, stop:1 green)
        cx:0.7, cy:0.7  光源中心点坐标
        angle:5  角度向上5度
        stop:0 red  原点为红色
        stop:0.5 white  断点为白色（可多个）
        stop:1 green  终点为绿色
        '''

        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()

    with open('base6.qss', 'r', encoding='UTF-8') as f:
        qApp.setStyleSheet(f.read())

    window.show()
    sys.exit(app.exec_())
