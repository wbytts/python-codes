from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('掩码设置')
window.resize(600, 450)
window.move(300, 300)

led = QLineEdit(window)
led.setInputMask('>AAAA-99A9;$')

window.show()
sys.exit(app.exec_())
