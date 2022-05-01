from PyQt5.Qt import *
import sys

'''
1.设计一个无边框，透明度为80%的窗口，能自由拖动
2.设计三个控件，最大化，最小化和关闭
'''


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowOpacity(0.9)  # 半透明，必须是浮点型
        self.setWindowTitle('窗口案例')
        self.resize(600, 450)
        self.mouse_press = False
        # self.move(300, 300)
        self.btn_w = 50
        self.btn_x = 20
        self.func_list()

    def func_list(self):
        self.btn()

    def btn(self):
        # 添加最大化、最小化和关闭按钮
        self.close_btn = QPushButton(self)
        self.close_btn.setText('关闭')
        self.close_btn.resize(self.btn_w, self.btn_x)

        self.max_btn = QPushButton(self)
        # max_btn.setText('最大化')
        self.max_btn.resize(self.btn_w, self.btn_x)

        self.min_btn = QPushButton(self)
        self.min_btn.setText('最小化')
        self.min_btn.resize(self.btn_w, self.btn_x)

        self.close_btn.pressed.connect(self.close)

        def max_signal():
            if self.isMaximized():
                self.showNormal()
                self.max_btn.setText('最大化')
            else:
                self.showMaximized()
                self.max_btn.setText('恢复')

        self.max_btn.pressed.connect(max_signal)

        self.min_btn.pressed.connect(self.showMinimized)

    def resizeEvent(self, QResizeEvent):
        self.close_btn.move(self.width() - 50, 2)
        self.max_btn.move(self.width() - 100, 2)
        self.min_btn.move(self.width() - 150, 2)

    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            self.mouse_press = True  # 需要在属性中先定义为False
            self.win_x = self.x()
            self.win_y = self.y()
            self.m_x = QMouseEvent.globalX()
            self.m_y = QMouseEvent.globalY()
            # 1.创建一个标记，用来判定鼠标只有在按下之后才能移动
            # 2.窗口的原始坐标
            # 3.鼠标按下的坐标

    def mouseMoveEvent(self, QMouseEvent):
        if self.mouse_press:
            move_x = QMouseEvent.globalX()
            move_y = QMouseEvent.globalY()
            xx = move_x - self.m_x
            yy = move_y - self.m_y
            self.move(self.win_x + xx, self.win_y + yy)
        # if 窗口标记 == True：
        # 2.根据鼠标按下的点计算移动量
        # 3.根据移动量和窗口的原始坐标得到新坐标
        # 4.移动窗口位置

    def mouseReleaseEvent(self, QMouseEvent):
        self.mouse_press = False
        # 1.把mousePressEvent中创建的标记重置为False


app = QApplication(sys.argv)
window = Window()

window.show()
sys.exit(app.exec_())

# 创建一个无边框窗口，透明度设置为80%
# 自定义最大化、最小化和关闭按钮
# 支持拖拽功能
