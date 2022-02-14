from PyQt5.Qt import *

import sys

# 在pyqt5中，有且只有一个，应用对象
app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("社会我王哥，人狠话不多")
window.resize(500, 500)
window.move(400, 200)
window.show()

label = QLabel(window)
label.setText("Hello World")
label.move(200, 200)
label.show()

sys.exit(app.exec_())
