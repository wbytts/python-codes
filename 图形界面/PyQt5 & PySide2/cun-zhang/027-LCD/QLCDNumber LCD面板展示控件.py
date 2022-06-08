from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("展示控件-QLCDNumber面板显示控件 - PyQt5中文网")
        self.resize(600, 500)
        self.func_list()

    def func_list(self):
        self.func()

    def func(self):
        lcd = QLCDNumber(6, self)  # 6为展示数字的位数
        # lcd.setDigitCount(6)  # 单独设置展示位数
        lcd.move(150, 150)
        lcd.resize(300, 60)

        # 能展示的字符
        # 0 1 2 3 4 5 6 7 8 9
        # A B C D E F g h H L o s S P r u U Y
        # : ' 空格
        # lcd.display('A B C D E')
        lcd.display(123456)  # 整形超出最大展示数值之后就显示0
        # lcd.display(123.456)  # 浮点型只展示前6为，小数点为一位
        # lcd.display('123456')
        # print(lcd.intValue())  # 只能获取整型
        # print(lcd.value())  # 只能获取浮点类型

        # 模式设置,获取到的数值会自动转为十进制
        # lcd.setMode(QLCDNumber.Bin)  # 二进制      setBinMode()
        # lcd.setMode(QLCDNumber.Oct)  # 八进制      setOctMode()
        # lcd.setMode(QLCDNumber.Dec)  # 十进制      setDecMode()
        # lcd.setMode(QLCDNumber.Hex)  # 十六进制     setHexMode()

        # 溢出判断
        # print(lcd.checkOverflow(123456789))  # 返回布尔值

        # 分段样式 - 创建三个控件对比就知道了
        # lcd.setSegmentStyle(QLCDNumber.Outline)  # 生成填充背景色的凸起
        # lcd.setSegmentStyle(QLCDNumber.Filled)  # 生成填充前景色的凸起
        # lcd.setSegmentStyle(QLCDNumber.Flat)  # 生成填充前景色的平坦部分

        # 信号
        # lcd.overflow()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())
