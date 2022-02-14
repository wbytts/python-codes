from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("title")
window.resize(500, 500)
window.show()

"""
QCommandLinkButton
    命令链接是windows vista引入的新控件
    用途类似于单选按钮，在一组互斥的选项之间选择
    不应单独使用，而应作为向导和对话框中单选按钮的替代选项
    外观类似于平面按钮的外观，除了普通按钮文本之外，还允许描述性文本
    
创建：
    QCommandLinkButton(parent)
    QCommandLinkButton(text, parent)
    QCommandLinkButton(text, description, parent)

描述：
    setDescription(str)：描述设置
    description()：获取描述
    

"""

sys.exit(app.exec_())

