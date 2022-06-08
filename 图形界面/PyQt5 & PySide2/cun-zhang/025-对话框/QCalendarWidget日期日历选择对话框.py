from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QCalendarWidget日期日历控件 - PyQt5中文网")
        self.resize(600, 500)
        self.func_list()

    def func_list(self):
        self.func()

    def func(self):
        qcw = QCalendarWidget(self)
        # 日期范围
        # qcw.setMaximumDate(QDate(2020, 12, 31))
        # qcw.setMinimumDate(QDate(1990, 1, 1))
        qcw.setDateRange(QDate(1990, 1, 1), QDate(2020, 12, 31))

        # 日期编辑
        # qcw.setDateEditEnabled(False)

        # 日期获取
        print(qcw.monthShown())
        print(qcw.yearShown())
        print(qcw.selectedDate())

        # 外观控制
        qcw.setNavigationBarVisible(False)  # 头部栏隐藏
        qcw.setFirstDayOfWeek(Qt.Sunday)  # 控制一周的第一天
        qcw.setGridVisible(True)  # 日期网格显示

        # 文本格式控制
        tcf = QTextCharFormat()
        # tcf.setFontFamily('宋体')
        tcf.setFont(QFont('宋体', 20, 50))
        # qcw.setHeaderTextFormat(tcf)

        # QCalendarWidget.SingleLetterDayNames  # 周
        # QCalendarWidget.ShortDayNames  # 周一
        # QCalendarWidget.LongDayNames  # 星期一
        # QCalendarWidget.NoHorizontalHeader  # 标题隐藏
        qcw.setHorizontalHeaderFormat(QCalendarWidget.LongDayNames)  # 水平显示设置

        # QCalendarWidget.ISOWeekNumbers  # 显示周数
        # QCalendarWidget.NoVerticalHeader  # 隐藏标题
        qcw.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)  # 垂直显示设置

        qcw.setWeekdayTextFormat(Qt.Monday, tcf)  # 特定星期文本字符格式

        qcw.setDateTextFormat(QDate(2020, 12, 30), tcf)  # 特定日期文本字符格式

        # 选中功能
        qcw.setSelectionMode(QCalendarWidget.NoSelection)  # 日期无法选择
        # qcw.setSelectionMode(QCalendarWidget.SingleSelection)  # 可以选择单个日期
        qcw.setSelectedDate(QDate(2020, 12, 1))  # 一般用于给用户展示某个日期

        # 常用方法
        qcw.showToday()  # 只展示当天所在页面，不选中
        qcw.showSelectedDate()
        qcw.showNextMonth()
        qcw.showNextYear()
        qcw.showPreviousYear()  # 前一年
        qcw.showPreviousMonth()
        qcw.setCurrentPage(2020, 11)  # 设置当前页面是哪一年那一月

        # 可用信号
        qcw.activated()  # 双击触发
        qcw.clicked()  # 点击触发
        qcw.currentPageChanged()  # 当前月份改变
        qcw.selectionChanged()  # 当前选择的日期发生改变


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())
