from PyQt5.Qt import *
import sys

'''
交互状态：
1.是否可用：setEnabled(bool)控件是否禁用  isEnable()
2.是否显示：setVisible(bool)    isVisible()  isVisibleTo()
3.是否隐藏: setHidden(bool)  show()隐藏  hide()展示  isHidden()
4.是否编辑: setWindowModified(bool)   isWindowModified()
5.是否为活跃窗口: isActiveWindow()
6.关闭: close()
信息提示： setStatusTip(str)
'''


class Window(QWidget):
    def paintEvent(self, e: QPaintEvent):
        print('窗口被绘制')
        return super().paintEvent(e)


class Btn(QPushButton):
    def paintEvent(self, e: QPaintEvent):
        print('按钮被绘制')
        return super().paintEvent(e)


app = QApplication(sys.argv)

window = Window()
window.setWindowTitle('控件交互 - PyQt5中文网[*]')
window.resize(600, 450)
window.move(300, 300)

btn = QPushButton(window)
btn.move(60, 60)
btn.resize(50, 35)
btn.setText('按钮控件')
# btn.setStyleSheet('background-color:green')

btn1 = Btn(window)
btn1.move(100, 100)
btn1.resize(50, 35)
btn1.setText('按钮控件')
# 是否可用
btn1.setEnabled(False)
# 是否绘制显示
# window.show()
# window.setVisible(True)
# window.setHidden(True)

btn1.setVisible(True)
btn1.setHidden(True)

window.setWindowModified(True)  # 现在标题后面设一个 [*] 放在标题任何位置都可以，但是一定要放 *

# print(window.isActiveWindow())

# 窗口关闭，不会会释放对象
# btn1.setVisible(False)
# btn1.setHidden(True)
# btn1.hide()

# 想要释放对象必须组合setAttribute一起使用，可以使用destroyed信号来检测
btn1.destroyed.connect(lambda: print('按钮被释放'))
btn1.setAttribute(Qt.WA_DeleteOnClose, True)
btn1.close()

window1 = QMainWindow()  # 懒加载窗口控件，只用用到的时候才会加载状态栏
window1.statusBar()  # 触发懒加载
window1.setStatusTip('这是一个懒加载窗口')

btn2 = QPushButton(window1)
btn2.setText('按钮2')
btn2.setStatusTip('按钮22')
btn2.setToolTip('停留一段时间显示')

window1.show()
window.show()
sys.exit(app.exec_())

ql2.setFocus()
ql2.clearFocus()

# TabFocus  只能使用Tab键才能获取焦点
# ClickFocus  只能使用鼠标点击才能获取焦点
# StrongFocus 上面两种都行
# NoFocus  上面两种都不行
# ql2.setFocusPolicy(Qt.StrongFocus)
