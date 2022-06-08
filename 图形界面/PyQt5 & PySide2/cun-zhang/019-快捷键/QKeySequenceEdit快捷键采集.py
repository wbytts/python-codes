from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QKeySequenceEdit-快捷键设置 - PyQt5中文网")
        self.resize(600, 500)
        self.func_list()

    def func_list(self):
        self.func()

    def func(self):
        # 设置快捷键
        kse = QKeySequenceEdit(self)
        ks = QKeySequence('Ctrl+A')  # 直接使用字符串设置
        # ks = QKeySequence(QKeySequence.Copy)  # 使用枚举值设置
        # ks = QKeySequence(Qt.CTRL + Qt.Key_C, Qt.CTRL + Qt.Key_A)  # 使用枚举值设置
        kse.setKeySequence(ks)

        # 获取快捷键
        # print(kse.keySequence())  # 获取快捷键对象
        # print(kse.keySequence().toString())  # 获取快捷键

        # 清除
        # kse.clear()

        # 信号
        # editingFinished()  # 结束编辑时
        # keySequenceChanged()  # 键位序列发生改变时
        kse.editingFinished.connect(lambda: print('AAAA'))  # 结束之后一秒
        # kse.keySequenceChanged.connect(lambda val: print('AAAA', val.toString()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())
