import sys
from PyQt5.QtWidgets import QApplication, QLabel


if __name__ == '__main__':
    app = QApplication(sys.argv)
    label = QLabel()
    # 我们可以直接在字符串中加上html代码，修改文本样式。
    label.setText('<font color="red">Hello</font> <h1>World</h1>')
    label.show()
    sys.exit(app.exec_())
