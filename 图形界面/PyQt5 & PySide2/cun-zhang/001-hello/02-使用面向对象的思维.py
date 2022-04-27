from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()  # 调用父类QWidget中的init方法
        self.setWindowTitle("软件名称")
        self.resize(600, 500)
        self.func_list()

    def func_list(self):
        self.func()

    def func(self):
        btn = QPushButton(self)
        btn.setText("软件内容")
        btn.resize(120, 30)
        btn.move(100, 100)
        btn.setStyleSheet('background-color:green;font-size:20px;')


if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建一个应用程序对象
    # sys.argv可以接收用户命令行启动时所输入的参数，根据参数执行不同程序
    # qApp 为全局对象
    print(sys.argv)
    print(app.arguments())
    print(qApp.arguments())
    # 以上三个输出结果是一样的
    window = Window()

    window.show()
    sys.exit(app.exec_())  # 0是正常退出
    # app.exec_()  进行循环
    # sys.exit()   检测退出原因
