from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("信号和槽")
        self.resize(600, 500)
        self.func_list()

    def func_list(self):
        self.func()
        self.on_btn_clicked()

    def func(self):
        btn = QPushButton('按钮', self)
        btn.setObjectName('btn')
        btn.resize(80, 50)
        btn.move(100, 100)

        btn2 = QPushButton('按钮', self)
        btn2.setObjectName('btn2')
        btn2.resize(80, 50)
        btn2.move(100, 200)

        # 表示把window对象中的子对象按照objectName链接到相关的槽函数上，必须放在所有子控件的最后
        QMetaObject.connectSlotsByName(self)


    # on_xxx 中间夹上，所要连接的控件的名称，注：是控件名称，不是变量名称
    @pyqtSlot(bool)  # 这里bool表示按钮有没有被选中
    def on_btn_clicked(self):  # 注意命名规则
        print('点击按钮')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())
