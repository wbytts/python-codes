from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QComboBox下拉框控件 - PyQt5中文网")
        self.resize(600, 500)
        self.func_list()

    def func_list(self):
        self.func()

    def func(self):
        self.qcb = QComboBox(self)
        self.qcb.move(150, 150)
        self.qcb.resize(150, 40)

        self.btn = QPushButton('按钮', self)
        self.btn.resize(60, 30)
        self.btn.move(150, 250)
        self.btn.pressed.connect(self.test)

    def test(self):
        # 增加条目
        # self.qcb.addItem('PyQt5中文网')
        # self.qcb.addItem(QIcon('123.jpg'), 'pyqt5视频教程')
        # self.qcb.addItems(['pyqt', 'pyqt5', 'python', 'django'])  # 数组
        # self.qcb.addItems(('pyqt', 'pyqt5', 'python', 'django'))  # 元祖

        # 插入条目
        # self.qcb.insertItem(1, 'PyQt5中文网')
        # self.qcb.insertItem(3, QIcon('123.jpg'), 'pyqt5视频教程')
        # self.qcb.insertItems(2, ['pyqt','pyqt5','python','django'])

        # 设置条目，可以修改指定位置的图标和标题
        # self.qcb.setItemIcon(2, QIcon('123.jpg'))
        # self.qcb.setItemText(2, 'django')
        # self.qcb.setItemData(2, QIcon('123.jpg'))  # 用户数据(获取来的)

        # 删除条目
        # self.qcb.removeItem(2)

        # 插入分割线
        # self.qcb.insertSeparator(2)

        # 下拉框默认值设定
        # self.qcb.setCurrentIndex(2)  # 通过匹配索引设置下拉框默认值
        # self.qcb.setCurrentText('python')  # 通过匹配下拉框字符串设置下拉框默认值
        # self.qcb.setEditable(True)  # 文本可编辑，并可添加
        # self.qcb.setEditText('WWWWWW')  # 让下拉框中文本可以被编辑,首先要设置成可编辑

        # 数据获取
        self.qcb.addItem(QIcon('123.jpg'), 'python', {'name', 'PyQt5'})
        # print(self.qcb.count())  # 条目个数
        print(self.qcb.itemIcon(3))  # 指定条目图片对象
        # print(self.qcb.itemIcon(self.qcb.currentIndex()))  # 指定索引的图片对象
        # print(self.qcb.itemText(3))  # 指定条目标题
        print(self.qcb.itemData(0))  # 指定条目数据{'name', 'PyQt5'}
        # print(self.qcb.currentIndex())  # 当前索引
        # print(self.qcb.currentText())  # 当前文本
        print(self.qcb.currentData())  # 返回当前数据{'name', 'PyQt5'}

        # 下拉框数据个数限制
        self.qcb.setMaxCount(8)  # 设置最大存储条目个数
        self.qcb.setEditable(True)
        self.qcb.setMaxVisibleItems(10)  # 设置最大可见的条目个数

        # 可重复
        self.qcb.setDuplicatesEnabled(False)  # 条目中不能出现两个或多个重复数据

        # 有边框
        self.qcb.setFrame(False)

        # 图标尺寸
        self.qcb.setIconSize(QSize(20, 20))

        # 尺寸调整策略
        # QComboBox.AdjustToContents
        # QComboBox.AdjustToMinimumContentsLength
        # QComboBox.AdjustToContentsOnFirstShow  # 默认值
        # QComboBox.AdjustToMinimumContentsLengthWithIcon
        self.qcb.setSizeAdjustPolicy(QComboBox.AdjustToMinimumContentsLength)  # 调整下拉框宽度

        # 清空
        self.qcb.clear()  # 清空下拉内容
        self.qcb.clearEditText()  # 清空被编辑的内容
        self.qcb.showPopup()  # 弹出下拉框

        # 下拉匹配
        self.qcb.setCompleter(QCompleter(['pyqt', 'pyqt5', 'python', 'django']))

        # 可用信号
        # self.qcb.activated()  # 某个条目被用户选中，
        # self.qcb.currentIndexChanged()  # 当前选中条目索引发生改变
        # self.qcb.currentTextChanged()  # 当前选中条目文本发生变化
        # self.qcb.editTextChanged()  # 编辑文本时
        # self.qcb.highlighted()  # 高亮==鼠标停留产生的高亮

        # self.qcb.activated.connect(lambda val: print(val))
        # self.qcb.activated[str].connect(lambda val: print(val))
        # self.qcb.currentIndexChanged.connect(lambda val: print(val))
        # self.qcb.currentIndexChanged[str].connect(lambda val: print(val))
        # self.qcb.setEditable(True)
        # self.qcb.editTextChanged.connect(lambda val: print(val))
        self.qcb.highlighted.connect(lambda val: print(val))

        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())
