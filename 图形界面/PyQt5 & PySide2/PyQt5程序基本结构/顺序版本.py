import sys
from PyQt5.Qt import *

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("title")
window.resize(400, 600)
window.move(0, 0)

window.show()
sys.exit(app.exec())
