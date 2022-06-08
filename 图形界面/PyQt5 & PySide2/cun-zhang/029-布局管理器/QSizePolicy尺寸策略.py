from PyQt5.Qt import *
import sys


class size_widget(QLabel):
    def sizeHint(self):
        return QSize(200, 200)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("布局管理器-尺寸策略size - PyQt5中文网")
        self.resize(600, 500)
        self.func_list()

    def func_list(self):
        self.func()

    def func(self):
        label1 = QLabel('标签1', self)
        label1.setStyleSheet('background-color:green')
        label2 = size_widget('标签2', self)
        label2.setStyleSheet('background-color:red')
        label3 = QLabel('标签3', self)
        label3.setStyleSheet('background-color:yellow')
        bl = QVBoxLayout()
        self.setLayout(bl)
        bl.addWidget(label1)
        bl.addWidget(label2)
        bl.addWidget(label3)

        # 策略取值
        # QSizePolicy.Fixed  # 按照控件本身尺寸取值
        # QSizePolicy.Minimum  # 可以伸缩尺寸，sizeHide已确定最小控件尺寸
        # QSizePolicy.Maximum  # 可以伸缩尺寸，sizeHide已确定最大控件尺寸
        # QSizePolicy.Preferred  # 可以伸缩尺寸，没有限制
        # QSizePolicy.Expanding  # 可以伸缩尺寸，相比上一个优先级更高
        # QSizePolicy.MinimumExpanding  # 可以伸缩尺寸......
        # QSizePolicy.Ignored  # 忽略sizeHide的作用，可以小到0
        # sp = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sp = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sp1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        label2.setSizePolicy(sp)
        label3.setSizePolicy(sp1)

        label3.setFixedSize(300, 300)  # 设置固定尺寸


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())
