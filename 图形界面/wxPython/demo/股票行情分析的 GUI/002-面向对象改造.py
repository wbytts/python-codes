# wxPython 工具库
import wx
# 日历控件 DatePickerCtrl 已经迁徙至 wx.adv 模块中
import wx.adv
# 电子表格控件 Grid，需要导入模块
import wx.grid
# 树形列表控件 TreeListCtrl，需要导入模块
import wx.gizmos

"""
自定义的 Frame 类、Panel 类，这样可以更灵活地设计我们所需要的 GUI 界面
"""


class Panel(wx.Panel):  # 继承 wx.Panel
    def __init__(self, parent):  # 构造函数
        wx.Panel.__init__(self, parent=parent, id=-1)
        # 此处添加 Panel 代码


class Frame(wx.Frame):  # 继承 wx.Frame
    def __init__(self):  # 构造函数
        wx.Frame.__init__(self, parent=None, title='Test Frame')
        self.DispPanel = Panel(self)
        # 此处添加各类控件
        btn = wx.Button(self.DispPanel, -1, label="Open")


class App(wx.App):  # 继承 wx.App
    def OnInit(self):
        """
        在应用程序创建后到事件循环开始前被 wx.App 父类调用，需要返回一个为 True 的布尔值
        :return:
        """
        self.frame = Frame()
        self.frame.Show()
        self.SetTopWindow(self.frame)  # 设置当前 Frame 为应用程序的顶级窗口
        return True


if __name__ == '__main__':
    app = App()
    # 应用程序一旦进入主事件循环，控制权将转交给 wxPython，程序会响应用户的鼠标和键盘事件。
    # 当应用程序的所有 Frame 关闭后 app.MainLoop()方法结束并退出程序。
    app.MainLoop()
