from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QPlainTextEdit-多行文字编辑框 - PyQt5中文网")
        self.resize(600, 500)
        self.func_list()

    def func_list(self):
        self.func()
        self.pte_edit()

    def func(self):
        self.pte = QPlainTextEdit(self)
        self.pte.move(150, 70)
        self.pte.resize(300, 300)

        self.line_num = QWidget(self)
        self.line_num.resize(20, 300)
        self.line_num.move(129, 70)
        self.line_num.setStyleSheet('background-color:green')

        self.line_label = QLabel(self.line_num)
        self.line_label.move(0, 5)
        line_nums = '\n'.join([str(i) for i in range(1, 101)])
        self.line_label.setText(line_nums)
        self.line_label.adjustSize()  # 根据内容自适应label控件的尺寸大小

    def pte_edit(self):
        '''
        # 占位设置
        # self.pte.setPlainText('请输入内容')
        self.pte.setPlaceholderText('请输入内容')
        # 只读设置
        # self.pte.setReadOnly(True)
        # 格式设置
        tcf = QTextCharFormat()
        tcf.setFontUnderline(True)
        tcf.setUnderlineColor(QColor(0,200,200))
        self.pte.setCurrentCharFormat(tcf)
        # 软换行模式,只有两种模式
        # QPlainTextEdit.WidgetWidth
        # QPlainTextEdit.NoWrap
        self.pte.setLineWrapMode(QPlainTextEdit.WidgetWidth)
        # 覆盖模式
        self.pte.setOverwriteMode(True) # 只能单个字符覆盖，不能覆盖中文字符
        # Tab键控制
        self.pte.setTabChangesFocus(True)
        self.pte.setTabStopDistance(20) # Tab键宽度
        # 文本操作，偏向于普通文本
        self.pte.setPlainText('python GUI编程网原创全套PyQt5视频教程，Qt Designer+PyUIC教程，pyqtgraph教程，以及pyqt5布局、控件、信号、槽、扩展应用和打包上线相关知识，此外还分享一些PyQt5常见问题和pyqt漂亮gui界面模板资源，从入门到精通一站式学习python可视化编程技术')
        self.pte.insertPlainText('python GUI编程网原创全套PyQt5视频教程，Qt Designer+PyUIC教程，pyqtgraph教程，以及pyqt5布局、控件、信号、槽、扩展应用和打包上线相关知识，此外还分享一些PyQt5常见问题和pyqt漂亮gui界面模板资源，从入门到精通一站式学习python可视化编程技术')
        self.pte.appendPlainText('www.pyqt5.cn')
        self.pte.appendHtml("<a href='http://www.bl186.net' name='pyqt5'>PyQt5中文网</a>")  # 部分html代码不支持
        print(self.pte.toPlainText())
        # 块操作
        self.pte.setMaximumBlockCount(4)  # 按照回车键划分的，查过4块，之前的就会被删除
        # 常见的编辑操作
        self.pte.copy()
        self.pte.zoomIn(5) # 正数为放大，负数为缩小
        self.pte.zoomOut(5) # 和上面正好相反，建议不使用
        # 滚动控制，主要控制内容滚动，保持光标可见
        self.pte.centerCursor()  # 光标所在行滚动到中间位置,两端不滚动
        self.pte.setCenterOnScroll(True) # 和上面一样，尾部会留空白，头部不留
        self.pte.ensureCursorVisible()  # 保证光标可见，移动距离最短优先
        # 光标控制
        self.pte.textCursor() # 获取光标QTextCursor
        self.pte.cursorForPosition(QPoint(100,100))
        self.pte.setCursorWidth(20) # 设置光标宽度
        '''
        # 可使用信号
        # textChanged()  # 文本改变时
        # selectionChanged()  # 选中内容改变时
        # modificationChanged()  # 编辑状态改变时
        # cursorPositionChanged()  # 光标位置改变时
        # blockCountChanged()  # 块的个数发生改变
        # updateRequest(rect,dy)  # 内容更新可用(传递两个参数，一个是跟新的区域，一个是y轴上的位移)
        # copyAvailable()  # 复制可用
        # redoAvailable()  # 重做可用
        # undoAvailable()  # 撤销可用
        # self.pte.textChanged.connect(lambda :print('WWWWWWWW'))
        # self.pte.selectionChanged.connect(lambda :print('WWWWWWWW'),self.pte.textCursor().selectedText())
        self.pte.updateRequest.connect(lambda rect, dy: self.line_label.move(self.line_label.x(), self.line_label.y() + dy))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())
