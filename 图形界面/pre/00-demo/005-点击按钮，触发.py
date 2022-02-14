from PyQt5.Qt import *
import sys


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle('TITLE')
        self.resize(500, 500)

        self.button = QPushButton('退出程序')
        self.button.clicked.connect(self.on_button_clicked)

        self.layout = QHBoxLayout()
        self.layout.addWidget(self.button)

        main_frame = QWidget()
        main_frame.setLayout(self.layout)
        self.setCentralWidget(main_frame)

    def on_button_clicked(self):
        print('按钮被点击了')
        # 获取应用程序实例
        app = QApplication.instance()
        # 退出应用程序
        app.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
