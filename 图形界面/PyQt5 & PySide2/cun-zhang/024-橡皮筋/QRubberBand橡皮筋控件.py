from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QRubberBand橡皮筋控件 - PyQt5中文网")
        self.resize(600, 500)
        self.func_list()

    def func_list(self):
        self.func()

    def func(self):
        # Line = 0  线形
        # Rectangle = 1 矩形
        # rb = QRubberBand(QRubberBand.Rectangle,self)
        # rb.setGeometry(QRect(30,30,30,30))  # 区域选择
        # rb.show()
        for i in range(0, 120):
            ck = QCheckBox(self)
            ck.setText(str(i))
            ck.move(i % 10 * 60, i // 10 * 40)

        self.rb = QRubberBand(QRubberBand.Rectangle, self)

    def mousePressEvent(self, QMouseEvent):
        # 创建一个橡皮筋控件
        # self.rb = QRubberBand(QRubberBand.Rectangle, self)  # 这行放到上面，避免同时出现多个选择区域，否则每次按下都会创建一个控件
        # 设置尺寸
        self.old_point = QMouseEvent.pos()
        self.rb.setGeometry(QRect(self.old_point, QSize()))
        # 展示控件
        self.rb.show()

    def mouseMoveEvent(self, QMouseEvent):
        # 计算出选择的区域尺寸
        self.rb.setGeometry(QRect(self.old_point, QMouseEvent.pos()).normalized())  # normalized()用来解决反向拖拽选择

    def mouseReleaseEvent(self, QMouseEvent):
        # 获取橡皮筋控件选择范围
        wh = self.rb.geometry()
        # 遍历控件
        for child in self.children():
            if wh.contains(child.geometry()) and child.inherits('QCheckBox'):
                child.toggle()
        self.rb.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())
