from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QSS样式加载方法 - PyQt5中文网")
        self.resize(600, 500)
        self.func_list()

    def func_list(self):
        self.func()

    def func(self):
        # 局部设置
        label1 = QLabel('标签1', self)
        # label1.setStyleSheet('background-color:green;')
        label1.move(100, 200)
        label1.resize(70, 30)

        label2 = QLabel('标签2', self)
        # label2.setStyleSheet('color:red;')
        label2.move(200, 200)
        label2.resize(70, 30)

        label3 = QLabel('标签3', self)
        # label3.setStyleSheet('background-color:yellow;font-size:30px;')
        label3.move(300, 200)
        label3.resize(70, 30)

        # 全局设置
        btn1 = QPushButton('按钮1', self)
        btn1.move(100, 100)
        btn1.resize(70, 30)
        btn2 = QPushButton('按钮2', self)
        btn2.move(200, 100)
        btn2.resize(70, 30)

        # btn1.setStyleSheet('''
        #     QPushButton{
        #             color:red;
        #         }
        #     QPushButton:hover{
        #             background-color: green;
        #         }
        # ''')

        # QSS文件加载
        btn3 = QPushButton('按钮3', self)
        btn3.setProperty('name', 'btn')
        btn3.move(100, 300)
        btn3.resize(70, 30)
        btn4 = QPushButton('按钮4', self)
        btn4.setObjectName('btn')
        btn4.move(200, 300)
        btn4.resize(70, 30)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()

    with open('index.qss', 'r', encoding='UTF-8') as f:
        app.setStyleSheet(f.read())

    # QssStyle = '''
    #         QPushButton:hover{
    #                 background-color: green;
    #             }
    #         QPushButton[name="btn"]:hover{
    #                 background-color: red;
    #             }
    #         QPushButton#btn:hover{
    #                 background-color: green;
    #                 color:red;
    #             }
    #         '''
    # # 全局设置
    # window.setStyleSheet(QssStyle)  # 当前窗口全局有效

    window.show()
    sys.exit(app.exec_())
