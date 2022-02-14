import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox, QVBoxLayout

"""
复选框一共有三种状态：全选中、半选中和无选中。
若一个父选项的子选项全部为选中状态，则该父选项为全选中；
若子选项全部为无选中状态，则该父选项为无选中状态；
若子选项既有全选中和无选中状态，则该父选项为半选中状态。
"""

class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.checkbox1 = QCheckBox('Checkbox 1', self)
        self.checkbox2 = QCheckBox('Checkbox 2', self)
        self.checkbox3 = QCheckBox('Checkbox 3', self)

        self.v_layout = QVBoxLayout()

        self.checkbox_init()
        self.layout_init()

    def layout_init(self):
        self.v_layout.addWidget(self.checkbox1)
        self.v_layout.addWidget(self.checkbox2)
        self.v_layout.addWidget(self.checkbox3)

        self.setLayout(self.v_layout)

    def checkbox_init(self):
        # 通过setChecked()方法传入True或者False可以将复选框设为选中或无选中状态；
        # 另外一种替代的方法是setCheckState()，
        # 传入的参数可以是选中状态Qt.Checked, 无选中状态Qt.Unchecked和半选中状态Qt.PartiallyChecked；
        self.checkbox1.setChecked(True)                                                             # 1
        # self.checkbox1.setCheckState(Qt.Checked)                                                  # 2
        #  stateChanged信号会在复选框状态发生改变的时候发出。
        # 这里我们发现槽函数是带参数的，可以通过lambda表达式来将参数传入槽函数。
        # 若单纯使用self.on_state_change_func(self.checkbox2)则会报错；
        self.checkbox1.stateChanged.connect(lambda: self.on_state_change_func(self.checkbox1))      # 3

        self.checkbox2.setChecked(False)
        # self.checkbox2.setCheckState(Qt.Unchecked)
        self.checkbox2.stateChanged.connect(lambda: self.on_state_change_func(self.checkbox2))

        #  如果要让一个复选框拥有三种状态，则必须通过setTristate(True)方法来实现。
        #  在这里我们让第三个复选框拥有三种状态；
        self.checkbox3.setTristate(True)                                                            # 4
        self.checkbox3.setCheckState(Qt.PartiallyChecked)                                           # 5
        self.checkbox3.stateChanged.connect(lambda: self.on_state_change_func(self.checkbox3))

    def on_state_change_func(self, checkbox):                                                       # 6
        """
        checkState()方法可以获取当前复选框的状态，
        返回值为int类型
            0为无选中状态
            1为半选中状态
            2为选中状态
        """
        print('{} was clicked, and its current state is {}'.format(checkbox.text(), checkbox.checkState()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
