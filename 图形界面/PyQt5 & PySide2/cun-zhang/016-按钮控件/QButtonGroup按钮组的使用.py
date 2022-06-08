from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('QButtonGroup - PyQt5中文网')
window.resize(600, 450)
window.move(300, 300)

btn1 = QRadioButton('男', window)
btn1.setIcon(QIcon('1.png'))
btn1.move(60, 60)
btn1.resize(60, 35)
btn1.setChecked(True)
btn1.setStyleSheet('background-color:green')

btn2 = QRadioButton('女', window)
btn2.setIcon(QIcon('2.png'))
btn2.move(60, 120)
btn2.resize(60, 35)
btn2.setStyleSheet('background-color:green')
sex_group = QButtonGroup(window)  # 创建按钮组，放在父控件内
sex_group.addButton(btn1, 1)
sex_group.addButton(btn2, 2)

btn3 = QRadioButton('是', window)
btn3.move(200, 60)
btn3.resize(60, 35)
btn3.setStyleSheet('background-color:green')

btn4 = QRadioButton('否', window)
btn4.move(200, 120)
btn4.resize(60, 35)
btn4.setStyleSheet('background-color:green')
group2 = QButtonGroup(window)
group2.addButton(btn3, 3)
group2.addButton(btn4, 4)

# print(sex_group.buttons())  # 获取组中所有按钮
# print(sex_group.button(1))  # 获取组中ID=1的按钮
# print(sex_group.checkedButton())  # 获取组中选中按钮
# 如果不设置按钮ID，按钮ID会默认为-1，并逐个递减

# sex_group.removeButton(btn2)  # 从组中移除按钮，注意这时候的互斥关系

# 按钮ID设置，放在组中设置
group2.setId(btn3, 3)
group2.setId(btn4, 4)
# print(group2.id(btn4))
# print(group2.checkedId()) # 没有选中的话结果是-1

# 独占设置
group2.setExclusive(True)


# 可用信号
def test(val):
    print(val)


# group2.buttonToggled.connect(test)
# 这里会传出两个信号，下面是选择信号的方法[int] or [QAbstractButton]
group2.buttonClicked[QAbstractButton].connect(test)
# group2.buttonPressed[int].connect(test)
# group2.buttonReleased.connect(test)


window.show()
sys.exit(app.exec_())
