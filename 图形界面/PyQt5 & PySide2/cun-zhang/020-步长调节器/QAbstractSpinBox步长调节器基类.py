from PyQt5.Qt import *
import sys


class Sun_asb(QAbstractSpinBox):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.lineEdit().setText('0')  # 设置一个默认值，作为容错

    def stepEnabled(self):  # 来判断上下是否有效
        num = int(self.text())
        if num == 0:
            return QAbstractSpinBox.StepUpEnabled
        elif num == 9:
            return QAbstractSpinBox.StepDownEnabled
        elif num < 0 or num > 9:
            return QAbstractSpinBox.StepNone
        else:
            return QAbstractSpinBox.StepUpEnabled | QAbstractSpinBox.StepDownEnabled

    def stepBy(self, r_int):  # 设置步长
        # print(r_int)
        num = int(self.text()) + r_int * 2  # 获取步长加上原有的数值
        self.lineEdit().setText(str(num))
        # self没有setText方法，所以要使用lineEdit来处理，因为self是一个组合控件，其中包含一个单行文本编辑器，这里的数值是直接插入单行文本编辑器中的，所以借助QLineEdit

    def validate(self, a_str, a_int):
        num = int(a_str)
        if num < 18:
            return (QValidator.Intermediate, a_str, a_int)
        elif num <= 180:
            return (QValidator.Acceptable, a_str, a_int)
        else:
            return (QValidator.Invalid, a_str, a_int)

    def fixup(self, a_str):
        return '18'


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QAbstractSpinBox步长调节器抽象基类 - PyQt5中文网")
        self.resize(600, 500)
        self.func_list()

    def func_list(self):
        self.func()

    def func(self):
        # 三种步长调节器：整形、浮点型、时间
        # QSpinBox
        # QDoubleSpinBox
        # QDateTimeEdit
        self.asb = Sun_asb(self)
        self.asb.resize(100, 30)
        self.asb.move(200, 50)
        # 子类化、实现控制方法，实现步长调节

        # 加速调节步长
        # self.asb.setAccelerated(True)

        # 只读设置，只允许步长调节器来改变内容
        # self.asb.setReadOnly(True)

        # 设置和获取步长调节器中的文本内容
        self.btn = QPushButton(self)
        self.btn.move(200, 100)
        self.btn.setText('按 钮')

        self.btn.pressed.connect(self.pre_btn)

    def pre_btn(self):
        print(self.asb.text())
        # self.asb.lineEdit().setText('55')
        self.asb.lineEdit().setToolTip('获取数据')

        # 对齐方式
        self.asb.setAlignment(Qt.AlignRight)

        # 设置周边框架
        print(self.asb.hasFrame())
        self.asb.setFrame(False)

        # 清空文本框内容
        self.asb.clear()

        # 设置上下键样式
        # QAbstractSpinBox.NoButtons
        # QAbstractSpinBox.UpDownArrows
        # QAbstractSpinBox.PlusMinus
        self.asb.setButtonSymbols(QAbstractSpinBox.UpDownArrows)

        # 文本内容验证
        # 在上面的类中写 validate()

        # 可用信号
        self.asb.editingFinished.connect(lambda: print(123))  # 结束编辑时调用


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())
