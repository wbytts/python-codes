from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QFileDialog文件选择对话框 - PyQt5中文网")
        self.resize(600, 500)
        self.func_list()

    def func_list(self):
        self.func()

    def func(self):
        '''  静态方法
        # 获取文件：只能获取文件路径
        # QFileDialog.getOpenFileName()
        # QFileDialog.getOpenFileNames()
        # QFileDialog.getOpenFileUrl()
        # QFileDialog.getOpenFileUrls()
        # QFileDialog.getSaveFileName()
        # QFileDialog.getSaveFileUrl()

        # 参数：父控件， 控件标题， 路径， 文件类型， 默认文件类型
        # res = QFileDialog.getOpenFileName(self, '文件选择', './', 'all(*.*);;images(*.png *.jpg);;python(*.py)', 'all(*.*)')
        # res = QFileDialog.getOpenFileNames(self, '文件选择', './', 'all(*.*);;images(*.png *.jpg);;python(*.py)', 'all(*.*)')
        # print(res)

        # 获取文件夹
        # QFileDialog.getExistingDirectory()  #
        # QFileDialog.getExistingDirectoryUrl()  #
        # res = QFileDialog.getOpenFileNames(self, '文件选择', './')
        # res = QFileDialog.getExistingDirectoryUrl(self, '文件选择', QUrl('./'))
        '''

        # 构造方法
        # fd = QFileDialog(self, '文件选择')
        fd = QFileDialog(self, '文件选择', './', 'all(*.*);;images(*.png *.jpg);;python(*.py)')

        # 接收模式和保存模式
        # QFileDialog.AcceptSave
        # QFileDialog.AcceptOpen
        # fd.setAcceptMode(QFileDialog.AcceptSave)  # 必须要有文件后缀名
        fd.setAcceptMode(QFileDialog.AcceptOpen)
        # fd.setDefaultSuffix('jpg')  # 设置默认文件后缀名

        '''
        # 选择文件模式
        # fd.setFileMode(QFileDialog.Directory)  # 选择目录
        # fd.setFileMode(QFileDialog.AnyFile)  # 选择文件
        # fd.setFileMode(QFileDialog.ExistingFile)  # 选择单个现有文件
        # fd.setFileMode(QFileDialog.ExistingFiles)  # 选择多个现有文件

        # 设置名称过滤器
        # fd.setNameFilter('image(*.jpg *.png)')
        # fd.setNameFilters(['all(*.*)', 'images(*.png *.jpg)', 'python(*.py)'])

        # 显示信息的详细程度，系统不兼容
        # fd.setViewMode(QFileDialog.List)
        # fd.setViewMode(QFileDialog.Detail)

        # 设置指定角色的标签名称
        fd.setLabelText(QFileDialog.FileName, '选择文件')
        fd.setLabelText(QFileDialog.Accept, '确定')
        fd.setLabelText(QFileDialog.Reject, '取消')
        fd.setLabelText(QFileDialog.FileType, '文件后缀')
        fd.setLabelText(QFileDialog.LookIn, '目录')

        # 可用信号
        # fd.currentChanged()  # 当前路径发生改变
        # fd.currentUrlChanged(QUrl)  # 当前路径URL改变
        # fd.directoryEntered()  # 进入选中文件夹
        # fd.directoryUrlEntered(QUrl)  # 进入选中文件夹URL时
        # fd.filterSelected()  # 选择名称后缀过滤器时
        # fd.fileSelected()  # 单个文件被选中
        # fd.fileSelected()  # 多个文件被选中
        # fd.urlSelected()  # 单个url被选中
        # fd.urlsSelected()  # 多个url被选中

        fd.currentChanged.connect(lambda str: print('当前路径发生改变', str))
        fd.filterSelected.connect(lambda filter: print('当前名称过滤器发生改变', filter))
        '''

        btn = QPushButton(self)
        btn.move(200, 200)
        btn.setText('打开对话框')
        btn.resize(100, 30)
        btn.clicked.connect(lambda: fd.show())

        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())
