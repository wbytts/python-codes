from PyQt5.Qt import *
import sys


# class Obj(QObject):
#     def timerEvent(self, QTimerEvent):
#         print(QTimerEvent, 2)


class Label(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resize(80, 40)
        self.move(100, 100)
        self.setStyleSheet("background-color:#02CDB9;font-size:25px")
        self.set_init_sec(100)
        self.set_time_step(500)
        self.timer_id = self.startTimer(self.time_step)

    def set_init_sec(self, sec):
        self.setText(str(sec))

    def set_time_step(self, step):
        self.time_step = str(step)

    def timerEvent(self, *args, **kwargs):
        print('事件案例演示')
        # 获取text中的数据
        sec = int(self.text())
        # 倒计时
        sec -= 1
        self.setText(str(sec))
        # 停止计时
        if sec == 0:
            self.killTimer(self.timer_id)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()
    window.resize(600, 500)
    label = Label(window)

    window.show()
    sys.exit(app.exec_())
