from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("布局管理器-堆叠布局QStackedLayout - PyQt5中文网")
        self.resize(600, 500)
        self.func_list()

    def func_list(self):
        self.func()

    def func(self):
        # sl = QStackedLayout()
        # self.setLayout(sl)  # 这里作为第二步不能改变，否则会不稳定
        sl = QStackedLayout(self)  # 可以直接取代上面两步

        label1 = QLabel('标签1', self)
        label1.setStyleSheet('background-color:green')
        label2 = QLabel('标签2', self)
        label2.setStyleSheet('background-color:red')
        label3 = QLabel('标签3', self)
        label3.setStyleSheet('background-color:yellow')

        label4 = QLabel('标签4', self)
        label4.setStyleSheet('background-color:green')

        sl.addWidget(label1)
        sl.addWidget(label2)
        sl.addWidget(label3)

        # 根据索引位置插入和获取
        print(sl.insertWidget(0, label4))  # 依然展示label1，但是索引值变成1
        print(sl.widget(0).text())

        # 界面切换方法
        # sl.setCurrentIndex(2)  # 直接设置索引显示
        sl.setCurrentWidget(label2)  # 直接调出控件显示

        # timer = QTimer(self)
        # timer.timeout.connect(lambda :sl.setCurrentIndex((sl.currentIndex() + 1) % sl.count()))
        # timer.start(200)

        # 展示模式
        # QStackedLayout.StackAll
        # QStackedLayout.StackOne  # 只显示当前控件hide()后就没有控件显示了
        sl.setStackingMode(QStackedLayout.StackAll)  # 所有都可见之后，把标签1缩小就能见到后面的控件了
        label2.setFixedSize(100, 100)
        label1.setFixedSize(200, 200)

        # 信号
        # sl.currentChanged()
        # sl.widgetRemoved()  # 控件被移除
        sl.removeWidget(label3)  # 控件被移除后后面的控件会自动显示


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())
