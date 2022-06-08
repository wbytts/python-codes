# 初学者不清楚各个类来自什么包，所以统一全部引入
from PyQt5.Qt import *
import sys
from qt_material import apply_stylesheet

# QApplication：qt的应用程序对象
# sys.argv 命令行参数
app = QApplication(sys.argv)
apply_stylesheet(app, theme='dark_teal.xml')

window = QWidget()  # 创建窗口对象
window.setWindowTitle("软件名称")  # 设置窗口标题
window.resize(600, 500)  # 改变窗口大小

btn = QPushButton(window)  # 创建按钮
btn.setText("按钮")  # 设置按钮上的文字
btn.resize(120, 30)  # 改变按钮大小
btn.move(100, 100)  # 移动按钮的位置

# 设置按钮样式
btn.setStyleSheet('''
    background-color: green;
    font-size: 16px;
    border: 4px solid red;
    border-radius: 10px;
''')

label = QLabel(window)  # 创建标签控件
label.setText('标签')  # 设置标签的文字

# 设置标签样式
label.setStyleSheet('''
    background-color: green;
    font-size: 16px;
    padding: 20px;
''')
# label.show()
window.show()  # 展示窗口

# 检测退出原因
sys.exit(app.exec_())
