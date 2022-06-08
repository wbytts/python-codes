from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QFontComboBox字体选择下拉控件 - PyQt5中文网")
        self.resize(600, 500)
        self.func_list()

    def func_list(self):
        self.func()

    def func(self):
        label = QLabel(self)
        label.setText('PyQt5中文网')
        label.setStyleSheet('font-size:35px')
        label.resize(300, 50)
        label.move(150, 150)

        qfcb = QFontComboBox(self)

        # currentFontChanged  # 当前字体发生改变
        qfcb.currentFontChanged.connect(lambda font: label.setFont(font))

        # 过滤器
        QFontComboBox.FontFilters(QFontComboBox.AllFonts)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())
