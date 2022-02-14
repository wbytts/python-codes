import sys
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QProgressBar, QPushButton, QHBoxLayout, QVBoxLayout


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.progressbar = QProgressBar(self)                   # 1
        # self.progressbar.setOrientation(Qt.Vertical)
        self.progressbar.setMinimum(0)                          # 2
        self.progressbar.setMaximum(100)
        # self.progressbar.setRange(0, 100)

        self.step = 0                                           # 3

        self.timer = QTimer(self)                               # 4
        self.timer.timeout.connect(self.update_func)

        self.ss_button = QPushButton('Start', self)             # 5
        self.ss_button.clicked.connect(self.start_stop_func)
        self.reset_button = QPushButton('Reset', self)          # 6
        self.reset_button.clicked.connect(self.reset_func)

        self.h_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()

        self.h_layout.addWidget(self.ss_button)
        self.h_layout.addWidget(self.reset_button)
        self.v_layout.addWidget(self.progressbar)
        self.v_layout.addLayout(self.h_layout)

        self.setLayout(self.v_layout)

    def start_stop_func(self):
        if self.ss_button.text() == 'Start':
            self.ss_button.setText('Stop')
            self.timer.start(100)
        else:
            self.ss_button.setText('Start')
            self.timer.stop()

    def update_func(self):
        self.step += 1
        self.progressbar.setValue(self.step)

        if self.step >= 100:
            self.ss_button.setText('Start')
            self.timer.stop()
            self.step = 0

    def reset_func(self):
        self.progressbar.reset()
        self.ss_button.setText('Start')
        self.timer.stop()
        self.step = 0


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
