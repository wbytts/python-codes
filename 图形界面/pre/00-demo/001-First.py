import sys

from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    # 创建QApplication实例
    app = QApplication(sys.argv)
    # 创建一个控件
    w = QWidget()
    # 调整控件的大小
    w.resize(400, 200)
    # 移动控件
    w.move(200, 200)
    # 显示控件
    w.show()
    # 开启程序的消息循环
    sys.exit(app.exec_())
