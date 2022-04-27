from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("TITLE")
window.resize(600, 400)
window.move(0, 0)


window.show()
sys.exit(app.exec_())
