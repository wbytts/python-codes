from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("title")
window.resize(1000, 500)
window.show()
"""
QAbstractButton：
    所有按钮控件的基类
    提供按钮的通用功能

继承 002-QWidget

QAbstractButton:
    QPushButton:
        QCommandLinkButton:
    QRadioButton:
    QCheckButton:
    QToolButton:
    
QAbstractButton 功能作用：
    提示文本：
        setText(str)：设置按钮提示文本
        text()：获取按钮提示文本
    图标相关：
        setIcon(QIcon(...))：设置图标
        setIconSize(QSize(w,h))：设置图标大小
        icon()：获取图标
        iconSize()：获取图标大小
    设置快捷键：
        方式1：有提示文本的，如果提示文本包含&符号，则QAbstractButton会自动创建快捷键，&x 的快捷键就是 Alt + x
        方式2：setShortcut('...')
    自动重复：
        setAutoRepeat(bool)：设置自动重复
        setAutoRepeatInterval(毫秒)：设置自动重复检测间隔
        setAutoRepeatDelay(毫秒)：设置初次检测延迟
        autoRepeat()：获取是否自动重复
        autoRepeatInterval()：获取自动重复检测间隔
        autoRepeatDelay()：获取初次检测延迟
    状态：
        isDown()：是否按下按钮
        setDown()：设置按钮是否被按下
        isChecked()：是否选中了按钮
        isCheckable()：按钮是否可以被选中
        setCheckable()：设置按钮是否可以被选中
        setChecked()：设置按钮是否选中
        toggle()：在选中与没选中之间切换
        继承Widget的状态：isEnabled()、setEnabled(bool)
    排他性：
        概念：如果同时存在多个按钮，而此时所有的按钮又设置了排他性，则在同一时刻只能选中一个按钮
        autoExclusize()：是否自动排他，默认是False，单选是True
        setAutoExclusize(bool)：设置自动排他
    点击：
        click()：普通点击
        animateClick(ms)：动画点击
    设置有效区域：
        重写 hitButton(QPoint)：有效返回True，无效返回False
    信号：
        pressed()：鼠标按下信号
        released()：鼠标释放信号
        clicked(checked=False)：控件内按下 + 控件内释放
        toggled(bool checked)：切换信号（一般在单选框或者复选框中使用）
"""


class Btn(QAbstractButton):
    def paintEvent(self, QPaintEvent):
        # print('重写QAbstractButton方法，绘制按钮')
        # 绘制按钮上要展示的界面内容
        # 创建一个画家
        painter = QPainter(self)
        # 创建一个笔
        pen = QPen(QColor(110, 100, 10), 6)
        # 给画家一个笔
        painter.setPen(pen)
        # 画画
        painter.drawText(20, 20, self.text())
        painter.drawEllipse(0, 0, 100, 100)


btn = Btn(window)
btn.setText('lalala')
btn.resize(100, 100)
btn.show()
btn.pressed.connect(lambda: print('按钮被点击了'))

sys.exit(app.exec_())
