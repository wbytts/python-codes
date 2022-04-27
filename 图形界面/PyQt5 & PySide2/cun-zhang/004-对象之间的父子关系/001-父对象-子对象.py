from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("父子关系-父对象")
window.resize(600, 400)
window.move(0, 0)


obj1 = QObject()
obj2 = QObject()
obj3 = QObject()

print(obj1, obj2, obj3)

# 通过 setParent 给一个对象设置父对象
obj2.setParent(obj1)
obj3.setParent(obj2)

# 获取直接子对象
print('obj1-children', obj1.children())
print('obj2-children', obj2.children())

print('obj1-findChild', obj1.findChild(QObject))
print('obj1-findChildren', obj1.findChildren(QObject))

window.show()
sys.exit(app.exec_())
