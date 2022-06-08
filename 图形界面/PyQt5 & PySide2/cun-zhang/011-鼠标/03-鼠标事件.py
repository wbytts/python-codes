from PyQt5.Qt import *
import sys


class MyWin(QWidget):
    # QMouseEvent
    def mouseMoveEvent(self, e: QMouseEvent):
        print('WWWWW', e.globalPos())  # 参考QMouseEvent文档，重点是全局和局部位置
        return super().mouseMoveEvent(e)

    def mousePressEvent(self, e: QShowEvent):
        print('鼠标按下')

    def mouseReleaseEvent(self, e: QShowEvent):
        print('鼠标松开')

    def mouseDoubleClickEvent(self, e: QShowEvent):
        print('鼠标双击')

    def enterEvent(self, e: QEvent):
        print('鼠标进入事件')
        self.setStyleSheet("background-color:red;")

    def leaveEvent(self, e: QEvent):
        print('鼠标离开事件')
        self.setStyleSheet("background-color:green;")

    def mouseMoveEvent(self, event):
        print("鼠标跟踪")


app = QApplication(sys.argv)

window = MyWin()
window.setWindowTitle('鼠标跟踪')
window.resize(600, 450)
window.move(300, 300)

window.setMouseTracking(True)

btn = QPushButton(window)
btn.move(60, 60)
btn.resize(50, 35)
btn.setText('按钮控件')
btn.setStyleSheet('background-color:green')

window.show()

sys.exit(app.exec_())
