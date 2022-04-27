from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("TITLE")
window.resize(600, 400)
window.move(0, 0)

w1 = QObject()
w2 = QWidget()
w3 = QPushButton()
w4 = QLabel()

obj_list = [w1, w2, w3, w4]
for o in obj_list:
    print(o.isWidgetType())  # 判断对象是否属于控件类型

print('-' * 100)

for o in obj_list:
    print(o.inherits('QWidget'))  # 判断某个对象是否继承与另一个对象

window.show()
sys.exit(app.exec_())
