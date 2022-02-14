from PyQt5.Qt import *
import sys


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle('第一个主窗口应用')
        self.resize(400, 400)
        self.status = self.statusBar()
        self.status.showMessage('只存在5秒的消息', 5000)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    # app.setWindowIcon(QIcon('...ico'))
    sys.exit(app.exec_())
