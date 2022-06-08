from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('QLineEdit-单行文本编辑器 - PyQt5中文网')
window.resize(600, 450)
window.move(300, 300)

btn = QPushButton(window)
btn.move(50, 50)
btn.setText('按钮')

# 构造
led = QLineEdit(window)
# ==============文本内容的设置和获取=============== # 代码分割线 - 开始
'''
setText()  设置文本内容
insert(mewText) 在光标处插入文本
text()  获取真实的文本内容
displayText() 获取用户能看到的内容
'''
# led.setText('11111')  # 或覆盖构造时默认的文本,这和QPushButton中的setText不一样
# led.insert('22')  # 如果文本框是空的，就和setText是一样的功能
# btn.pressed.connect(lambda :led.insert('WWW'))
# print(led.text())
# btn.pressed.connect(lambda :print(led.text()))
# print(led.displayText())
# btn.pressed.connect(lambda :print(led.displayText()))
# ==============文本内容的设置和获取=============== # 代码分割线 - 结束
# 案例：两个文本框，通过按钮把上一个文本框的内容复制到下一个
# ==============QLineEdit文本框输出模式=============== # 代码分割线 - 开始
# setEchoMode() 明文Normal=0、密文Password=2、不输出NoEcho=1、编辑时明文，结束后密文PasswordEchoOnEdit=3
# 以上的枚举值都是类属性，所以样用QLineEdit调用出来
led.setEchoMode(QLineEdit.Normal)
# ==============QLineEdit文本框输出模式=============== # 代码分割线 - 结束

# ==============QLineEdit占位提示=============== # 代码分割线 - 开始
# setPlaceholderText()
# placeholderText()
led.setPlaceholderText('请输入密码')
# ==============QLineEdit占位提示=============== # 代码分割线 - 结束

# ==============QLineEdit清空按钮=============== # 代码分割线 - 开始
led.setClearButtonEnabled(True)
# ==============QLineEdit清空按钮=============== # 代码分割线 - 结束

# ==============QLineEdit添加明文/密文操作行为=============== # 代码分割线 - 开始
action = QAction(led)  # 创建一个QAction对象放在led表单中
action.setIcon(QIcon('close.png'))  # 给对象设置图标


def change():
    if led.echoMode() == QLineEdit.Normal:
        led.setEchoMode(QLineEdit.Password)
        action.setIcon(QIcon('close.png'))
    else:
        led.setEchoMode(QLineEdit.Normal)
        action.setIcon(QIcon('open.png'))


action.triggered.connect(change)
led.addAction(action, QLineEdit.TrailingPosition)  # 接收对象，指定存放位置
# ==============QLineEdit添加明文/密文操作行为=============== # 代码分割线 - 结束

# ==============QLineEdit自动补全=============== # 代码分割线 - 开始
qcompleter = QCompleter(['aaa', 'abc', 'AAA', '123', '136'], led)
led.setCompleter(qcompleter)  # led改为明文显示
# ==============QLineEdit自动补全=============== # 代码分割线 - 结束

# ==============输入限制=============== # 代码分割线 - 开始
led.setMaxLength(5)  # 字符长度限制
led.setReadOnly(True)  # 制度设置
# ==============输入限制=============== # 代码分割线 - 结束

window.show()
sys.exit(app.exec_())
