from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('QCommandLinkButton-命令链接按钮 - PyQt5中文网')
window.resize(600, 450)
window.move(300, 300)

btn = QPushButton(window)
btn.move(160, 160)
btn.resize(50, 35)
btn.setText('按钮控件')
btn.setStyleSheet('background-color:green')

btn2 = QCommandLinkButton('标题', '描述', window)
btn2.setText('标题标题标题')
btn2.setDescription('描述描述描述描述描述描述')
btn2.setIcon(QIcon('123.jpg'))
# QCommandLinkButton中的信号完全使用的是父类QPushbutton的

window.show()
sys.exit(app.exec_())
