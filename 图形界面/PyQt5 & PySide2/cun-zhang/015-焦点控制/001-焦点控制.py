from PyQt5.Qt import *
import sys

'''
setFocus()
clearFocus()
setFocusPolicy()
'''
app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('焦点控制 - PyQt5中文网')
window.resize(600, 450)
window.move(300, 300)

led1 = QLineEdit(window)
led1.move(220, 50)
led2 = QLineEdit(window)
led2.move(220, 100)
led3 = QLineEdit(window)
led3.move(220, 150)

# led2.setFocus()
# led2.clearFocus()

# TabFocus  只能使用Tab键才能获取焦点
# ClickFocus  只能使用鼠标点击才能获取焦点
# StrongFocus 上面两种都行
# NoFocus  上面两种都不行
led2.setFocusPolicy(Qt.NoFocus)

window.show()
sys.exit(app.exec_())
