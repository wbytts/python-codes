import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

"""
把信号视作裁判鸣枪，而用于行动的槽函数则视作选手开跑，当裁判鸣枪后(即信号发出)，选手就开始往前跑(槽函数启动)
PyQt5中各个对象间或各个对象自身就是通过信号与槽机制来相互通信的
"""


# 该类继承QWidget，可以将QWidget看作是一种毛坯房，还没有装修，
# 而我们往其中放入QPushButton、QLabel等控件就相当于在装修这间毛坯房
class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        # 实例化一个QPushButton，因为继承于QWidget，所以self不能忘了(相当于告诉程序这个QPushButton是放在QWidget这个房子中的)；
        self.button = QPushButton('Start', self)
        # 连接信号与槽函数。
        # self.button就是一个控件，
        # clicked(按钮被点击)是该控件的一个信号，
        # connect()即连接，self.change_text即下方定义的函数(我们称之为槽函数)。
        # 所以通用的公式可以是：控件.控件的信号.connect(槽)
        # 控件和控件的信号也合称为信号，所以公式为：信号.connect(槽)
        self.button.clicked.connect(self.change_text)

    def change_text(self):
        print('change text')
        # 将按钮文本从‘Start’改成‘Stop’；
        self.button.setText('Stop')
        # 信号和槽解绑，解绑后再按按钮你会发现控制台不会再输出‘change text’（信号与槽解绑）
        # 如果把这行解绑的代码注释掉，你会发现每按一次按钮，控制台都会输出一次‘change text’；
        self.button.clicked.disconnect(self.change_text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 实例化Demo类
    demo = Demo()  # demo 其实是一个 QWidget（继承）
    # 使demo可见，其中的控件自然都可见(除非某控件刚开始设定隐藏)
    demo.show()
    sys.exit(app.exec())
