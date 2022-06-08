from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('QFrame多行文本框基类边框样式设置 - PyQt5中文网')
window.resize(600, 450)
window.move(300, 300)

frame = QFrame(window)
frame.resize(350, 350)
frame.move(50, 50)
frame.setStyleSheet('background-color:gray')
# 框架形状
# QFrame.NoFrame
# QFrame.Box
# QFrame.Panel
# QFrame.HLine
# QFrame.VLine
# QFrame.StyledPanel
# QFrame.WinPanel
frame.setFrameShape(QFrame.HLine)

# 框架边框阴影
# QFrame.Plain
# QFrame.Raised
# QFrame.Sunken
frame.setFrameShadow(QFrame.Raised)

# 线宽
frame.setLineWidth(15)
frame.setMidLineWidth(20)
print(frame.frameWidth())  # 内线和外线宽度一样

# 框架样式
frame.setFrameStyle(QFrame.Box | QFrame.Raised)

# 框架矩形
frame.setFrameRect(QRect(50, 50, 250, 150))

window.show()
sys.exit(app.exec_())
