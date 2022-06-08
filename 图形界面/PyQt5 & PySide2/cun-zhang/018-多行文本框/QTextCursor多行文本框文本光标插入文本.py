from PyQt5.Qt import *
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTextEdit - PyQt5中文网")
        self.resize(600, 500)
        self.func_list()

    def func_list(self):
        self.func()
        # self.place_hold()
        self.text_cur()

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

    # ==============内容设置=============== # 代码分割线 - 开始

    # 文本光标完成内容和格式设置
    def text_cur(self):
        # 1.首先创建一个光标对象；2.通过光标插入文本，传入上面的格式对象；# 3.插入文本内容格式
        # self.qte.document()  # 获取文本文档的方法，返回QTextDocument
        # self.qte.textCursor()  # cursor是直接操作鼠标的方法，textCursor是操作光标的

        # 插入文本
        # 1.首先创建一个光标对象
        qtc = self.qte.textCursor()
        # 3.插入文本内容格式
        tcf = QTextCharFormat()  # 创建一个格式对象
        tcf.setToolTip('pyqt5中文网')  # 设置提示文本
        tcf.setFontFamily('楷书')  # 设置字体
        tcf.setFontPointSize(25)  # 设置字体大小
        # 2.通过光标插入文本，传入上面的格式对象
        qtc.insertText('www.PyQt5.cn' , tcf)
        qtc.insertHtml("<a href='https://www.pyqt5.cn'>PyQt5中文网</a>")

        # 插入图片
        # 1.首先创建一个光标对象
        qtc = self.qte.textCursor()
        # 3.插入图片内容格式
        tcf = QTextImageFormat()
        tcf.setName('123.jpg')
        tcf.setWidth(40)
        tcf.setHeight(40)
        # 2.通过光标插入文本，传入上面的格式对象
        qtc.insertImage(tcf)

        # 插入文件
        # 1.首先创建一个光标对象
        qtc = self.qte.textCursor()
        # 3.插入文件内容格式
        tcf = QTextDocumentFragment().fromHtml("<a href='https://www.pyqt5.cn'>PyQt5中文网</a>")  # 插入富文本
        # tcf.fromHtml("<a href='https://www.pyqt5.cn'>PyQt5中文网</a>") # fromHtml有返回值，所以必须给个变量名，这样写就错了
        # tcf = QTextDocumentFragment().fromPlainText("<a href='https://www.pyqt5.cn'>PyQt5中文网</a>") # 插入普通文本
        # 2.通过光标插入文本，传入上面的格式对象
        qtc.insertFragment(tcf)

        # 插入列表1
        # 1.首先创建一个光标对象
        qtc = self.qte.textCursor()
        # 3.插入文本内容格式
        # tcf = QTextList()
        # tcf.count()
        # 2.通过光标插入文本，传入上面的格式对象
        tcf = qtc.insertList(QTextListFormat.ListDecimal)  # 返回一个QTextList对象
        # qtc.createList(QTextListFormat.ListDecimal)
        print(tcf.item(3))

        # 插入列表2
        # 1.首先创建一个光标对象
        qtc = self.qte.textCursor()
        # 3.插入文本内容格式
        tcf = QTextListFormat()
        tcf.setNumberPrefix('$')  # 列表前缀，必须要加上setStyle，设置为数字
        tcf.setIndent(2)  # 缩进一个Tab
        tcf.setStyle(QTextListFormat.ListDecimal)
        # 2.通过光标插入文本，传入上面的格式对象
        qtc.insertList(tcf)

        # 插入表格
        # 1.首先创建一个光标对象
        qtc = self.qte.textCursor()
        # 3.插入表格格式
        tcf = QTextTableFormat()
        tcf.setAlignment(Qt.AlignRight)
        tcf.setHeight(30)
        tcf.setWidth(150)
        tcf.setCellPadding(1.1)
        tcf.setCellSpacing(0.1)
        tcf.setColumnWidthConstraints()
        # 2.通过光标插入文本，传入上面的格式对象
        # qtc.insertTable(2, 3)
        # qtc.insertTable(2, 3, tcf)  # 返回QTextTable,还可以追加后续操作，如下
        ttt = qtc.insertTable(2, 3, tcf)
        ttt.appendColumns(3)  # 追加3列


        # 插入文本快
        qtc = self.qte.textCursor()
        tcf = QTextBlockFormat()
        tcf.setAlignment(Qt.AlignRight)
        tcf.setRightMargin(50)

        tcf2 = QTextCharFormat()
        tcf2.setFontFamily('隶书')
        tcf2.setFontWeight(50)

        qtc.insertBlock(tcf,tcf2)
        self.qte.setFocus()

        # 插入框架
        qtc = self.qte.textCursor()
        tcf = QTextFrameFormat()
        tcf.setBorder(3)
        tcf.setRightMargin(20)
        qtc.insertFrame(tcf)


# ==============内容设置=============== # 代码分割线 - 结束

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())
