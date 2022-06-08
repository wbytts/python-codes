from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("展示控件对话框-QMessageBox消息盒子 - PyQt5中文网")
        self.resize(600, 500)
        self.func_list()

    def func_list(self):
        self.func()

    def func(self):
        # 1.构造函数1
        '''
        qmb = QMessageBox(self)
        qmb.show()  # 使用show还是模态对话框，窗口级别所以用open，系统重写了模态设置，可以通过下面两个方法改变
        # qmb.setModal(True)
        # qmb.setWindowModality(Qt.NonModal)
        '''
        # 2.构造函数2
        '''
        # 图标类型
        # QMessageBox.NoIcon  # 没有图标显示
        # QMessageBox.Question  # 显示提问图标
        # QMessageBox.Information  # 显示没有异常图标
        # QMessageBox.Warning  # 警告图标
        # QMessageBox.Critical  # 严重问题图标

        # 按钮类型
        # QMessageBox.Ok
        # QMessageBox.Open
        # QMessageBox.Save
        # QMessageBox.Cancel
        # QMessageBox.Close
        # QMessageBox.Discard
        # QMessageBox.Apply
        # QMessageBox.Reset
        # QMessageBox.Help
        # QMessageBox.Yes
        # ...
        # qmb = QMessageBox(QMessageBox.Information, '窗口标题', '<h1>提示信息</h1>', QMessageBox.Ok | QMessageBox.Close, self)

        # 3.消息盒子基础设置
        qmb = QMessageBox(self)
        qmb.setWindowTitle('窗口标题')
        qmb.setIcon(QMessageBox.Information)
        qmb.setIconPixmap(QPixmap(''))
        qmb.setText('<h1>提示信息</h1>')
        qmb.setInformativeText('内容提示')
        qmb.setCheckBox(QCheckBox('跳过此步骤', qmb))
        qmb.setDetailedText('此步骤此步骤此步骤此步骤此步骤')  # 详细信息文本

        # 3.按钮操作
        qmb.setStandardButtons(QMessageBox.Ok | QMessageBox.Close)
        # 自定义按钮 + 角色设置
        qmb.addButton(QPushButton('按钮', qmb), QMessageBox.YesRole)
        # 移除按钮
        # qmb.removeButton()
        # 焦点获取 or 默认按钮
        # qmb.setDefaultButton()
        '''

        '''
        # 4.按钮判定方法1 - 标准按钮
        qmb = QMessageBox(self)
        qmb.setWindowTitle('窗口标题')
        qmb.setText('<h2>提示信息</h2>')
        qmb.setInformativeText('内容提示内容提示内容提示内容提示内容提示内容提示内容提示')
        qmb.setStandardButtons(QMessageBox.Ok | QMessageBox.Close)
        # 在控件qmb中创建两个按钮,对应上面的两个按钮
        y_btn = qmb.button(QMessageBox.Ok)
        n_btn = qmb.button(QMessageBox.Close)
        def test(btn):
            if btn == y_btn:
                print('按钮OK被按下')
            else:
                print('按钮NO被按下')
        qmb.buttonClicked.connect(test)
        '''

        # 5.按钮判定方法2 - 角色按钮判定
        qmb = QMessageBox(self)
        qmb.setWindowTitle('窗口标题')
        qmb.setText('<h2>提示信息</h2>')
        qmb.setInformativeText('内容提示内容提示内容提示内容提示内容提示内容提示内容提示')
        qmb.addButton(QPushButton('确定', qmb), QMessageBox.YesRole)
        qmb.addButton(QPushButton('取消', qmb), QMessageBox.NoRole)

        def test(btn):
            role = qmb.buttonRole(btn)
            if role == QMessageBox.YesRole:
                print('确定被按下')
            else:
                print('取消被按下')

        qmb.buttonClicked.connect(test)

        # 6.文本交互 - 只能控制主标题
        qmb.setTextInteractionFlags(Qt.TextSelectableByMouse)

        # 7.静态方法
        # qmb.about()
        # qmb.aboutQt()
        # qmb.critical()
        # qmb.information()
        # qmb.question()
        qmb.question(self, '123', '321', QMessageBox.Ok | QMessageBox.Close)
        # qmb.warning(self, '123', '321')

        qmb.open()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())
