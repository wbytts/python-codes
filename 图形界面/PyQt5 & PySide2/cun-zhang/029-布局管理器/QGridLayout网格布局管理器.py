from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("布局管理器-网格布局QGridLayout - PyQt5中文网")
        self.resize(600, 500)
        self.func_list()

    def func_list(self):
        self.func()

    def func(self):
        gl = QGridLayout()
        self.setLayout(gl)
        label1 = QLabel('标签1', self)
        label1.setStyleSheet('background-color:green')
        label2 = QLabel('标签2', self)
        label2.setStyleSheet('background-color:red')
        label3 = QLabel('标签3', self)
        label3.setStyleSheet('background-color:green')
        # 元素操作 - 添加控件
        # gl.addWidget(label1)
        # gl.addWidget(label2)
        # gl.addWidget(label3)

        # 按单元格添加
        # gl.addWidget(label1, 0, 0)
        # gl.addWidget(label2, 0, 1)  # 第0行，第1列
        # gl.addWidget(label3, 1, 0)

        # 合并单元格
        gl.addWidget(label1, 0, 0)
        gl.addWidget(label2, 0, 1)
        gl.addWidget(label3, 1, 0, 1, 2)  # 第1行，第0列，跨1行，跨2列

        # 元素操作 - 添加布局
        label4 = QLabel('标签4', self)
        label4.setStyleSheet('background-color:green')
        label5 = QLabel('标签5', self)
        label5.setStyleSheet('background-color:red')
        label6 = QLabel('标签6', self)
        label6.setStyleSheet('background-color:green')
        layout = QBoxLayout(QBoxLayout.TopToBottom)
        layout.addWidget(label4)
        layout.addWidget(label5)
        layout.addWidget(label6)

        gl.addLayout(layout, 2, 0, 2, 3)

        # 获取位置和条目
        print(gl.getItemPosition(2))  # 获取第三个控件或布局的位置信息
        print(gl.itemAtPosition(0, 1).widget().text())  # 获取第一行，第二列控件名称信息

        # 尺寸设置 - 行高和列宽最小尺寸设置
        # gl.setColumnMinimumWidth(1, 100)  # 设置第2列最小宽度是100
        # gl.setRowMinimumHeight(1, 100)  # 设置第2行最小高度是100

        # 尺寸设置 - 拉伸系数设置
        # gl.setColumnStretch(1, 2)
        # gl.setColumnStretch(0, 1)
        # gl.setRowStretch(1, 2)
        # gl.setRowStretch(0, 1)

        # 间距控制
        # gl.setVerticalSpacing(20)
        # gl.setHorizontalSpacing(20)
        gl.setSpacing(30)  # 行间距和列间距都是30

        # 布局元坐标设置
        # Qt.TopLeftCorner
        # Qt.TopRightCorner
        # Qt.BottomLeftCorner
        # Qt.BottomRightCorner
        # gl.setOriginCorner(Qt.TopRightCorner)

        # 信息获取
        print(gl.rowCount())
        print(gl.columnCount())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()

    gl = window.layout()
    print(gl.cellRect(0, 1))  # 父控件显示完全后才能获取矩形区域的值

    window.show()
    sys.exit(app.exec_())
