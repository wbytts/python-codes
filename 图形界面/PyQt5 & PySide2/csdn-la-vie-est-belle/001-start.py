from PyQt5.Qt import *
# from PyQt5.QtWidgets import QApplication, QLabel
import sys

if __name__ == '__main__':
    # 1 想要创建应用必须先实例化一个QApplication，并将sys.argv作为参数传入
    app = QApplication(sys.argv)
    # 2 实例化一个QLabel控件，该控件用来展示文字或图片(可以想象下衣服标签，上面既有文字也有图片)，这里用于展示文本。
    label = QLabel('Hello World')
    # 3 通过调用show()方法使控件可见(默认是隐藏)；
    label.show()
    # 4 app.exec_()是执行应用，让应用开始运转循环，直到窗口关闭返回0给sys.exit()，退出整个程序。
    sys.exit(app.exec())

"""
注意：
    在Python2中exec是关键字，所以PyQt5就使用exec_()而不是exec() 。
    不过exec在Python3中已经不再是关键字了，所以如果读者使用的是Python3的话那在上述代码中用exec()也完全没关系。
"""
