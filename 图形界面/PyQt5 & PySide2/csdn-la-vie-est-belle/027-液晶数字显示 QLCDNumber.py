import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLCDNumber, QVBoxLayout
from qt_material import apply_stylesheet

class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(600, 600)

        # 实例化一个QLCDNumber控件，然后通过setDiditCount()方法来设置一共可以显示多少为数字；
        self.lcd_1 = QLCDNumber(self)
        self.lcd_1.setDigitCount(10)
        self.lcd_1.display(1234567890)


        self.lcd_2 = QLCDNumber(self)
        # 通过setSegmentStyle()可以设置显示屏数字样式
        '''
            QLCDNumber.Outline     0     让内容浮显，其颜色同显示屏背景颜色相同
            QLCDNumber.Filled      1     让内容浮显，颜色同窗口标题颜色相同
            QLCDNumber.Flat        2     让内容扁平化显示，颜色同窗口标题颜色相同
        '''
        self.lcd_2.setSegmentStyle(QLCDNumber.Flat)
        # setSmallDecimalPoint(bool)方法可以设置小数点的显示方式：若为True，那么小数点就会在两个数字之间显示出来，而不会单独占一个位置。如果为False，那就会单独占位(默认为False)。
        # self.lcd_2.setSmallDecimalPoint(True)
        self.lcd_2.setDigitCount(10)
        self.lcd_2.display(0.123456789)

        self.lcd_3 = QLCDNumber(self)
        # 可以显示的字母种类有限：A, B, C, D, E, F, h, H, L, o, P, r, u, U, Y, O/0, S/5,  g/9
        self.lcd_3.setSegmentStyle(QLCDNumber.Filled)
        self.lcd_3.display('HELLO')

        self.lcd_4 = QLCDNumber(self)
        # 可以通过setMode()方法来更改数字显示方式，这里用传入QLCDNumber.Hex让数字以16进制方式显示
        '''
            QLCDNumber.Hex
            QLCDNumber.Dec
            QLCDNumber.Oct
            QLCDNumber.Bin
        '''
        self.lcd_4.setSegmentStyle(QLCDNumber.Outline)
        self.lcd_4.setMode(QLCDNumber.Hex)
        self.lcd_4.setDigitCount(6)
        self.lcd_4.display(666)

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.lcd_1)
        self.v_layout.addWidget(self.lcd_2)
        self.v_layout.addWidget(self.lcd_3)
        self.v_layout.addWidget(self.lcd_4)

        self.setLayout(self.v_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_lightgreen.xml')
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
