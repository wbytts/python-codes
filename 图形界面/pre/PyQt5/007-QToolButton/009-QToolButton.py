from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("title")
window.resize(500, 500)
window.show()
"""
QToolButton：
    提供了一个快速访问按钮
    通常是在工具栏内部使用
    工具按钮通常不显示文本标签，而是显示图片
    
创建：
继承的设置文本和工具提示：
按钮样式风格：
设置箭头：
自动提升：
菜单：
菜单弹出模式：
"""

bt = QToolButton(window)
bt.setText('ToolButton')
bt.show()

sys.exit(app.exec_())
