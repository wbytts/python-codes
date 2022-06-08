from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('QToolButton-工具按钮 - PyQt5中文网')
window.resize(600, 450)
window.move(300, 300)

# btn = QPushButton(window)
btn = QToolButton(window)
btn.move(60, 60)
btn.resize(50, 35)
btn.setText('按钮控件')
btn.setIcon(QIcon('123.jpg'))  # 加上图片之后text自动被覆盖了
btn.setToolTip('XXXXXXX')  # 设置提示文本，QWidget中的方法

# ==============QToolButton图标和文本显示设置=============== # 代码分割线 - 开始
# Qt.ToolButtonIconOnly
# Qt.ToolButtonTextOnly
# Qt.ToolButtonTextBesideIcon
# Qt.ToolButtonTextUnderIcon
btn.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
# ==============QToolButton图标和文本显示设置=============== # 代码分割线 - 结束

# ==============QToolButton箭头设置=============== # 代码分割线 - 开始
# Qt.DownArrow
# Qt.NoArrow
# Qt.UpArrow
# Qt.LeftArrow
# Qt.RightArrow
btn.setArrowType(Qt.NoArrow)
# ==============QToolButton箭头设置=============== # 代码分割线 - 结束

# ==============QToolButton自动提升功能=============== # 代码分割线 - 开始
btn.setAutoRaise(True)
# QPushbutton中的setFlat(True)是不能用在这里的，他们不是父子关系
# ==============QToolButton自动提升功能=============== # 代码分割线 - 结束

# ==============QToolButton菜单的设置=============== # 代码分割线 - 开始
# 和QPushButton对比学习
menu = QMenu()
sun_menu = QMenu(menu)
menuAction1 = QAction(QIcon('123.jpg'), '菜单1', window)
menuAction1.triggered.connect(lambda: print('WWWWWW'))
menu.addAction(menuAction1)
btn.setMenu(menu)
btn.setPopupMode(QToolButton.DelayedPopup)
# MenuButtonPopup   点击箭头显示子菜单
# InstantPopup     单击按钮显示子菜单
# DelayedPopup     长按按钮显示子菜单
# ==============QToolButton菜单的设置=============== # 代码分割线 - 结束

# ==============QToolButton可用信号=============== # 代码分割线 - 开始
# 首先继承父类所有信号
btn2 = QToolButton(window)
btn2.setText('信号')
menus = QMenu(btn2)
menuAction1 = QAction(QIcon('123.jpg'), '菜单1', window)
menuAction1.setData(111)
menuAction2 = QAction(QIcon('123.jpg'), '菜单2', window)
menuAction2.setData(window)

menus.addAction(menuAction1)
menus.addAction(menuAction2)
btn2.setMenu(menus)
btn2.setPopupMode(QToolButton.InstantPopup)


def tool_action(action):
    print('JJJ', action.data())


btn2.triggered.connect(tool_action)
# ==============QToolButton可用信号=============== # 代码分割线 - 结束

window.show()
sys.exit(app.exec_())
