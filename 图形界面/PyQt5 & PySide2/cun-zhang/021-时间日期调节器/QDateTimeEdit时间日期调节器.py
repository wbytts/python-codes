from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QDateTimeEdit时间和日期步长调节器 - PyQt5中文网")
        self.resize(600, 500)
        self.func_list()

    def func_list(self):
        self.func()

    def func(self):
        """
        QDateTimeEdit(parent: QWidget = None)
        QDateTimeEdit(Union[QDateTime, datetime.datetime], parent: QWidget = None)
        QDateTimeEdit(Union[QDate, datetime.date], parent: QWidget = None)
        QDateTimeEdit(Union[QTime, datetime.time], parent: QWidget = None)
        # 从构造函数可以看出，以下三个类没有继承关系
        QDateTime
        QDate
        QTime
        """
        """
        # 简单的构造方法
        self.qsb = QDateTimeEdit(self)  # 直接构造范围最小日期为：1752.9.14，最大日期为：9999.12.31
        self.qsb.resize(150, 40)
        self.qsb.move(150, 150)

        self.btn = QPushButton('按钮', self)
        self.btn.resize(60, 30)
        self.btn.move(150, 200)
        self.btn.pressed.connect(self.test)
        """
        # 传入QDateTime的一种构造方法
        # self.dt_tm = QDateTime(2020,1,15,11,31,55)
        self.dt_tm = QDateTime.currentDateTime()  # 当前时间
        self.dt_tm = self.dt_tm.addYears(2)  # 不会直接显示在控件中，要重新赋值
        self.dt_tm.offsetFromUtc()  # 此时与标准时间差

        self.qsb = QDateTimeEdit(self.dt_tm, self)
        self.qsb.resize(150, 40)
        self.qsb.move(150, 150)

        # QDate和QTime与上面差不多
        # 计时功能
        time = QTime.currentTime()
        time.start()
        btn = QPushButton(self)
        btn.clicked.connect(lambda: print(time.elapsed() / 1000))

        self.qsb1 = QDateTimeEdit(QDateTime.currentDateTime(), self)
        self.qsb2 = QDateTimeEdit(QDate.currentDate(), self)
        self.qsb3 = QDateTimeEdit(QTime.currentTime(), self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())
