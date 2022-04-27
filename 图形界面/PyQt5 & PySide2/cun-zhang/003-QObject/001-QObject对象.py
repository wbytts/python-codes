from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("QObject对象")
window.resize(600, 400)
window.move(0, 0)

obj = QObject()
# QObject，设置的 ObjectName是一个标识符
obj.setObjectName('第一个QObject对象')
print(obj)  # <PyQt5.QtCore.QObject object at 0x0000025C973A11B0>


window.show()
sys.exit(app.exec_())









