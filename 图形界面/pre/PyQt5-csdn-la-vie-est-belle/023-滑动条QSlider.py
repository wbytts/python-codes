import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QLabel, QVBoxLayout, QHBoxLayout


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        # 通过传入Qt.Hrizontal可以实例化一个水平的滑动条，传入Qt.Vertical的话可以实例化一个垂直的滑动条；
        self.slider_1 = QSlider(Qt.Horizontal, self)                                       # 1
        # 通过setRange()方法可以设置滑动条的范围；
        self.slider_1.setRange(0, 100)                                                     # 2
        # 当滑动时，数值发生改变，触发valueChanged信号；
        self.slider_1.valueChanged.connect(lambda: self.on_change_func(self.slider_1))     # 3

        self.slider_2 = QSlider(Qt.Vertical, self)
        # 除了setRange()方法，还可以使用setMinimum()和setMaximum()方法来设置最小值和最大值；
        self.slider_2.setMinimum(0)                                                        # 4
        self.slider_2.setMaximum(100)                                                      # 5
        # 数值变化信号
        self.slider_2.valueChanged.connect(lambda: self.on_change_func(self.slider_2))

        # 这里实例化的QLabel是为了显示出QSlider当前的数值；
        self.label = QLabel('0', self)                                                     # 6
        self.label.setFont(QFont('Arial Black', 20))

        self.h_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()

        self.h_layout.addWidget(self.slider_2)
        self.h_layout.addStretch(1)
        self.h_layout.addWidget(self.label)
        self.h_layout.addStretch(1)

        self.v_layout.addWidget(self.slider_1)
        self.v_layout.addLayout(self.h_layout)

        self.setLayout(self.v_layout)

    def on_change_func(self, slider):                                                       # 7
        """
        在自定义的槽函数中，将两个滑动条的数值同步，然后用QLabel显示出当前数值。
        """
        if slider == self.slider_1:
            self.slider_2.setValue(self.slider_1.value())
            self.label.setText(str(self.slider_1.value()))
        else:
            self.slider_1.setValue(self.slider_2.value())
            self.label.setText(str(self.slider_2.value()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
