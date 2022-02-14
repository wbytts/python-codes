"""
002-QWidget：
    所有可视化控件的基类
    是一个最简单的空白控件
    控件是用户界面的最小元素
    每个控件都是矩形的，他们按Z轴顺序排序
    控件由其父控件和前面的控件剪切
    没有父控件的控件，称之为窗口

控件的创建：
    __init__(self, parent=None, flags)


flags：标志位


API：
    获取：
        x()：相对于父控件的x位置（包含窗口框架），顶层框架则是相对于桌面的位置
        y()：相对于父控件的y位置（包含窗口框架），顶层框架则是相对于桌面的位置
        pos()：x和y的组合 QPoint(x, y)
        width()：控件的宽度，不包含任何窗口框架
        height()：控件的高度，不包含任何窗口框架
        size()：width和height的组合 QSize(width, height)
        geometry()：用户区域相对于父控件的位置以及尺寸的组合 QRect(x, y, width, height)
        rect()：0， 0， width， height 的组合
        frameSize()：框架大小
        frameGeomrtry()：
        注意：窗口显示完毕后，相关的数值才会准确
    设置：
        move(x, y)：操作x和y，也就是pos
        resize(width, height)：操作宽高（不包括窗口框架）
        setGeometry(x_noFrame, y_noFrame, width, height)
        adjustSize()：根据内容自适应大小
        setFixSize()：设置固定尺寸
    最大和最小尺寸：
        获取：
            minimumWidth()：最小尺寸的宽度
            minimumHeight()：最小尺寸的高度
            minimumSize()：
            maximumWidth()：
            maximumHeight()：
            maximumSize()：
        设置：
            setMinimumWidth()：
            setMinimumHeight()：
            setMinimumSize()：
            setMaximumWidth()：
            setMaximumHeight()：
            setMaximumSize()：
        注意：控件完全展示后会有所差异
    内容边距：
        设置内容边距：setContentsMargins(左, 上, 右, 下)
        获取内容边距：getContentsMargins()，返回元组 (左, 上, 右, 下)
        获取内容区域：getContentsRect()
        注：必须是控件本身留够对应的大小
    鼠标相关操作：
        设置鼠标形状：setCursor()
            Qt.ArrowCursor
            Qt.UpArrowCursor
            Qt.CrossCursor
            Qt.IBeamCursor
            Qt.WaitCursor
            Qt.BusyCursor
            Qt.ForbidenCursor
            Qt.PointingHandCursor
            Qt.WhatThisCursor
            Qt.SizeVerCursor
            Qt.SizeHorCursor
            Qt.SizeBDiagCursor
            Qt.SizeAllCursor
            Qt.SplitVCursor
            Qt.SplitHCursor
            Qt.OpenHandCursor
            Qt.ClosedHandCursor
            Qt.BlankCursor
            自定义，QCursor对象
                pixmap = QPixmap('xxx.png')
                # 可以调整尺寸 pixmap.scaled(50, 50)
                cursor = QCursor(pixmap)
                # 可以设置参照的热点 cursor = QCursor(pixmap, hotX, hotY)
                xxx.setCursor(cursor)
        重置形状：unsetCursor()
        获取鼠标：cursor() 返回 QCursor对象
        鼠标跟踪：
            hasMouseTracking()：判断是否设置了鼠标跟踪
            setMouseTracking(bool)：
                设置鼠标是否跟踪
                所谓鼠标跟踪，其实就是设置检测鼠标移动事件的条件
                不跟踪：鼠标移动时，必须处于按下状态，才会触发mouseMoveEvent事件
                跟踪：鼠标移动时，不处于按下状态，也会触发mouseMoveEvent事件
        QCursor对象：
            pixmap()
            pos()
            setPos(x, y)
            ...
    父子关系扩充：
        childAt(x, y)：获取在指定坐标的控件
        parentWidget()：获取指定控件的父控件
        childrenRect()：所有子控件组成的边界矩形

    层级控制：
        lower()：将控件降低到最底层
        raise_()：将控件提升到最上层（注意有一个下划线）
        a.stackUnder(b)：将a放在b下面
        注：以上操作专指同级控件

    顶层窗口相关：
        图标：
            setWindowIcon(QIcon("xxx.png"))
            windowIcon()
        标题：
            setWindowTitle("标题")
            windowTitle()
        不透明度：
            setWindowOpacity(float)：0.0~1.0
            windowOpacity()
        窗口状态：
            setWindowState(state)
                Qt.WindowNoState：无状态
                Qt.WindowMinimized：最小化
                Qt.WindowMaximized：最大化
                Qt.WindowFUllScreen：全屏
                Qt.WindowActive：活动窗口
            windowState()
        最大化最小化：
            控制：
                showFullScreen()
                showMaximized()
                showMinimized()
                showNormal()
            判定：
                isMinimized()
                isMaximized()
                isFullScreen()
        窗口标志：
            window.setWindowFlags(Qt.WindowStaysOnTopHint)：
                窗口样式：
                    Qt.Widget
                        默认
                        是一个窗口或控件
                            有父控件，就是一般控件
                            没有父控件，则是窗口
                                窗口边框
                                标题栏
                                    图标
                                    标题
                                    最大化
                                    最小化
                                    关闭
                    Qt.Window
                    Qt.Dialog
                    Qt.Sheet
                    Qt.Drawer
                    Qt.Popup
                    Qt.Tool
                    Qt.ToolTip
                    Qt.SplashScreen
                    Qt.SubWindow
                顶层窗口外观标志：
                    Qt.MSWindowsFixedSizeDialogHint：窗口无法调整大小
                    Qt.FramelessWindowHint：窗口无边框
                    Qt.CustomizeWindowHint：有边框但是无标题栏和按钮，不能移动和拖动
                    Qt.WindowTitleHint：添加标题栏和一个关闭按钮
                    Qt.WindowSystemMenuHint：添加系统目录和一个关闭按钮
                    Qt.WindowMaximizeButtonHint：激活最大化和关闭按钮，禁用最小化按钮
                    Qt.WindowMinimizeButtonHint：激活最小化和关闭按钮，禁用最大化按钮
                    Qt.WindowMinMaxButtonsHint：激活最小化、最大化、关闭按钮
                    Qt.WindowCloseButtonHint：添加一个关闭按钮
                    Qt.WindowContextHelpButtonHint：添加问好和关闭按钮，同对话框
                    Qt.WindowStaysOnTopHint：窗口始终处于顶层位置
                    Qt.WindowStaysOnBottomHint：窗口始终处于底层位置
                注意：
                    窗口：没有父控件的控件，即顶层控件
                    控件：一般指非窗口控件
    交互状态：
        是否可用：
            setEnabled(bool)：设置控件是否可用
            isEnabled()：获取控件是否可用
        是否显示：
            setVisible(bool)：设置控件是否可见（传递的参数值为True也不一定可见）
                setHidden(bool)
                show()：显示控件
                hide()：隐藏控件
            isHidden()：判断控件是否隐藏，一般是基于父控件可见
            isVisible()：判断控件的最终状态是否可见
            isVisibleTo(widget)：如果能随着widget控件的显示和隐藏，而同步变化，则返回True
        是否隐藏：
        是否编辑：
            设置窗口标题 XXX[*]，这里的中括号不会显示，只会显示 *
            setWindowModified(bool)：
                被编辑状态：显示 *
                没有被编辑：不显示 *
            isWindowModified()：窗口是否是被编辑状态
        是否为活跃窗口：
            isActiveWindow()
            并不是谁在前面谁就是活动窗口
        关闭：
            close()
            补充：setAttribute(Qt.WA_DeleteOnClose, True)
            注：
        ！注意：
            visible：代表控件的最终的状态，是否被我们所见（被其他控件所遮挡也属于可见）
            hide：可理解为相对于父控件是否可见
            隐藏的一定是不可见的，反之不然

    信息提示：
        状态提示：
            statusTip()
            setStatusTip(str)
            效果：鼠标停在控件上，展示在状态栏
        工具提示：
            toolTip()
            setToolTip(str)
            时长：
                toolTipDuration()
                setToolTipDuration(msec)
            效果：鼠标悬停在控件上一会后，展示在旁边
        这是啥提示：
            whatsThis()
            setWhatThis(str)
            效果：切换到 查看这是啥 模式，点击该控件时显示

    焦点控制：
        单个控件角度：
            setFocus()：指定控件获取焦点
            setFocusPolicy(policy)：设置焦点获取策略
                Policy：
                    Qt.TabFocus：通过Tab键获取焦点
                    Qt.ClickFocus：通过被单击获得焦点
                    Qt.StrongFocus：可通过以上两种方式获得焦点
                    Qt.NoFocus：不能通过前两种方式获得焦点
            clearFocus()：取消焦点
        父控件角度：
            focusWidget()：获取子控件中当前焦点的控件
            focusNextChild()：聚焦下一个子控件
            focusPreviousChild()：聚焦上一个子控件
            focusNextPrevChild(bool)：True上一个，False下一个
            setTabOrder(pre_widget, next_widget)：静态方法，设置子控件获取焦点的先后顺序

    几个信号：
        windowTitleChanged(QString)：窗口标题改变信号
        windowIconChanged(QIcon)：窗口图标改变信号
        customContextMenuRequested(QPoint)：自定义上下文菜单请求信号
"""
from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)


class Window(QWidget):
    def mouseMoveEvent(self, mv):
        print('鼠标移动', mv.localPos())
        label = self.findChild(QLabel)
        pos = mv.localPos()
        label.move(pos.x(), pos.y())


window = Window()
window.setWindowTitle("title")
window.resize(500, 500)
window.show()

print(QWidget.__base__)
print('------')
print(QWidget.mro())

win2 = QWidget()
win2.setWindowTitle('XXX')
win2.resize(40, 40)
win2.setStyleSheet('background-color: red')
win2.setParent(window)
win2.show()

lab = QLabel(window)
lab.setText('厉害呀')
lab.setStyleSheet('font-size: 24px; background-color: green; color: red;')
lab.show()

sys.exit(app.exec_())
