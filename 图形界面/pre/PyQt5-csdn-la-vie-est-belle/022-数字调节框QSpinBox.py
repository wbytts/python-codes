import sys
from PyQt5.QtWidgets import QApplication, QWidget, QSpinBox, QDoubleSpinBox, QHBoxLayout


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        # 给实例化的QSpinBox设置范围，如果不设置的话QSpinBox默认范围为0-99；
        self.spinbox = QSpinBox(self)
        self.spinbox.setRange(-99, 99)                                                      # 1
        # 设置步长，即每次点击递增或递减多少值；
        self.spinbox.setSingleStep(1)                                                       # 2
        #  设置初始显示值；
        self.spinbox.setValue(66)                                                           # 3
        # 每次数字发生变化都会触发valueChanged信号；
        self.spinbox.valueChanged.connect(self.value_change_func)                           # 4

        # QSpinBox为整型数字调节框，而QDoubleSpinBox为浮点型数字调节框。
        # QDoubleSpinBox的默认范围为0.00-99.99，而小数位数默认是两位，不过可以通过setDecimals(int)方法来设置小数位数；
        self.double_spinbox = QDoubleSpinBox(self)                                          # 5
        self.double_spinbox.setRange(-99.99, 99.99)
        self.double_spinbox.setSingleStep(0.01)
        self.double_spinbox.setValue(66.66)

        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.spinbox)
        self.h_layout.addWidget(self.double_spinbox)
        self.setLayout(self.h_layout)

    def value_change_func(self):
        """
        该槽函数主要是在QSpinBox数值发生变化时，将QDoubleSpinBox的整数部分设置成QSpinBox的值，小数部分保持不变。
        所以要首先获取QDoubleSpinBox的小数部分再进行设置。通过setValue()方法可以设置调节框的值，而value()方法是获取值。
        """
        decimal_part = self.double_spinbox.value() - int(self.double_spinbox.value())       # 6
        self.double_spinbox.setValue(self.spinbox.value() + decimal_part)                   # 7


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
