import sys
from PySide2.QtWidgets import (QLineEdit, QPushButton, QApplication,
                               QVBoxLayout, QDialog)


class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        # 创建组件，编辑框与按钮
        self.edit = QLineEdit("Write my name here")
        self.button = QPushButton("Show Greetings")
        # 创建一个垂直盒子布局
        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)
        # 设置布局
        self.setLayout(layout)
        # 连接按钮点击事件
        self.button.clicked.connect(self.greetings)

    # 槽函数
    def greetings(self):
        print("Hello %s" % self.edit.text())


if __name__ == '__main__':
    # 创建QT应用
    app = QApplication(sys.argv)
    # 创建并显示Form
    form = Form()
    form.show()
    # 运行主循环
    sys.exit(app.exec_())
