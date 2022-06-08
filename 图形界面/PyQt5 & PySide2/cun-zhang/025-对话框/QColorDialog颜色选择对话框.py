from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QColorDialog颜色选择对话框 - PyQt5中文网")
        self.resize(600, 500)
        self.func_list()

    def func_list(self):
        self.func()

    def func(self):
        cd = QColorDialog(self)
        cd.setCustomColor(3, QColor(100, 120, 5))  # 3为位置下标
        # 默认颜色设置
        cd = QColorDialog(QColor(155, 200, 20), self)

        '''
        # 使用show()设置背景色
        def color(col):
            pal = QPalette()
            pal.setColor(QPalette.Background, col)  # 选择背景界面，插入颜色对象
            self.setPalette(pal)  # 设置背景色
        cd.colorSelected.connect(color)
        cd.show()  # show()没有返回值，所以需要借助上面的槽函数完成背景色设置

        # 使用open()设置背景色
        def color():
            pal = QPalette()
            pal.setColor(QPalette.Background, cd.selectedColor())  # 选择背景界面，获取选中颜色
            self.setPalette(pal)  # 设置背景色
        cd.open(color)  # open()直接当成链接信号

        # 使用exec()设置背景色
        def color():
            pal = QPalette()
            pal.setColor(QPalette.Background, qd.selectedColor())  # 选择背景界面，获取选中颜色
            self.setPalette(pal)  # 设置背景色
        if cd.exec():  # 拥有返回值，直接调用color函数进行设置
            color()
        '''

        # 选项控制
        '''
        # QColorDialog.ShowAlphaChannel  # 颜色透明度设置
        # QColorDialog.NoButtons  # 不现实OK和取消按钮
        def color():
            pal = QPalette()
            pal.setColor(QPalette.Background, qd.currentColor())  # 选择背景界面，获取当前颜色
            self.setPalette(pal)  # 设置背景色
        cd.currentColorChanged.connect(color)  # 链接信号
        cd.setOptions(QColorDialog.NoButtons | QColorDialog.ShowAlphaChannel)
        cd.show()
        '''

        # 静态方法
        # QColorDialog.customCount()
        # QColorDialog.setCustomColor()
        # QColorDialog.customColor()
        # QColorDialog.setCustomColor()
        # QColorDialog.getColor()
        cd.show()
        # btn.clicked.connect(lambda: print(QColorDialog.customCount()))  # 静态方法可以使用类调用也可以使用对象调用
        # btn.clicked.connect(lambda: print(qd.customCount()))  # 静态方法可以使用类调用也可以使用对象调用
        # 0是第一个颜色框，但是这里没有办法显示，是因为setCustomColor必须创建在qd之前
        # btn.clicked.connect(lambda: print(qd.setCustomColor(0, QColor(100, 120, 5))))  # 返回22和23行


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())
