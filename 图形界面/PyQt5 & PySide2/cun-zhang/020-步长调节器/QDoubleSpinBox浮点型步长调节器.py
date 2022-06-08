from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QDoubleSpinBox-处理浮点型步长调节器 - PyQt5中文网")
        self.resize(600, 500)
        self.func_list()

    def func_list(self):
        self.func()

    def func(self):
        self.qsb = QDoubleSpinBox(self)  # 直接构造范围是0-99.99,步长为1.0
        self.qsb.resize(100, 30)
        self.qsb.move(150, 150)

        self.btn = QPushButton('按钮', self)
        self.btn.resize(60, 30)
        self.btn.move(150, 200)
        self.btn.pressed.connect(self.test)

    def test(self):
        # 修改最大值
        self.qsb.setMaximum(9.99)
        self.qsb.setMinimum(-5.2)
        print(self.qsb.minimum())
        self.qsb.setRange(-5.2, 9.99)
        # 数值循环
        self.qsb.setWrapping(True)
        # 设置步长
        self.qsb.setSingleStep(0.07)

        # 设置前缀和后缀
        self.qsb.setPrefix('%')
        self.qsb.setSuffix('$')
        # self.qsb.setRange(0.5,5.5)
        # self.qsb.setPrefix('周')
        # self.qsb.setSpecialValueText('周日')  # 设置最小值字符串
        # 小数位数设置
        self.qsb.setDecimals(1)

        # 获取或设置文本框数值
        # self.qsb.setRange(1,25)  # 这里设置之后下面数值设置超过范围内则显示这里的最大值
        self.qsb.setValue(50)
        print(self.qsb.value())  # 只能拿到数值
        print(self.qsb.cleanText())  # 获取文本字符串，不包括前后缀和空格
        print(self.qsb.text())  # 能拿到数值和前缀
        print(self.qsb.lineEdit().text())  # 能拿到数值和前缀

        # 自定义展示格式,重写方法，在上面Qsb中

        # 可用信号
        self.qsb.valueChanged[float].connect(lambda val: print(type(val)))
        self.qsb.valueChanged[str].connect(lambda val: print(type(val)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())
