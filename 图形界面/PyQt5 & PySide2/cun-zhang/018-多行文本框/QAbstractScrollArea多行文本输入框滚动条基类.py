from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('QAbstractScrollArea-多行文本框滚动条 - PyQt5中文网')
window.resize(600, 450)
window.move(300, 300)

qte = QTextEdit('多行文本框', window)
# 设置滚动条，设置滚动策略
# Qt.ScrollBarAlwaysOn
# Qt.ScrollBarAlwaysOff
# Qt.ScrollBarAsNeeded
qte.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
qte.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
qte.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)

# 角落控件
btn = QPushButton(window)
btn.setIcon(QIcon('123.jpg'))
qte.setCornerWidget(btn)

window.show()
sys.exit(app.exec_())
