from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("鼠标操作")
        self.resize(600, 500)
        self.func_list()

    def func_list(self):
        self.func()

    def func(self):
        label = QLabel(self)
        label.resize(150, 150)
        label.move(50, 50)
        label.setText('标签学习')
        label.setStyleSheet('background-color:green')
        label.setCursor(Qt.DragLinkCursor)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()

    pixmap = QPixmap('aaa.png')
    new_pixmap = pixmap.scaled(150, 150)
    cursor = QCursor(new_pixmap, 120, 120)
    window.setCursor(cursor)

    window.show()
    sys.exit(app.exec_())
