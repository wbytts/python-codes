from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QFontDialog字体选择对话框 - PyQt5中文网")
        self.resize(600, 500)
        self.func_list()

    def func_list(self):
        self.func()

    def func(self):
        # 1.构造方法
        # 设置默认字体
        font = QFont()
        font.setFamily('站酷酷黑')
        font.setPointSize(22)
        # qd = QFontDialog(font, self)

        # 设置当前字体 == 设置默认字体
        qd = QFontDialog(self)
        qd.setCurrentFont(font)  # 在没有点击OK之前，当前字体可以是默认字体，也可以是选择的字体。点击之后就变为最终选择字体

        btn = QPushButton(self)
        btn.move(100, 100)
        btn.setText('选择字体')
        btn.clicked.connect(lambda: qd.open())

        # 最终选择字体
        def font_sel():
            print(qd.selectedFont().family())
            pass

        btn.clicked.connect(lambda: qd.open(font_sel))

        '''
        # 选项控制
        # qd.setOption()  # 设置单个选项
        # qd.setOptions()  # 设置多个选项
        # qd.testOption()  # 测试选项是否生效
        # qd.options()  # 获得当前选项
        # 枚举值
        # QFontDialog.NoButtons  # 不现实OK和取消按钮
        # QFontDialog.DontUseNativeDialog  # 在Mac上使用Qt的标准字体对话框
        # QFontDialog.ScalableFonts  # 显示可缩放字体
        # QFontDialog.NonScalableFonts  # 显示不可缩放字体
        # QFontDialog.MonospacedFonts  # 显示等宽字体
        # QFontDialog.ProportionalFonts  # 显示比例字体

        # label = QLabel(self)
        # label.move(150, 150)
        # label.setText('PyQt5中文网')
        #
        # def font_con(font):
        #     label.setFont(font)
        #     label.adjustSize()
        # qd.currentFontChanged.connect(font_con)
        #
        # qd.show()


        # 静态方法
        label2 = QLabel(self)
        label2.move(150, 150)
        label2.setText('PyQt5中文网')

        def font_con2():
            # res = QFontDialog.getFont(self)  # 返回一个对象和一个布尔结果元祖
            res = QFontDialog.getFont(font, self, '对话框标题')  # 返回一个对象和一个布尔结果元祖
            if res[1]:
                label2.setFont(res[0])
                label2.adjustSize()
        btn.clicked.connect(font_con2)

        # 可用信号
        # qd.currentFontChanged()  # 字体发生改变
        # qd.fontSelected()  # 最终选择的字体
        '''


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())
