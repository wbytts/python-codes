from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("布局管理器-表单布局QFormLayout - PyQt5中文网")
        self.resize(600, 500)
        self.func_list()

    def func_list(self):
        self.func()

    def func(self):
        name_label = QLabel('姓名：')
        age_label = QLabel('年龄：')
        tel_label = QLabel('号码：')

        name_line = QLineEdit()
        age_line = QSpinBox()
        tel_line = QLineEdit()

        sub_btn = QPushButton('提交')

        man_btn = QRadioButton('男')
        woman_btn = QRadioButton('女')
        check_btn = QFormLayout()
        check_btn.addRow(man_btn, woman_btn)

        # 1.创建布局管理器
        form = QFormLayout()

        # 2.行操作
        # 1.1.添加行
        # form.addWidget(name_label)
        # form.addWidget(name_line)
        # form.addRow(name_label, name_line)
        form.addRow(name_label, name_line)  # 字符串被自动解释为标签控件
        form.addRow('性别：', check_btn)
        form.addRow(tel_label, tel_line)
        form.addRow(sub_btn)

        # 1.2.插入行(和上面的添加行一样，仅多一个位置整形数字)
        # form.insertRow(2, sub_btn)  # int超出范围后直接加在最后

        # 1.3.移除行
        # form.removeRow(tel_label)  # 删除子控件,同时删除整行
        # form.takeRow(2)  # 不删除子控件
        ''''''
        # 1.4.修改行（一行中两个角色的分别控制）
        # QFormLayout.LabelRole  # 标签角色
        # QFormLayout.FieldRole  # 输入框角色
        # QFormLayout.SpanningRole  # 整体行（包括输入框和标签）
        form.setWidget(0, QFormLayout.LabelRole, tel_label)  # 如果0位置已经有控件，修改不会成功
        form.setWidget(0, QFormLayout.FieldRole, tel_line)
        # form.setLayout(1, QFormLayout.FieldRole, check_btn)

        # 1.5.获取行信息
        print(form.rowCount())
        # print(form.getWidgetPosition(name_line))
        print(form.getLayoutPosition(check_btn))

        # 1.6.标签操作
        form.labelForField(name_label.setText('name' * 8))

        # 1.7.包装策略
        # QFormLayout.DontWrapRows  # 字段一直在标签旁边
        # QFormLayout.WrapLongRows  # 标签文本过长，字段自动换行
        # QFormLayout.WrapAllRows  # 字段一直位于标签下方
        form.setRowWrapPolicy(QFormLayout.WrapLongRows)

        # 1.8.对齐和间距
        form.setFormAlignment(Qt.AlignRight | Qt.AlignBottom)  # 表单对齐
        form.setLabelAlignment(Qt.AlignRight)  # 标签对齐
        form.setHorizontalSpacing(30)
        form.setVerticalSpacing(30)

        # 1.9.字段增长策略
        # QFormLayout.FieldsStayAtSizeHint  # 字段宽度不变
        # QFormLayout.ExpandingFieldsGrow  # 字段宽度自适应变化
        # QFormLayout.AllNonFixedFieldsGrow  # 用的不多
        form.setFieldGrowthPolicy(QFormLayout.FieldsStayAtSizeHint)

        # 2.为父控件添加布局管理器
        self.setLayout(form)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())
