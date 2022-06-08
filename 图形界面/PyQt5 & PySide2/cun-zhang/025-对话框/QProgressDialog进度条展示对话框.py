from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("展示控件对话框-QProgressDialog进度条 - PyQt5中文网")
        self.resize(600, 500)
        self.func_list()

    def func_list(self):
        self.func()

    def func(self):
        # 构造函数
        # qpd = QProgressDialog(self)
        qpd = QProgressDialog('提示信息', '退出', 50, 100, self)  # 不需要手动输出，自动弹出，默认自小弹出时长4秒
        qpd.setWindowTitle('下载进度')

        qpd.setMinimumDuration(0)  # 0秒之后打开对话框
        qpd.setRange(50, 100)
        qpd.setValue(75)

        # qpd.setAutoClose(False)
        # qpd.setAutoReset(False)
        # for i in range(0, 101):
        #     qpd.setValue(i)

        # 数据处理
        qpd = QProgressDialog(self)
        qpd.setLabelText('下载进度')
        qpd.setCancelButtonText('取消')
        qpd.setRange(0, 100)

        qpd.wasCanceled()  # 是否取消
        qpd.setAutoClose(False)  # 进度条满格之后不会自动关闭
        qpd.setAutoReset(False)  # 进度条加载结束后不会重置

        # 案例
        time = QTimer(qpd)

        def test():
            if qpd.value() + 1 >= qpd.maximum() or qpd.wasCanceled():
                time.stop()
            qpd.setValue(qpd.value() + 1)

        time.timeout.connect(test)
        time.start(500)

        # 可用信号
        # qpd.canceled.connect()

        qpd.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())
