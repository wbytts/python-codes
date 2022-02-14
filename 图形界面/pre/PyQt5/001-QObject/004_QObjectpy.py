"""
什么是控件：一个程序界面上的各个独立的元素，具备不同的功能
常用控件：按钮、输入、展示、容器、结构、滚动。。。。。。

这里以按钮为例：
"""
from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle('这是一个标题')
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        self.QObject继承结构测试()
        # self.QObject对象名称和属性的操作()
        # self.测试QSS()
        # self.QObject父子对象操作()
        # self.信号操作()
        # self.类型判定()
        # self.事件处理()

    def QObject继承结构测试(self):
        # 001-QObject.__subclasses__()
        mros = QObject.mro()
        for mro in mros:
            print(mro)

    def QObject对象名称和属性的操作(self):
        # 测试API
        obj = QObject()
        # 对象名称
        obj.setObjectName('notice')
        print(obj.objectName())
        # 属性操作
        obj.setProperty('notice_level', 'error')
        obj.setProperty('xxx', 'qwe')
        print(obj.property('notice_level'))
        # 获取一个对象中所有通过 setProperty() 设置的属性名称
        print(obj.dynamicPropertyNames())

    def 测试QSS(self):
        label = QLabel(self)
        label.setText('wby')
        label.setStyleSheet('font-size:36px;color:red;')

        label2 = QLabel(self)
        label2.setText('wby')
        label2.move(200, 200)
        label2.resize(200, 100)
        with open('./qss/004_style.qss', 'r') as f:
            label2.setStyleSheet(f.read())  # 样式表也可以放在 Application 对象中

    def QObject父子对象操作(self):
        """
            setParent(parent) 设置父对象，父对象只能设置一个
            parent() 获取父对象
            children() 获取所有子对象，直接子对象（不是间接的）
            findChild()
                参数1：类型或者类型元组
                参数2：名称
                参数3：查找选项
                    Qt.FindChildrenRecursively 递归查找，默认
                    Qt.FindDirectChildrenOnly  只查找直接子对象
            findChildren(...)

            如果一个控件没有任何父控件，那么就会被当做顶层控件（窗口）
            多个顶层窗口相互独立
            如果想要一个控件被包含在另外一个控件内部，就需要设置父子关系
                显示位置受父约束，生命周期也被父对象接管

            QT对象树：所有对象都直接或者间接继承QObject
            QObject在一个树中组织它们，当创建了一个QObject，如果它使用了其他对象作为父对象，那么它就会被加入到这个对象的children列表中
            当父对象被销毁的时候，这个对象也会被销毁
        :return:
        """
        obj1 = QObject()
        obj2 = QObject()
        obj2.setParent(obj1)
        print('obj1', obj1)
        print('obj2', obj2)
        print(obj2.parent())

    def 信号操作(self):
        """
            信号signal和槽slot是qt中的核心机制，主要作用在于对象之间进行通讯
            信号：当一个控件的状态发生改变时，向外界发出的信息
            槽：一个执行某些操作的函数、方法
            所有继承自QWidget的控件都支持信号与槽的机制

            信号：控件内置、也可以自定义
            连接方式：obj.信号.connect(槽函数)
            特性：
                一个信号可以连接多个槽函数
                一个信号也可以连接另外一个信号
                信号的参数可以是任何Python类型
                一个槽可以监听多个信号

            取消连接：disconnect
            临时（取消）阻止指定控件所有的信号与槽的连接：widget.blockSignals(bool)
                True：取消，False：恢复
            信号是否被阻止：widget.signalsBlocked()
            返回连接到信号的接收器的数量：widget.receivers('信号')
        :return:
        """
        # 将obj绑定到对象上，防止自动释放
        self.obj = QObject()

        # obj.destroyed
        # obj.objectNameChanged
        def destroy_cao(obj):
            print('对象被释放了', obj)

        self.obj.destroyed.connect(destroy_cao)

        # 删除obj的引用，obj会被释放
        # del self.obj

        def obj_name_changed_cao(name):
            print('对象名称发生了改变', name)

        self.obj.objectNameChanged.connect(obj_name_changed_cao)
        self.obj.setObjectName('xxx')

        # 取消信号的连接
        self.obj.objectNameChanged.disconnect()
        self.obj.setObjectName('xxx2')

    def 类型判定(self):
        """
            obj.isWidgetType：判断是否是控件类型
            obj.inherit(父类)：一个对象是否继承（直接或间接）某个类
        :return:
        """
        obj = QObject()
        w = QWidget()
        btn = QPushButton()
        label = QLabel()

        objs = [obj, w, btn, label]
        for o in objs:
            print(o.isWidgetType())

    def 事件处理(self):
        """
            相对于信号与槽机制
                信号与槽机制是对事件机制的高级封装
                事件机制更偏底层（远离用户）
            API：
                childEvent()
                customEvent()
                eventFilter()
                installEventFilter()
                removeEventFilter()
                event()
        :return:
        """

    def 定时器(self):
        """
            startTimer(ms, Qt.TimerType) 开启一个定时器，返回timer_id（定时器唯一标识）
                Qt.TimerType：
                    Qt.PreciseTimer：精确定时器，尽可能保持毫秒准确
                    Qt.CoarseTimer：粗定时器，百分之5的误差间隔
                    Qt.VeryCoarseTimer：很粗的定时器，只能到秒级
            killTimer(timer_id)：根据定时器id，杀死定时器
            timerEvent()：定时器执行事件
        :return:
        """


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
