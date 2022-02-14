import sys
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QDial, QLabel, QHBoxLayout


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        # setWindowTitle()方法可以设置窗口标题；
        self.setWindowTitle('QDial')                            # 1

        self.dial = QDial(self)
        # 实例化一个QDial控件后，通过setFixedSize()方法来固定QDial的大小。
        # 如果不设置该方法的话，我们会发现在改变表盘数值时，表盘的大小会发生改变；
        self.dial.setFixedSize(100, 100)                        # 2
        # 使用setRange()方法来设置表盘数值范围，当然也可以使用setMinimum()和setMaximum()方法；
        self.dial.setRange(0, 100)                              # 3
        # setNotchesVisible(True)可以显示刻度，刻度会根据我们设置的数值自动调整；
        self.dial.setNotchesVisible(True)                       # 4
        # 当改变表盘数值时，会触发valueChanged信号，在槽函数中我们让QLabel显示出当前表盘数值。
        self.dial.valueChanged.connect(self.on_change_func)     # 5

        self.label = QLabel('0', self)
        self.label.setFont(QFont('Arial Black', 20))

        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.dial)
        self.h_layout.addWidget(self.label)

        self.setLayout(self.h_layout)

    def on_change_func(self):
        self.label.setText(str(self.dial.value()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
