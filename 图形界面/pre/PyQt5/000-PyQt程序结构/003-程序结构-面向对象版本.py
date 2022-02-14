from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle('title')
        self.resize(500, 500)
        self.show()
        self.setup_ui()

    def setup_ui(self):
        label = QLabel(self)
        label.setText('xxx')
        label.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
