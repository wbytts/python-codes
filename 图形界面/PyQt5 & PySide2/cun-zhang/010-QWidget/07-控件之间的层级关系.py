from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)
window = Window()

label1 = QLabel(window)
label1.setText('标签1')

label2 = QLabel(window)
label2.setText('标签2')
label2.move(50, 50)

label3 = QLabel(window)
label3.setText('标签3')
label3.setStyleSheet('background-color:green')
label3.move(100, 100)

print(label1)
print(label2)
print(label3)
print('========')
print(window.childAt(110, 110))
print('========')
print(window)
print(label3.parentWidget())

print(window.childrenRect())

window.show()
sys.exit(app.exec_())
