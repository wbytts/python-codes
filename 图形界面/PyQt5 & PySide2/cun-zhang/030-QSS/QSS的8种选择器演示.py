from PyQt5.Qt import *
import sys


class Btn(QPushButton):
    pass


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QSS选择器使用方法总结 - PyQt5中文网")
        self.resize(600, 500)
        self.func_list()

    def func_list(self):
        self.func()

    def func(self):
        box = QWidget(self)
        box.setObjectName('box')

        box1 = QWidget(box)
        box1.setObjectName('box')
        box1.resize(100, 60)
        box1.move(250, 200)
        box1.setStyleSheet('border:1px solid red')

        label1 = QLabel('标签1', box)
        label1.move(100, 200)
        label1.resize(100, 50)
        label1.setObjectName('aaa')
        label2 = QLabel('标签2', box1)
        label2.move(250, 200)
        label2.resize(100, 50)
        label2.setStyleSheet('color:red;')
        label3 = QLabel('标签3', self)
        label3.move(400, 200)
        label3.resize(100, 50)
        label3.setObjectName('bbb')

        btn1 = QPushButton('按钮1', box)
        btn1.move(100, 100)
        btn1.resize(100, 50)
        btn1.setProperty('name', 'btn1')
        btn2 = QPushButton('按钮2', self)
        btn2.move(250, 100)
        btn2.resize(100, 50)
        btn3 = QPushButton('按钮3', self)
        btn3.setProperty('name', 'btn')
        btn3.move(100, 300)
        btn3.resize(100, 50)
        btn4 = Btn('按钮4', self)
        btn4.setObjectName('btn')
        btn4.move(250, 300)
        btn4.resize(100, 50)

        print(box1.children())

        ck = QCheckBox('选择正确答案', self)
        ck.move(150, 400)
        ck.resize(100, 40)

        sb = QSpinBox(self)
        sb.move(300, 400)
        sb.resize(100, 40)

        # 1.通配符选择器：匹配所有控件
        '''
        *{  // 用*号匹配所有控件
            color:green;
        }
        '''
        # 2.类型选择器（通过控件类型来匹配控件包含子类）
        '''
        QPushButton{
            font-size:30px;
        }

        Btn{
            font-size:30px;
        }
        '''
        # 3.类选择器(通过控件类型匹配 不包括子类)
        '''
        .QPushButton{
            font-size: 30px;
        }
        '''
        # 4.ID选择器setObjectName
        '''
        #btn{
            background-color:green;
        }
        '''
        # 5.属性选择器setProperty
        '''
        QPushButton[name="btn"]:hover{
            background-color:red;
        }
        // 表示只要加上setProperty的所有name属性按钮都是红色背景，不影响其他无样式按钮的新建
        QPushButton[name]:hover{
            background-color:red;
        }
        '''
        # 6.后代选择器(通过父控件直接或间接作用于子控件)
        '''
        QWidget#box QPushButton{
            background-color:green;
        }
        '''
        # 7.子选择器（直接包含的子控件）
        '''
        QWidget#box>QLabel{
            background-color:green;
        }
        '''
        # 8.子控件选择器(主要用于组合控件中的一部分组件样式修改)
        # 8.1.常见伪状态
        '''
        :checked  # 控件被选中
        :unchecked  # 控件被取消选中
        :hover  # 鼠标停留
        :pressed  # 控件被按下
        :focus  # 获取到焦点
        :disable  # 失效控件
        :enable  # 有效控件
        :indeterminate  # checkBox或radioButton被部分选中
        :on  # 开启状态
        :off  # 关闭状态
        '''
        # 8.2.常用组合控件子控件
        '''
        QCheckBox, QRadioButton    ::indicator
        QComboBox                  ::drop-down
        QSpinBox, QDateEdit, QTimeEdit, QDateTimeEdit    ::up-button  ::down-button  ::up-arrow  ::down-arrow
        QSlider                    ::groove  ::handle  ::add-page  ::sub-page
        QProgressBar               ::chunk
        QScrollBar                 ::sub-line, ::add-line  ::sub-page, ::add-page  ::up-arrow, ::down-arrow  ::left-arrow, ::right-arrow
        QGroupBox                  ::title  ::indicator
        QTableView                 ::item
        QHeaderView, QTableCornerButton   ::section
        QTreeView                  ::item  ::branch
        QHeaderView                ::section
        QTabWidget                 QTabWidget::pane  QTabWidget::tab-bar  QTabBar::tab  QTabBar::close-button  QTabBar::tear  QTabBar::scroller  QTabBar QToolButton::left-arrow  QTabBar QToolButton::right-arrow
        '''

        '''
        QCheckBox::indicator{
            width: 20px;
            height: 20px;
        }
        QCheckBox::indicator:checked{
            image: url(y.png);
        }
        QCheckBox::indicator:unchecked{
            image: url(n.png);
        }
        '''

        # 9.选择器的组合使用(使用逗号隔开)
        '''
        #aaa,#bbb{
            color: red;
        }
        '''

        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()

    with open('test.qss', 'r', encoding='UTF-8') as f:
        qApp.setStyleSheet(f.read())

    window.show()
    sys.exit(app.exec_())
