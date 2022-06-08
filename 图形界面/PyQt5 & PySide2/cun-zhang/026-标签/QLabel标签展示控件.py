from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("展示控件-QLabel标签控件 - PyQt5中文网")
        self.resize(600, 500)
        self.func_list()

    def func_list(self):
        self.func()

    def func(self):
        # 构造函数
        label = QLabel('PyQt5中文网', self)
        label.resize(200, 50)
        label.move(100, 100)
        label.setStyleSheet('background-color:green')

        # 对齐方式
        # label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

        # 缩进和边距
        # label.setIndent(30)  # 文本缩进
        # label.setMargin(60)  # 内容区域和边框四周保留60个像素缩进

        # 文本格式
        # label1 = QLabel('<h1>PyQt5中文网</h1>', self)
        # label1.setTextFormat(Qt.PlainText)  # 字符串被解释为纯文本
        # label1.setTextFormat(Qt.RichText)  # 字符串被解释为富文本
        # label1.setTextFormat(Qt.AutoText)  # 自动识别文本和富文本

        # 小伙伴关联快捷键绑定
        # label = QLabel('PyQt5中文网(&A)', self)
        # led1 = QLineEdit(self)
        # led1.move(150, 250)
        # led2 = QLineEdit(self)
        # led2.move(150, 300)
        # label.setBuddy(led1)   # 绑定后label中的&自动消失，按住Alt+A自动切换焦点

        # 文本交互标志
        # label.setTextInteractionFlags(Qt.NoTextInteraction)  # 不能与文本交互
        # label.setTextInteractionFlags(Qt.TextSelectableByKeyboard)  # 使用键盘选中文本
        # label.setTextInteractionFlags(Qt.TextSelectableByMouse)  # 使用鼠标选中文本
        # label.setTextInteractionFlags(Qt.TextSelectableByMouse | Qt.TextSelectableByKeyboard | Qt.TextEditable)
        # label.setText("<a href='http://www.pyqt5.cn'>pyqt5中文网</a>")
        # label.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard)  # 使用键盘凸显和激活链接可以,使用Tab键突出显示连接，并使Enter激活它
        # label.setTextInteractionFlags(Qt.LinksAccessibleByMouse)  # 使用鼠标凸显和激活链接
        # label.setTextInteractionFlags(Qt.TextEditable)  # 文字可编辑
        # label.setTextInteractionFlags(Qt.TextEditorInteraction)  # 文本编辑器
        # label.setTextInteractionFlags(Qt.TextBrowserInteraction)  # 默认值

        # 选中文本
        # label.setSelection(1, 5)   # 被选中区间
        # label.hasSelectedText()  # 有没有被选中
        # label.selectedText()  # 选中内容
        # label.selectionStart()  # 选中开始字符

        # 链接交互
        label.setText("<a href='http://www.pyqt5.cn'>pyqt5中文网</a>")
        label.setOpenExternalLinks(True)

        # 单词换行
        # label.setText("pyqt5中文网\n pyq t5中文网pyqt5中文网pyqt5 中文网pyqt5中文网pyq t5中文网pyqt5中文网py qt5中文网pyqt5中 文网")
        # label.adjustSize()
        # label.setWordWrap(True)

        # 图片缩放
        # label.setPixmap(QPixmap('123.jpg'))
        # label.adjustSize()  # 根据图片大小缩放
        # label.setScaledContents(True)  # 根据label控件尺寸大小缩放

        # 内容操作
        # label.setText('')  # 文本操作
        # label.setNum(123)  # 数值操作
        # label.setPixmap()  # 直接插入图片
        # setPixmap延伸
        # pic = QPicture()  # 绘制指令
        # paint = QPainter(pic)  # 创建画家对象
        # paint.setPen(QPen(QColor(50, 200, 1)))  # 设置画笔
        # paint.drawEllipse(0, 0, 150, 150)  # 画一个椭圆
        # label.setPicture(pic)  # 图片处理 - 绘制的时候使用

        # label.setMovie(QMovie('123.gif').start())  # 动图处理    stop() 只能用于没有声音的简单动画，不是视频
        # label.setSpeed(200)  # 100为一倍速度
        # label.clear()  # 所有内容清空

        # 可用信号
        # label.linkActivated()  # 超链接被激活时，如果不能打开网址传递出网址，如果能打开不传递信号
        # label.linkHovered()  # 鼠标移动到超链接上时，传递出网址
        label.setText("<a href='https://www.pyqt5.cn'>pyqt5中文网</a>")
        label.linkHovered.connect(lambda a: print(a))

        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())
