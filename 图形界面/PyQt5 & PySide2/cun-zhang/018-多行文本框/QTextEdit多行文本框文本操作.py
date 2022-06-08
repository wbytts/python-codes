from PyQt5.Qt import *
import sys


class Text_Url(QTextEdit):
    def mousePressEvent(self, QMouseEvent):
        print(QMouseEvent.pos())
        link = self.anchorAt(QMouseEvent.pos())
        if len(link) > 0:
            QDesktopServices.openUrl(QUrl(link))
        return super().mousePressEvent(QMouseEvent)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTextEdit-多行文本框直接操作文本 - PyQt5中文网")
        self.resize(600, 500)
        self.func_list()

    def func_list(self):
        self.func()

    def func(self):
        self.qte = Text_Url('QTextEdit-多行文本框' * 5, self)
        self.qte.move(100, 100)
        self.qte.resize(250, 250)
        self.qte.setStyleSheet('background-color:green')
        self.qte.setFrameStyle(QFrame.Box | QFrame.Raised)
        self.qte.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.qte.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.qte.insertHtml("多行文本框" * 20 + "<a href='http://www.bl186.net' name='pyqt5'>PyQt5中文网</a>")

        self.btn = QPushButton('按  钮', self)
        self.btn.move(120, 50)
        self.btn.resize(70, 30)
        self.btn.pressed.connect(self.text_cur)

    def text_cur(self):
        '''
        # 1.自动化格式（以*作为触发）
        # self.qte.setAutoFormatting(QTextEdit.AutoBulletList)

        # 2.换行模式设置
        # QTextEdit.NoWrap  # 不换行，超过宽度后会出现水平滚动条
        # QTextEdit.WidgetWidth  # 以控件宽度为标准，保持单词完整性
        # QTextEdit.FixedColumnWidth  # 填充列宽度
        # QTextEdit.FixedPixelWidth  # 直接设置一行宽度为多少像素
        self.qte.setLineWrapMode(QTextEdit.FixedPixelWidth)  # 设置软换行
        self.qte.setLineWrapColumnOrWidth(100)  # 配合FixedPixelWidth和FixedColumnWidth

        # QTextOption.NoWrap
        # QTextOption.WordWrap  # 保持单词完整性
        # QTextOption.ManualWrap
        # QTextOption.WrapAnywhere  # 在任意位置换行
        # QTextOption.WrapAtWordBoundaryOrAnywhere
        # self.qte.setWordWrapMode(QTextOption.WrapMode)  # 设置单词换行模式

        # 3.设置覆盖模式
        self.qte.setOverwriteMode(True)

        # 4.光标设置
        self.qte.setCursorWidth(10)

        # 5.段落对其方式设置
        # Qt.AlignLeft
        # Qt.AlignRight
        # Qt.AlignCenter
        self.qte.setAlignment(Qt.AlignRight)

        # 6.字体格式设置(字体样式、字体尺寸、字体效果、统一设置)
        # QFontDialog.getFont()
        # self.qte.setFontFamily('站酷快乐体2016修订版')
        # self.qte.setFontWeight(5)
        #
        # self.qte.setFontPointSize(30)
        #
        # self.qte.setFontUnderline(True)

        # font = QFont()
        # font.setFamily('站酷快乐体2016修订版')
        # font.setOverline(True)
        # self.qte.setFont(font)

        # 颜色设置(文字颜色和背景颜色)
        self.qte.setTextBackgroundColor(QColor(100, 50, 50))
        self.qte.setTextColor(QColor(200, 10, 100))

        # 设置字符格式
        tcf = QTextCharFormat()
        tcf.setFontFamily('站酷快乐体2016修订版')
        tcf.setFontPointSize(30)
        self.qte.setCurrentCharFormat(tcf)

        tcf2 = QTextCharFormat()
        tcf2.setFontUnderline(True)
        # self.qte.setCurrentCharFormat(tcf2)
        self.qte.mergeCurrentCharFormat(tcf2)

        # 常用编辑操作
        # copy()
        # paste()
        # canPaste()
        # setUndoRedoEnabled()
        # redo()
        # undo()
        # selectAll()
        # find()

        self.qte.copy()
        self.qte.paste()
        # QTextDocument.FindBackward  # 向前查找
        # QTextDocument.FindCaseSensitively  # 区分大小写操作
        # QTextDocument.FindWholeWords  # 匹配完整单词
        self.qte.find('文本', QTextDocument.FindBackward)

        # 只读设置
        self.qte.setReadOnly(True)

        # Tab控制
        self.qte.setTabChangesFocus(True)
        self.qte.setTabStopDistance(150)  # 点击按钮之后会自动变化
        '''
        # 打开超链接-重写点击事件

        # 可用信号
        # self.qte.textChanged()  # 文本内容改变时
        # self.qte.selectionChanged()  # 选中内容改变时
        # self.qte.cursorPositionChanged()  # 光标位置改变时
        # self.qte.currentCharFormatChanged()  # 当前字符发生改变时
        # self.qte.copyAvailable()  # 复制可用时
        # self.qte.redoAvailable()  # 重做可用时
        # self.qte.undoAvailable()  # 撤销可用时

        self.qte.textChanged.connect(self.text_change)
        self.qte.copyAvailable.connect(self.copy_yes)

    def text_change(self):
        print('文本内容改变时')

    def copy_yes(self, yes):
        print('复制可用', yes)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())
