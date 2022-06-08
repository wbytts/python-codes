from PyQt5.Qt import *
import sys

'''
setMenu(QMenu)   设置菜单
menu()    获取菜单
showMenu()   展示菜单
QMenu()继承自QWidget
addMenu(QMenu)   添加子菜单
addSeparator()   添加分割线
addAction(QAction)  添加行为动作
QMenu控件设置：setTitle()  setIcon(QIcon)
QAction设置：setText()  setIcon(QIcon)  信号：triggered
'''
app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('QPushButton')
window.resize(600, 450)
window.move(300, 300)

# ==============QPushbutton的构造函数=============== # 代码分割线 - 开始
# btn1 = QPushButton()
# btn2 = QPushButton(window)
# btn3 = QPushButton('按钮',window)
btn4 = QPushButton(QIcon('123.jpg'), '按钮', window)
# ==============QPushbutton的构造函数=============== # 代码分割线 - 结束

# ==============控件菜单设置=============== # 代码分割线 - 开始
# 流程参考test.py
# 创建菜单对象
menu = QMenu()
sun_menu = QMenu(menu)  # 放在父菜单中
sun_menu.setTitle('子菜单标题')
# 构造一个菜单
menuAction1 = QAction(QIcon('123.jpg'), '菜单1', window)
menuAction1.triggered.connect(lambda: print('WWWWWW'))

menuAction2 = QAction(QIcon('123.jpg'), '菜单2', window)
menuAction2.triggered.connect(lambda: print('SSSSSSSS'))

menuAction3 = QAction('菜单3', window)
menuAction3.triggered.connect(lambda: print('AAAAA'))
# 构造一个子菜单
sun_menuAction = QAction(QIcon('123.jpg'), '子菜单1', window)
# 添加菜单列表
menu.addAction(menuAction1)
menu.addAction(menuAction2)
menu.addSeparator()  # 添加分割线
menu.addMenu(sun_menu)  # 先在主菜单栏中添加一个子菜单
sun_menu.addAction(sun_menuAction)  # 然后为上面的子菜单添加子菜单
menu.addAction(menuAction3)

btn4.setMenu(menu)
# btn4.showMenu()  # 继承与QWidget所以可以单独展示
# ==============控件菜单设置=============== # 代码分割线 - 结束

window.show()
btn4.showMenu()
sys.exit(app.exec_())
