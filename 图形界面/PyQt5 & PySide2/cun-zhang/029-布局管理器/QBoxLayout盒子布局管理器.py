from PyQt5.Qt import *
import sys
from qt_material import apply_stylesheet

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("布局管理-盒子布局QBoxLayout - PyQt5中文网")
        self.resize(600, 500)
        self.func_list()

    def func_list(self):
        self.func()

    def func(self):
        # QBoxLayout有两个子类QVBoxLayout和QHBoxLayout
        label1 = QLabel('标签1', self)
        label1.setStyleSheet('background-color:green')
        label2 = QLabel('标签2', self)
        label2.setStyleSheet('background-color:red')
        label3 = QLabel('标签3', self)
        label3.setStyleSheet('background-color:green')
        # 1.创建布局管理器
        # QBoxLayout.RightToLeft
        # QBoxLayout.LeftToRight
        # QBoxLayout.TopToBottom
        # QBoxLayout.BottomToTop
        layout = QBoxLayout(QBoxLayout.RightToLeft)
        # layout = QHBoxLayout()
        # 2.添加控件
        layout.addWidget(label1, 1)  # 1为1/6
        layout.addWidget(label2, 3)  # 3为3/6
        layout.addWidget(label3, 2)  # 2为2/6
        # 3.添加布局管理器到父控件
        self.setLayout(layout)

        # 修改方向
        # layout.setDirection(QBoxLayout.TopToBottom)

        # 添加元素
        # label4 = QLabel('标签4', self)
        # label4.setStyleSheet('background-color:green')
        # layout.addWidget(label3)
        # layout.insertWidget(2, label4)  # 索引值为2的地方插入label4

        # 移除控件
        # layout.removeWidget(label3)  # 移除的控件只是从布局管理器中踢出，但是会在父控件正常展示，可以直接调用hide()方法

        # 添加空白
        # 直接在控件之间添加，就是在控件之间添加一个空白控件
        # layout.addWidget(label1)
        # layout.addSpacing(50)  # 可以自由调节某个元素之间的间距
        # layout.addWidget(label2)
        # layout.addWidget(label3)

        # 弹簧:当所有控件没有设定伸缩因子的时候就会使用默认值，如果其中一个控件伸缩因子改为1，代表这个控件占所有伸缩量的百分之百
        # layout.addWidget(label1, 1)  # 1为1/8
        # layout.addStretch(2)  # 增加2个宽度的伸缩因子
        # layout.addWidget(label2, 3)  # 3为3/8
        # # layout.insertStretch(2)
        # layout.addWidget(label3, 2)  # 2为2/8

        # 布局嵌套
        label4 = QLabel('标签4')
        label4.setStyleSheet('background-color:green')
        label5 = QLabel('标签5')
        label5.setStyleSheet('background-color:red')
        label6 = QLabel('标签6')
        label6.setStyleSheet('background-color:green')

        layout2 = QVBoxLayout()

        layout2.addWidget(label4)
        layout2.addWidget(label5)
        layout2.addWidget(label6)

        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addLayout(layout2)
        layout.addWidget(label3)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_teal.xml')

    window = Window()

    window.show()
    sys.exit(app.exec_())
