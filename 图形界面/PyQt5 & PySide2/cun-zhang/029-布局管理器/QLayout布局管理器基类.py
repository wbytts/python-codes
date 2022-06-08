from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("布局管理-初识QLayout - PyQt5中文网")
        self.resize(600, 500)
        self.func_list()

    def func_list(self):
        self.func()

    def func(self):
        # 初识布局管理器
        # QLayout是抽象类，直接使用子类创建布局管理器
        # 因为父控件直接和布局管理器产生联系，布局管理器再和子控件建立联系，所以这里子控件可以省略self
        label1 = QLabel('按钮1', self)
        label1.setStyleSheet('background-color:green')
        label2 = QLabel('按钮2', self)
        label2.setStyleSheet('background-color:red')
        label3 = QLabel('按钮3', self)
        label3.setStyleSheet('background-color:green')

        # label_width = self.width()
        # label_height = self.height() / 3
        # label1.resize(label_width, label_height)
        # label2.resize(label_width, label_height)
        # label3.resize(label_width, label_height)

        # label1.move(0, 0)
        # label2.move(0, label_height)
        # label3.move(0, label_height * 2)

        # 1.创建布局管理器对象
        # v_layout = QVBoxLayout()
        v_layout = QHBoxLayout()

        # 2.设置对象参数
        # 2.1边距调节
        v_layout.setContentsMargins(10, 30, 50, 70)  # 外边距 上左下右
        v_layout.setSpacing(30)  # 内边距
        # 2.2设置布局的方向
        # Qt.RightToLeft
        # Qt.LeftToRight
        # Qt.LayoutDirectionAuto  # 自动布局
        self.setLayoutDirection(Qt.RightToLeft)

        # 3.添加子控件
        v_layout.addWidget(label1)
        v_layout.addWidget(label2)
        v_layout.addWidget(label3)

        # 4.添加布局管理器到父控件
        self.setLayout(v_layout)  # setLayout直接继承QWidget，不是控件，只是一种定位策略
        print(self.children())  # 这时候布局管理器和子控件拥有相同的父对象self，所以布局管理器不是控件，只是一种定位策略
        # label2.hide()

        # 构造函数
        label1 = QLabel('标签1', self)
        label1.setStyleSheet('background-color:green')
        label2 = QLabel('标签2', self)
        label2.setStyleSheet('background-color:red')
        label3 = QLabel('标签3', self)
        label3.setStyleSheet('background-color:green')

        # QLayout  # 是一个抽象基类
        # QBoxLayout  # 是一个基类，属于盒子布局，内部必须声明布局方向

        # QBoxLayout.LeftToRight
        # QBoxLayout.RightToLeft
        # QBoxLayout.TopToBottom
        # QBoxLayout.BottomToTop
        layout = QBoxLayout(QBoxLayout.TopToBottom)

        self.setLayout(layout)
        layout.addWidget(label1)
        # layout.addWidget(label2)
        # layout.addWidget(label3)

        # layout.setSpacing(50)
        # QMargins
        # layout.contentsMargins().left()  # 获取左外边距

        # 控件替换
        # layout.replaceWidget(label2, label3)  # 被替换的控件会从布局管理器中移除，但是会在父控件中展示
        # label2.setParent(None)  # 释放label2

        # 布局嵌套
        label4 = QLabel('标签4', self)
        label4.setStyleSheet('background-color:green')
        label5 = QLabel('标签5', self)
        label5.setStyleSheet('background-color:red')
        label6 = QLabel('标签6', self)
        label6.setStyleSheet('background-color:green')

        layout2 = QBoxLayout(QBoxLayout.LeftToRight)
        layout2.addWidget(label4)
        layout2.addWidget(label5)
        layout2.addWidget(label6)
        layout.addLayout(layout2)
        layout.addWidget(label2)
        layout.addWidget(label3)

        # 能用性
        # layout.setEnabled(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())
