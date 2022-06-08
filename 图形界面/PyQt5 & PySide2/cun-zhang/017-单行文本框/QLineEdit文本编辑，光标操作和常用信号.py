from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('QLineEdit常见方法和信号')
window.resize(600, 450)
window.move(300, 300)

led = QLineEdit(window)
led.setText('单行文本框')
led.move(100, 100)

btn = QPushButton('复制', window)
btn.move(100, 130)


def cpoy_btn():
    print(led.isModified())
    led.setModified(False)


btn.pressed.connect(cpoy_btn)

led1 = QLineEdit(window)
led1.setText('光标位置控制方法')
led1.move(250, 100)

btn1 = QPushButton('按钮', window)
btn1.move(250, 130)


# False表示只移动不选中，True表示选中加移动
# cursorBackward
# cursorForward
# cursorWordBackward  # 按照单词长度移动，不用输入步长，以空格为间隔
# cursorWordForward
# home
# end
def cur_move():
    # led1.cursorBackward(False,2)
    # led1.cursorBackward(True,2)
    # led1.home(True)
    # led1.setCursorPosition(len(led1.text()/2))
    # led1.setCursorPosition(3)
    # led1.cursorWordForward(True)
    led1.setFocus()
    led1.setSelection(1, 4)


btn1.pressed.connect(cur_move)

# 文本对其方式设置
led2 = QLineEdit(window)
led2.setText('光标位置控制方法')
led2.move(100, 200)
led2.resize(200, 200)
led2.setTextMargins(0, 10, 20, 0)  # 左上右下
led2.setAlignment(Qt.AlignRight | Qt.AlignTop)

# 常见编辑功能
# backspace()  退格
# del_()  删除
# clear()  清空
# copy()  赋值
# cut()  剪切
# paste()  粘贴
# isUndoAvailable()  undo()  撤销
# isRedoAvailable()  redo()  重做
# setDragEnabled()  拖放


# 文本选中方法
# setSelection
# 放在led的槽函数中测试
# led.setSelection(1,2)  # 选中指定区域文本
# led.selectAll()  # 选中所有文本
# led.deselect()  # 取消选中文本
# led.hasSelectedText()  # 是否有选中文本
# led.selectedText()  # 获取选中文本
# led.selectionStart() # 选中的开始位置
# led.selectionEnd()  # 选中的结束位置
# led.selectionLength() # 选中的文本长度


# 可用信号
# textEdited()  # 文本编辑时发出的信号
# textChanged()  # 文本发生改变时
# returnPressed()  # 回车键被按下时
# editingFinished()  # 结束编辑的时候
# cursorPositionChanged()  # 光标位置发生改变时
# selectionChanged()  # 选中的文本发生改变的时候
led3 = QLineEdit(window)
led3.move(350, 200)
led3.resize(150, 60)

led4 = QLineEdit(window)
led4.move(350, 270)
led4.resize(150, 60)
# led3.textEdited.connect(lambda val:print('文本编辑时发出的信号',val))  # 用户在前段编辑的时候触发
# led3.textChanged.connect(lambda val:print('文本发生改变时',val))  # 前后端有任何变化都会触发
# led3.setText('123')
# led3.returnPressed.connect(lambda :print('123',led4.setFocus()))
led3.editingFinished.connect(lambda: print('结束编辑的时候'))

window.show()
sys.exit(app.exec_())
