from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QInputDialog输入对话框 - PyQt5中文网")
        self.resize(600, 500)
        self.func_list()

    def func_list(self):
        self.func()

    def func(self):
        # 1.构造函数
        # Qt.MSWindowsFixedSizeDialogHint  # 窗口大小无法调整
        # Qt.FramelessWindowHint  # 无边框
        # Qt.CustomizeWindowHint  # 有边框，捂标题栏，不能拖动
        # Qt.WindowTitleHint  # 添加标题和关闭按钮
        # Qt.WindowSystemMenuHint  # 添加系统目录和关闭按钮
        # Qt.WindowMaximizeButtonHint  # 激活最大和关闭按钮，禁用最小按钮
        # Qt.WindowMinimizeButtonHint  # 激活最小和关闭按钮，禁用最大按钮
        # Qt.WindowMinMaxButtonsHint  # 激活最小、最大、关闭按钮
        # Qt.WindowCloseButtonHint  # 添加一个关闭按钮
        # Qt.WindowContextHelpButtonHint  # 添加问好和关闭窗口
        # Qt.WindowStaysOnTopHint  # 窗口始终处于顶层
        # Qt.WindowStaysOnBottomHint  # 窗口始终处于底层

        # qid = QInputDialog(self, Qt.FramelessWindowHint)
        qid = QInputDialog(self)

        # 2.文本框内容快速获取静态方法，参数填写参考文档
        # QInputDialog.getInt()  # 获取整形
        # QInputDialog.getDouble()  # 获取浮点型
        # QInputDialog.getText()  # 获取文本
        # QInputDialog.getMultiLineText()  # 获取多行文本
        # QInputDialog.getItem()  # 获取下拉条目
        # print(QInputDialog.getInt(self, '标题1', '标题2', 999, step=9))  # step步长
        # QInputDialog.getDouble(self, '标题1', '标题2', 999.2, decimals=3)  # decimals小数位数
        # QInputDialog.getText(self, '标题1', '标题2', echo=QLineEdit.Password)  # echo输出模式
        # QInputDialog.getItem(self, '标题1', '标题2', ['111', '222', '333'], 2, True)  # 2为默认值下标，True为回车==确定

        # 3.界面文本设置
        qid.setOkButtonText('确定')
        qid.setLabelText('文本')
        qid.setCancelButtonText('退出')

        # 4.选项设置
        # QInputDialog.InputDialogOption
        # QInputDialog.NoButtons  # 不显示确定和取消按钮
        # QInputDialog.UseListViewForComboBoxItems  # 直接使用列表展示条目，不可编辑
        # QInputDialog.UsePlainTextEditForTextInput  # 使用下拉列表展示条目，不可编辑
        # qid.setOption(QInputDialog.UseListViewForComboBoxItems, on=True)  # 设置控件展示下面items条目
        # qid.setComboBoxItems(['aaa', 'eee', '123'])

        # 5.输入模式
        # qid.setInputMode(QInputDialog.IntInput)
        # qid.setInputMode(QInputDialog.TextInput)
        # qid.setInputMode(QInputDialog.DoubleInput)

        # 整形
        # qid.setIntMaximum(80)  # 最大值
        # qid.setIntMinimum()  # 最小值
        # qid.setIntRange()  # 范围
        # qid.setIntStep()  # 步长
        # qid.setIntValue()  # 默认值

        # 浮点型
        # qid.setDoubleMaximum()
        # qid.setDoubleMinimum()
        # qid.setDoubleDecimals()  # decimals小数位数
        # qid.setDoubleRange()
        # qid.setDoubleStep()
        # qid.setDoubleValue()

        # 字符串
        # qid.setTextEchoMode()  # 输出模式：明文、密文...
        # qid.setTextValue()  # 默认字符串

        # 下拉列表
        # qid.setComboBoxItems(['aaa', 'eee', '123'])  # 下拉列表条目
        qid.setComboBoxEditable(True)  # 可编辑下拉列表框

        # 可用信号
        # qid.intValueChanged()
        # qid.intValueSelected()
        # qid.doubleValueChanged()
        # qid.doubleValueSelected()
        # qid.textValueChanged()
        # qid.textValueSelected()

        qid.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())
