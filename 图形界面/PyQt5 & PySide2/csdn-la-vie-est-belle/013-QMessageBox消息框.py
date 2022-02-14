import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.button = QPushButton('information', self)
        # 实例化一个QPushButton并将clicked信号与自定义的show_messagebox槽函数连接起来，这样点击按钮后，信号发出，槽函数就会启动；
        self.button.clicked.connect(self.show_messagebox)  # 1

    def show_messagebox(self):
        # 在槽函数中我们创建了一个信息框(information)，基本用法如下：
        # QMessageBox.information(QWidget, ‘Title’, ’Content‘, buttons)
        """
        第一个参数填self，表示该信息框属于我们这里的Demo窗口；
        第二个参数类型为字符串，填入的是该信息框的标题；
        第三个参数类型也是字符串，填入的是信息框的提示内容；
        最后个参数为信息框上要添加的按钮，
        在示例代码中我们添加了Yes、No和Cancel三个按钮，多个按钮之间用 | 来连接，
        常见的按钮种类有以下几种：
            QMessageBox.Ok
            QMessageBox.Yes
            QMessageBox.No
            QMessageBox.Close
            QMessageBox.Cancel
            QMessage.Open
            QMessage.Save
        如果你没有显示指定信息框的按钮，那信息框会自己默认加上合适的按钮上去 QMessageBox.information(self, 'Title', 'Content')
        当然还有其他类型的消息框 如：QMessageBox.question  QMessageBox.warning  QMessageBox.critical  QMessageBox.about
        """
        QMessageBox.information(self, 'Title', 'Content',
                                QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)  # 2


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
