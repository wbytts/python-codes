from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QSS-语法声明-背景设置 - PyQt5中文网")
        self.resize(600, 500)
        self.func_list()

    def func_list(self):
        self.func()

    def func(self):
        label1 = QLabel('外边距和内边距设置', self)
        label1.resize(300, 300)
        btn = QPushButton(self)
        btn.move(300, 300)
        btn.resize(110, 110)

        '''样式叠加
        hb = QHBoxLayout(self)
        for i in range(0, 4):
            btn = QPushButton(self)
            btn.move(300, 300)
            # btn.resize(110, 110)
            btn.setFixedSize(110, 110)
            print(i)
            btn.setStyleSheet("""
            QPushButton{
                padding-left: -%dpx;
                padding-top: -%dpx;
                }
            """ % (i * 175 + 25, 35))
            hb.addWidget(btn)
        '''

        '''
        background
        background-color  # 背景颜色
        background-image  # 背景图片
        background-position  # 背景位置
        background-origin  # 背景延伸范围
        background-clip  # 裁剪掉边框外的部分
        background-repeat  # 背景重复
        background-attachment  # 固定背景图像,取值scroll(背景跟随滚动)和fixed(背景不滚动)
        '''

        '''背景图片调整
        QPushButton{
            background-image: url(btn-ico.jpg);
            border: 5px solid lightblue;
            background-origin: content;
            background-clip: padding;
            padding-left: -25px;  // 边框宽度也要计算在内
            padding-top: -35px;
        }
        '''

        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()

    with open('base7.qss', 'r', encoding='UTF-8') as f:
        qApp.setStyleSheet(f.read())

    window.show()
    sys.exit(app.exec_())
