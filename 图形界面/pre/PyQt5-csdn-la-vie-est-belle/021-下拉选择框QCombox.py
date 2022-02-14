import sys
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QFontComboBox, QLineEdit, QMessageBox, QVBoxLayout


class Demo(QWidget):
    choice = 'a'
    choice_list = ['b', 'c', 'd', 'e']

    def __init__(self):
        super(Demo, self).__init__()

        # 实例化一个QComboBox和QFontComboBox，前者是普通的下拉框，框里是没有内容的，需要添加。
        # 而QFontComboBox是字体下拉框，继承于QComboBox，该字体下拉框里会默认有许多字体供选择；
        self.combobox_1 = QComboBox(self)                   # 1
        self.combobox_2 = QFontComboBox(self)               # 2

        # 这里实例化一个单行文本输入框，用于测试从字体下拉框中选择一项时，输入框中字体发生的变化；
        self.lineedit = QLineEdit(self)                     # 3

        self.v_layout = QVBoxLayout()

        self.layout_init()
        self.combobox_init()

    def layout_init(self):
        self.v_layout.addWidget(self.combobox_1)
        self.v_layout.addWidget(self.combobox_2)
        self.v_layout.addWidget(self.lineedit)

        self.setLayout(self.v_layout)

    def combobox_init(self):
        # addItem()方法是添加一个选项，而addItems()接收一个可循环参数，这里传入了列表self.choice_list；
        self.combobox_1.addItem(self.choice)              # 4
        self.combobox_1.addItems(self.choice_list)        # 5

        # 当下拉框当前选项发生变化变化的话，则会触发序号变化currentIndexChanged信号和文本变化currentTextChanged信号，
        # 我们在这里进行了信号与槽的连接，注意槽函数是带参数的，所以我们用lambda表达式进行处理；
        self.combobox_1.currentIndexChanged.connect(lambda: self.on_combobox_func(self.combobox_1))   # 6
        # self.combobox_1.currentTextChanged.connect(lambda: self.on_combobox_func(self.combobox_1))  # 7

        self.combobox_2.currentFontChanged.connect(lambda: self.on_combobox_func(self.combobox_2))
        # self.combobox_2.currentFontChanged.connect(lambda: self.on_combobox_func(self.combobox_2))

    def on_combobox_func(self, combobox):                                                             # 8
        """
        在自定义的槽函数中，我们通过判断combobox的种类，若是self.combobox_1的话，则出现信息框，并且显示当前文本和及文本序号，
            currentIndex()方法获取当前文本序号，currentText()方法获取当前文本。
        若是self.combobox_2的话，则通过setFont()方法将输入框的字体设为当前选中的字体，currentFont()获取字体下拉框的当前字体。
        """
        if combobox == self.combobox_1:
            QMessageBox.information(self, 'ComboBox 1', '{}: {}'.format(combobox.currentIndex(), combobox.currentText()))
        else:
            self.lineedit.setFont(combobox.currentFont())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
