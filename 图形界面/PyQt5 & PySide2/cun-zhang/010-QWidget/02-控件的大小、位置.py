from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("TITLE")

# window.resize(600, 400)
# window.move(0, 0)

# w.setGeometry(x, y, w, h)
window.setGeometry(0, 0, 600, 400)

# 自适应尺寸
# w.adjustSize()

window.show()
sys.exit(app.exec_())
