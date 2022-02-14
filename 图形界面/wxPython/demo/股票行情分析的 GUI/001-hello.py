# wxPython 工具库
import wx
# 日历控件 DatePickerCtrl 已经迁徙至 wx.adv 模块中
import wx.adv
# 电子表格控件 Grid，需要导入模块
import wx.grid
# 树形列表控件 TreeListCtrl，需要导入模块
import wx.gizmos

app = wx.App()  # 创建应用程序
frame = wx.Frame(None, -1, "Test Frame")
btn = wx.Button(frame, -1, label="Open")  # 在 frame 上实例化 wx.Button
frame.Show(True)  # 在调用 app.MainLoop 前显示 frame
app.MainLoop()  # 进入主事件循环
