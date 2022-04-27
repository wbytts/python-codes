from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('鼠标操作')
window.resize(600, 450)
window.move(300, 300)
# 1.鼠标形状操作
# window.setCursor(Qt.BusyCursor)

# 2.自定义鼠标形状
pixmap = QPixmap('123.jpg')
new_pixmap = pixmap.scaled(5, 5)  # 这个方法通过返回值传递下去，并不是直接改变对象，所以要给一个变量，
cursor = QCursor(new_pixmap, 1, 1)  # 0为图片中型位置，根据mew_pixmap中设置图片的大小来取值
window.setCursor(cursor)  # 从这一步反推上去

# 3.获取鼠标位置和设置鼠标位置
window.cursor().setPos(100, 100)

# 4.鼠标跟踪：下一个文件中

btn = QPushButton(window)
btn.move(60, 60)
btn.resize(50, 35)
btn.setText('按钮控件')
btn.setStyleSheet('background-color:green')

window.show()

btn.setCursor(Qt.DragLinkCursor)
window.setMouseTracking(True)

sys.exit(app.exec_())
