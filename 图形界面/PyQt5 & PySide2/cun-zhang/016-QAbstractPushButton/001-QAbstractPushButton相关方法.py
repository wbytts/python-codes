'''
1.提示文本：setText()  text()
2.图像：setIcon()   setIconSize()   icon()   iconSize()
3.快捷键：
4.自动重复：
setAutoRepeat()   设置自动重复
setAutoRepeatInterval(毫秒)   设置自动重复间隔
setAutoRepeatDelay(毫秒)    设置首次自动重复延时
autoRepeat()   获取自动重复
autoRepeatInterval()   获取自动重复间隔
autoRepeatDelay()    获取首次自动重复延时
5.按钮状态：setDown(bool) isDown() isChecked()  setChecked(bool)  isCheckable()  setCheckable()  toggle()全选/反选
继承：QWidget中的：isEnabled() setEnabled(bool)
6.排他性：autoExclusive()  setAutoExclusive(bool)
7.模拟点击：click()  animateClick(ms)
8.按钮点击有效区域设置：hitButton(QPoint)
'''

from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('QAbstractButton')
window.resize(600, 450)
window.move(300, 300)

btn = QPushButton(window)
btn.setText('按钮')

# ==============图标设置=============== # 代码分割线 - 开始
qicon = QIcon('123.jpg')
btn.setIcon(qicon)

qsize = QSize(5, 5)
btn.setIconSize(qsize)

print(btn.icon())
print(btn.iconSize())
# ==============图标设置=============== # 代码分割线 - 结束

# ==============快捷键设置=============== # 代码分割线 - 开始
btn.pressed.connect(lambda: print('WWWWW'))
# btn.setText('&aaaa')    # Alt + &后面的首字母
btn.setShortcut('Ctrl+s')  # 这个使用起来更加自由
# ==============快捷键设置=============== # 代码分割线 - 结束

# ==============自动重复=============== # 代码分割线 - 开始
print(btn.autoRepeat())
btn.setAutoRepeat(True)
btn.setAutoRepeatInterval(1000)
btn.setAutoRepeatDelay(3000)
# ==============自动重复=============== # 代码分割线 - 结束

# ==============按钮状态=============== # 代码分割线 - 开始
btn2 = QPushButton(window)
btn2.setText('第二个按钮')
btn2.move(100, 100)
btn2.setStyleSheet('QPushButton:pressed {background-color:green}')
btn2.setDown(True)

btn3 = QRadioButton(window)
btn3.setText('单选按钮')
btn3.move(150, 150)


def tog():
    # btn3.toggle()
    btn3.setChecked(not btn3.isChecked())


btn2.pressed.connect(tog)
# ==============按钮状态=============== # 代码分割线 - 结束

# ==============排他性=============== # 代码分割线 - 开始
btn4 = QCheckBox(window)
btn4.move(200, 200)
btn4.setText('男')
btn4.setAutoExclusive(True)

btn5 = QCheckBox(window)
btn5.move(200, 230)
btn5.setText('女')
btn5.setAutoExclusive(True)
# ==============排他性=============== # 代码分割线 - 结束

# ==============按钮模拟点击=============== # 代码分割线 - 开始
btn6 = QPushButton(window)
btn6.setText('模拟点击')
btn6.move(300, 300)
# btn6.click()
btn6.animateClick(2000)


# ==============按钮模拟点击=============== # 代码分割线 - 结束


# ==============按钮点击有效区域设置=============== # 代码分割线 - 开始
class Btn2(QPushButton):
    def hitButton(self, poi):
        print(poi)
        if poi.x() > self.width() / 2:
            return True
        return False


btn6 = Btn2(window)
btn6.setText('有效区域')
btn6.move(0, 300)
btn6.pressed.connect(lambda: print('========='))
# ==============按钮点击有效区域设置=============== # 代码分割线 - 结束
window.show()
sys.exit(app.exec_())
