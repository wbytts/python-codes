from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("展示控件-QProgressBar进度条展示控件 - PyQt5中文网")
        self.resize(600, 500)
        self.func_list()

    def func_list(self):
        self.func()

    def func(self):
        pgb = QProgressBar(self)
        pgb.move(150, 150)
        # pgb.resize(200, 30)

        # pgb.setMinimum(0)
        # pgb.setMaximum(100)

        pgb.setRange(0, 100)
        # pgb.setRange(0, 0)  # 繁忙状态
        pgb.setValue(65)

        # pgb.reset()  # 重置进度条,当前值会变成最小值减一
        # pgb.value()  # 获取进度

        # 格式设置
        # %p:百分比   %v:当前值   %m:总值
        # pgb.setFormat('当前进度:%v , 总共:%m , 下载比例:%p%')
        pgb.setFormat('当前进度:{}'.format(pgb.value() - pgb.minimum()))
        # pgb.resetFormat()  # 重置数据
        pgb.setAlignment(Qt.AlignHCenter)  # 下载进度水平居中

        # 文本操作
        pgb.setTextVisible(True)
        print(pgb.text())

        pgb.setOrientation(Qt.Vertical)  # 垂直拜访
        # pgb.setOrientation(Qt.Horizontal)  # 水平拜访

        # 倒立外观
        pgb.setInvertedAppearance(True)

        # 可用信号
        # pgb.valueChanged()
        time = QTimer(pgb)

        def test():
            if pgb.value() == pgb.maximum():
                time.stop()
            pgb.setValue(pgb.value() + 5)

        time.timeout.connect(test)
        time.start(1000)
        pgb.valueChanged.connect(lambda val: print('当前下载', val))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())
