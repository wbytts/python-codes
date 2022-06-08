from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QDial旋转按钮控件 - PyQt5中文网")
        self.resize(600, 500)
        self.func_list()

    def func_list(self):
        self.func()

    def func(self):
        slider = QDial(self)
        slider.resize(100, 100)
        slider.move(100, 100)
        # 显示刻度
        slider.setNotchesVisible(True)
        # 大刻度控制
        slider.setPageStep(20)
        # 启用包裹,消除缺口
        slider.setWrapping(True)
        # 缺口之间的差值密度
        slider.setNotchTarget(10.0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())
