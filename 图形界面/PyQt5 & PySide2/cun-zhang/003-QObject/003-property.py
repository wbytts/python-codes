from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("TITLE")
window.resize(600, 400)
window.move(0, 0)

obj = QObject()
obj.setProperty("key1", "value1")
obj.setProperty("key2", "value2")

print("属性 key1 =", obj.property("key1"))
print("属性 key2 =", obj.property("key2"))

print("所有设置的属性对象：", obj.dynamicPropertyNames())

window.show()
sys.exit(app.exec_())
