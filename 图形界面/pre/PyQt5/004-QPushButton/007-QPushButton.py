from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("title")
window.resize(500, 500)
window.show()

"""
QPushButton：
    用来给用户点击，来完成某种动作，一般是矩形
    继承于 QAbstractButton

创建：
    QPushButton()
    QPushButton(parent)
    QPushButton(text, parent)
    QPushButton(icon, text, parent)

菜单：
    setMenu(QMenu)：设置菜单
    menu()：获取菜单
    showMenu()：展示菜单
    QMenu()：
        addMenu(QMenu)：添加子菜单
        addSeparator()：添加分隔线
        addAction(QAction)：添加行为动作
        setTitle(str)：设置标题
        setIcon(QIcon)：设置图标
        
        QAction设置：
            setText(str)：设置内容
            setIcon(QIcon)：设置图标
            信号：triggered
边框是否保持扁平：
    setFlat(bool)：默认为False，设置为True时，除非按下按钮，否则大多数样式都不会绘制按钮背景
    isFlat()：获取当前按钮边框是否扁平
默认处理：
    setAutoDefault(bool)：
        设置为自动默认按钮
        在某些GUI样式中，默认按钮被绘制，其周围有一个额外的框架，三个像素或者更多
        Qt会自动在自动默认按钮周围保留此空间，即自动默认按钮可能会有稍大的提示
        对于具有QDialog父级的按钮，此属性的默认值为True，否则默认值为False
    autoDefault()
    setDefault(bool)
    isDefault()

信号基本继承了 QAbstractButton 和 002-QWidget

自定义上下文菜单请求信号：customContextMenuRequested(QPoint)
    setContextMenuPolicy(Qt.CustomContextMenu)
    Qt.DefaultContextMenu：调用对象方法contextMenuEvent()
    Qt.CustomContextMenu：发射信号
"""


sys.exit(app.exec_())

