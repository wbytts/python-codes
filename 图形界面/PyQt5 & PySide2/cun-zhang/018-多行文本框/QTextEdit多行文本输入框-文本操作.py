from PyQt5.Qt import *
import sys

'''
占位提示文本：
setPlaceholderText()   placeholderText()
'''


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTextEdit - PyQt5中文网")
        self.resize(600, 500)
        self.func_list()

    def func_list(self):
        self.func()
        # self.place_hold()
        self.text_set()

    def func(self):
        self.qte = QTextEdit('111', self)
        self.qte.move(100, 100)
        self.qte.resize(250, 250)
        self.qte.setStyleSheet('background-color:green')
        self.qte.setFrameStyle(QFrame.Box | QFrame.Raised)
        self.qte.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.qte.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        self.btn = QPushButton('按  钮', self)
        self.btn.move(120, 50)
        self.btn.resize(70, 30)
        self.btn.pressed.connect(self.text_cur)

    # ==============占位提示文本=============== # 代码分割线 - 开始
    #     def place_hold(self):
    #         self.qte.setPlaceholderText('在这里输入文本内容')
    # ==============占位提示文本=============== # 代码分割线 - 结束

    # ==============内容设置=============== # 代码分割线 - 开始
    # 普通文本和富文本
    def text_set(self):
        # self.qte.setPlainText('<h1>AAAAA</h1>')
        # self.qte.insertPlainText('<h1>AAAAA</h1>')  # 这个方法不会清空原有的setText()中的文本内容，文本会放在前面
        # print(self.qte.toPlainText())  # 获取
        # self.qte.setHtml('<h1>AAAAA</h1>')   # 插入富文本
        # self.qte.insertHtml('<h1>AAAAA</h1>')
        # print(self.qte.toHtml())  # 会输出整个HTML网页完整模板代码
        self.qte.setText('<h1>AAAAA</h1>')  # 遇到富文本格式自动渲染

    # 追加文本和清空文本
    def add_clear(self):
        self.qte.append('<h1>AAAAA</h1>')  # 会追加到原文本的结尾，并自动识别文本类型
        self.qte.clear()  # 配合信号来测试


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())
