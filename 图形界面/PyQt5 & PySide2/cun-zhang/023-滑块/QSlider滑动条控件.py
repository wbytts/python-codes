from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QSlider刻度控件 - PyQt5中文网")
        self.resize(600, 500)
        self.func_list()

    def func_list(self):
        self.func()

    def func(self):
        label = QLabel(self)
        label.setText('0')
        label.resize(70, 50)
        label.move(150, 150)
        label.setStyleSheet('background-color:green;font-size:35px')

        slide = QSlider(self)
        slide.move(50, 50)
        slide.setOrientation(Qt.Horizontal)
        # QSlider.TicksBothSides    3
        # QSlider.NoTicks    0
        # QSlider.TicksRight    2
        # QSlider.TicksLeft    1
        # QSlider.TicksAbove    1
        # QSlider.TicksBelow    2

        slide.setTickPosition(QSlider.TicksAbove)
        # slide.setTickPosition(1)
        slide.setPageStep(5)  # 调整刻度和步长
        slide.setTickInterval(5)  # 只调整刻度，不调整步长


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())
