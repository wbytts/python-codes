from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('QAbstractButton')
window.resize(600, 450)
window.move(300, 300)


class Btn2(QPushButton):
    def hitButton(self, poi):
        print(poi)
        if poi.x() > self.width() / 2:
            return True
        return False


btn6 = Btn2(window)
btn6.setText('有效区域')
btn6.move(0, 300)
btn6.setChecked(True)
btn6.pressed.connect(lambda: print('========='))
btn6.released.connect(lambda: print('========='))
btn6.clicked.connect(lambda val: print('=========', val))
btn6.toggled.connect(lambda val: print('=========', val))

window.show()
sys.exit(app.exec_())
