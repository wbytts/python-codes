from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QDialog对话框控件 - PyQt5中文网")
        self.resize(600, 500)
        self.func_list()

    def func_list(self):
        self.func()

    def func(self):
        # 四种对话框和一个日期控件
        # QFontDialog
        # QColorDialog
        # QFileDialog
        # QInputDialog
        # QCalendarWidget

        # 用于短期任务或临时交互：
        # 1.模态对话框：应用程序级别(exce(),需要关闭交互窗口之后才能操作其他窗口==模态)
        # 2.模态对话框：窗口级别(open()仅阻塞关联窗口交互，不影响其他窗口的交互==模态)
        # 3.非模态对话框：show()
        # 模态（阻塞性）；非模态（不阻塞）

        # 模态演示
        qd = QDialog(self)
        qd.exec()
        # qd.open()  # 不关联的时候就能拖动

        # qd.setModal(True)  # 设置为模态窗口
        # qd.setWindowModality(Qt.WindowModal)  # 设置为窗口级别，Qt.ApplicaModal设置成应用程序级别
        # qd.show()

        # 尺寸调整
        qd.setSizeGripEnabled(True)  # 控件右下角显示

        # 槽函数
        # qd.accept()  # 接受
        # qd.reject()  # 取消
        # qd.done()  # 替代其他功能

        btn1 = QPushButton(qd)
        btn1.move(10, 10)
        btn1.setText('按钮1')
        btn1.clicked.connect(lambda: qd.accept())  # 接受，返回值为1

        btn2 = QPushButton(qd)
        btn2.move(60, 60)
        btn2.setText('按钮2')
        btn2.clicked.connect(lambda: qd.reject())  # 拒绝，返回值为0

        btn3 = QPushButton(qd)
        btn3.move(10, 100)
        btn3.setText('按钮3')
        btn3.clicked.connect(lambda: qd.done(5))  # 返回值为5

        '''
        # 设置和获取数值
        qd.setResult(int)
        qd.result()

        btn1 = QPushButton(qd)
        btn1.move(10, 100)
        btn1.setText('按钮1')
        btn1.clicked.connect(lambda: qd.setResult(111))

        btn2 = QPushButton(qd)
        btn2.move(60, 60)
        btn2.setText('按钮2')
        btn2.clicked.connect(lambda: print(qd.result()))
        '''

        # 可用信号
        # qd.accepted()
        # qd.finished()
        # qd.rejected()
        # qd.accepted.connect(lambda: print('接受'))
        # qd.finished.connect(lambda: print('取消'))
        # qd.rejected.connect(lambda val: print('接受', val))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())
