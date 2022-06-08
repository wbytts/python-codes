from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QSS-语法声明-边框的样式、宽度、颜色设置")
        self.resize(600, 500)
        self.func_list()

    def func_list(self):
        self.func()

    def func(self):
        label1 = QLabel('标签1', self)
        label1.move(100, 200)
        label1.resize(100, 50)
        label2 = QLabel('标签2', self)
        label2.move(250, 200)
        label2.resize(100, 50)
        # 1.认识盒子模型(margin外边距,border边框,padding内边距,content内容矩形)(样式、宽度、颜色)
        '''样式声明
        border-style
        border-top-style
        border-right-style
        border-bottom-style
        border-left-style

        # 边框样式属性
        none  无边框
        dotted  点状
        dashed  虚线
        solid  实线
        double  双实线
        groove  定义 3D 凹槽边框。其效果取决于 border-color 的值
        ridge   定义 3D 垄状边框。其效果取决于 border-color 的值
        inset  定义 3D inset 边框。其效果取决于 border-color 的值
        outset  定义 3D outset 边框。其效果取决于 border-color 的值
        '''

        '''
        QLabel{
            border-style:dotted dashed solid double;  // 上 右 下 左
        }
        '''

        '''边框宽度声明
        border-width
        border-top-width
        border-right-width
        border-bottom-width
        border-left-width
        QLabel{
            border-width:2px 5px 10px 15px;  // 上 右 下 左
            border-width:2px 10px;  // 上下  左右
            border-style:solid;
            border-color:red;
        }
        16px == 1em
        '''

        '''边框颜色声明
        border-color
        border-top-color
        border-right-color
        border-bottom-color
        border-left-color
        QLabel{
            border-color:green black blue red;  // 上 右 下 左
            border-color:green black;  // 上下  左右
            border-style:solid;
            border-width:5px;
        }
        rgb(255, 255, 255)
        #ffffff
        '''


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()

    with open('base3.qss', 'r', encoding='UTF-8') as f:
        qApp.setStyleSheet(f.read())

    window.show()
    sys.exit(app.exec_())
