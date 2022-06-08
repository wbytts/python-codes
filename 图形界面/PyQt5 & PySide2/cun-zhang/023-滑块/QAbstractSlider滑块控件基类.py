from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QAbstractSlider滑块控件基类 - PyQt5中文网")
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

        # QAbstractSlider是抽象类，只能借助子类来演示
        slide = QSlider(self)
        slide.move(50, 50)

        # 信号
        slide.valueChanged.connect(lambda val: label.setText(str(val)))
        # slide.valueChanged.connect(lambda :label.setText(slide.value()))

        # 数值范围
        slide.setMaximum(100)
        slide.setMinimum(0)

        # 当前数值
        slide.setValue(40)

        # 步长 - 使用键盘
        slide.setSingleStep(5)  # 使用上下键
        slide.setPageStep(10)  # 使用pageup和pagedown

        # 追踪设置
        # slide.setTracking(False)  # 鼠标松开后才会改变数值

        # 滑块位置
        slide.setSliderPosition(55)

        # 倒立外观
        slide.setInvertedAppearance(True)  # 包括上下键都会被改变

        # 操作反转
        slide.setInvertedControls(True)  # 改变上下键的值变化

        # 滑块方向
        slide.setOrientation(Qt.Horizontal)  # 改变滑块方向 水平

        # 是否按下
        slide.setSliderDown(False)  # 了解就可以了

        # 可用信号
        # slide.valueChanged()  # 滑块改变
        # slide.sliderPressed()
        # slide.sliderMoved()
        # slide.sliderReleased()
        # slide.actionTriggered()  # 行为触发
        # slide.rangeChanged()  # 数值范围改变
        slide.sliderMoved.connect(lambda val: print(val))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())
