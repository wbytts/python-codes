from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('QCheckBox-复选框 - PyQt5中文网')
window.resize(600, 450)
window.move(300, 300)

btn = QCheckBox('PyQt5', window)
btn.move(60, 60)
btn.resize(60, 35)
btn.setStyleSheet('background-color:green')
# ==============QCheckBox多选框三态设置=============== # 代码分割线 - 开始
btn.setTristate(True)  # 看效果
# 设置复选框状态
# btn.setChecked(True)  # 这个只能设置两种状态
btn.setCheckState(Qt.Unchecked)
btn.setCheckState(Qt.PartiallyChecked)
btn.setCheckState(Qt.Checked)
# ==============QCheckBox多选框三态设置=============== # 代码分割线 - 结束

# ==============QCheckBox信号=============== # 代码分割线 - 开始
# toggled 是指选中状态之后有没有发生切换，返会两种结果T  F
# btn.toggled.connect(lambda isChecked:print(isChecked))
btn.stateChanged.connect(lambda state: print(state))
# ==============QCheckBox信号=============== # 代码分割线 - 结束

window.show()
sys.exit(app.exec_())
