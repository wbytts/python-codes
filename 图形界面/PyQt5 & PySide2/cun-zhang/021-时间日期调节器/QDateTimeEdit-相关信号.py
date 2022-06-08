from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QDateTimeEdit日期和时间控件功能作用 - PyQt5中文网")
        self.resize(600, 500)
        self.func_list()

    def func_list(self):
        self.func()

    def func(self):
        self.qsb = QDateTimeEdit(self)
        self.qsb.resize(200, 40)
        self.qsb.move(150, 150)

        self.btn = QPushButton('按钮', self)
        self.btn.resize(60, 30)
        self.btn.move(150, 200)
        self.btn.pressed.connect(self.test)

    def test(self):
        '''
        # 时间显示格式
        self.qsb.setDisplayFormat('yyyy-mm-dd  mm:ss:zzz')
        # section控制
        print(self.qsb.sectionCount())
        self.qsb.setCurrentSectionIndex(2)  # 找到指定索引的section
        self.qsb.setCurrentSectionIndex(QDateTimeEdit.DaySection)  # 找到指定section的索引
        print(self.qsb.sectionText(QDateTimeEdit.DaySection))   # 获取指定位置文本内容

        # 日期时间范围
        self.qsb.setMaximumDateTime(QDateTime(2020,6,15,6,10))
        # 设定当前时间前后5天
        self.qsb.setDateTimeRange(QDateTime.currentDateTime().addDays(-5), QDateTime.currentDateTime().addDays(5))

        # 日历选择控件
        self.qsb.setCalendarPopup(True)
        # 获取时间和日期
        self.qsb.dateTime()
        '''
        # 可用信号
        self.qsb.dateTimeChanged.connect(lambda: print(self.qsb.dateTime()))
        self.qsb.timeChanged.connect(lambda: print(self.qsb.time()))
        self.qsb.dateChanged.connect(lambda: print(self.qsb.date()))

        # 时间(QTimeEdit)和日期(QDateEdit)控件与父控件(QDateTimeEdit)基本一样


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())
