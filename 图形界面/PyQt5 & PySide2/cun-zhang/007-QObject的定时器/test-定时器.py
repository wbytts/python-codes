from PyQt5.Qt import *
import sys


class Obj(QObject):
    def timerEvent(self, timer_event):
        print(timer_event, 2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()

    obj = Obj()
    timer_id = obj.startTimer(1000)  # 这里的单位是毫秒！
    # obj.killTimer(timer_id)  # 指定定时器id，终止定时器
    window.show()
    sys.exit(app.exec_())


