# wxPython 工具库
import wx
# 日历控件 DatePickerCtrl 已经迁徙至 wx.adv 模块中
import wx.adv
# 电子表格控件 Grid，需要导入模块
import wx.grid
# 树形列表控件 TreeListCtrl，需要导入模块
import wx.gizmos
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wx import NavigationToolbar2Wx as NavigationToolbar
from matplotlib.figure import Figure
import numpy as np


class Panel(wx.Panel):
   def __init__(self, parent):
       wx.Panel.__init__(self,parent=parent, id=-1)

       self.figure = Figure()
       self.subplot = self.figure.add_subplot(1, 1, 1)

       self.FigureCanvas = FigureCanvas(self, -1, self.figure) # figure 加到 FigureCanvas
       self.TopBoxSizer = wx.BoxSizer(wx.VERTICAL)
       self.TopBoxSizer.Add(self.FigureCanvas, proportion=10, border=2, flag=wx.ALL | wx.EXPAND)
       self.TopBoxSizer.Add(self.add_slider_ctr(), proportion = 0.5, border = 2,flag = wx.ALL | wx.EXPAND)

       self.SetSizer(self.TopBoxSizer)

   def add_slider_ctr(self):

       self.WindowPanel = wx.Panel(self, -1)
       self.slider = wx.Slider(self.WindowPanel, minValue=0, maxValue=600, size=(600, -1),
                               style=wx.SL_HORIZONTAL)
       self.slider.SetTickFreq(5)
       return self.WindowPanel

class Panel_sw(wx.Panel):
   def __init__(self, parent):
       wx.Panel.__init__(self, parent=parent, id=-1)

       self.figure = Figure()
       self.subplot = self.figure.add_subplot(1, 1, 1)

       self.FigureCanvas = FigureCanvas(self, -1, self.figure)  # figure 加到 FigureCanvas
       self.NavigationToolbar = NavigationToolbar(self.FigureCanvas)  # 创建导航工具
       #self.StaticText = wx.StaticText(self, -1, label='Show Help String')  # 创建标签

       self.SubBoxSizer = wx.BoxSizer(wx.HORIZONTAL)
       self.SubBoxSizer.Add(self.NavigationToolbar, proportion=-1, border=2, flag=wx.ALL | wx.EXPAND)
       #self.SubBoxSizer.Add(self.StaticText, proportion=-1, border=2, flag=wx.ALL | wx.EXPAND)

       self.TopBoxSizer = wx.BoxSizer(wx.VERTICAL)
       self.TopBoxSizer.Add(self.SubBoxSizer, proportion=-1, border=2, flag=wx.ALL | wx.EXPAND)
       self.TopBoxSizer.Add(self.FigureCanvas, proportion=-1, border=2, flag=wx.ALL | wx.EXPAND)

       self.SetSizer(self.TopBoxSizer)

# proportion 参数控制容器尺寸比例
class Frame(wx.Frame):

   def __init__(self):
       wx.Frame.__init__(self, parent = None, title = u'量化软件', size=(1000,600),
                     style=wx.DEFAULT_FRAME_STYLE^wx.MAXIMIZE_BOX)

       # 创建显示区面板
       self.DispPanel = Panel(self) # 自定义
       # 创建参数区面板
       self.ParaPanel = wx.Panel(self,-1)
       # self.ParaPanel.SetBackgroundColour('black') # 设置背景色彩
       # 创建控制面板
       self.CtrlPanel = wx.Panel(self,-1)

       # 第二层布局
       vbox_sizer_a = wx.BoxSizer(wx.VERTICAL) # 纵向 box
       vbox_sizer_a.Add(self.add_stock_para_lay() , proportion=0, flag=wx.EXPAND|wx.BOTTOM, border=5) # 添加行情参数布局
       vbox_sizer_a.Add(self.add_back_para_lay()  , proportion=0, flag=wx.EXPAND|wx.BOTTOM, border=5) # 添加回测参数布局
       vbox_sizer_a.Add(self.add_pick_para_lay()  , proportion=0, flag=wx.EXPAND|wx.BOTTOM, border=5) # 添加回测参数布局
       vbox_sizer_a.Add(self.add_download_para_lay(), proportion=0, flag=wx.EXPAND|wx.BOTTOM, border=5) # 添加下载参数布局
       vbox_sizer_a.Add(self.add_progress_bar(), proportion=0,flag=wx.EXPAND|wx.ALL, border=2)

       self.TextAInput = wx.TextCtrl(self.CtrlPanel, -1, "股票信息提示:", style = wx.TE_MULTILINE|wx.TE_READONLY)#多行|只读
       vbox_sizer_b = wx.BoxSizer(wx.VERTICAL)  # 纵向 box
       vbox_sizer_b.Add(self.add_buttons_lay(),proportion=0,flag=wx.EXPAND|wx.BOTTOM,border=2) #proportion 参数控制容器尺寸比例
       vbox_sizer_b.Add(self.TextAInput, proportion=1, flag=wx.EXPAND | wx.ALL, border=2)

       self.ParaPanel.SetSizer(vbox_sizer_a)
       self.CtrlPanel.SetSizer(vbox_sizer_b)

       # 第一层布局
       self.HBoxPanelSizer = wx.BoxSizer(wx.HORIZONTAL)
       self.HBoxPanelSizer.Add(self.ParaPanel,proportion = 1.5, border = 2,flag = wx.EXPAND|wx.ALL)
       self.HBoxPanelSizer.Add(self.DispPanel,proportion = 8, border = 2,flag = wx.EXPAND|wx.ALL )
       self.HBoxPanelSizer.Add(self.CtrlPanel,proportion = 1, border = 2,flag = wx.EXPAND|wx.ALL )
       self.SetSizer(self.HBoxPanelSizer)  # 使布局有效

       self.add_menu_bar()

   def add_stock_para_lay(self):
       # 行情参数
       stock_para_box = wx.StaticBox(self.ParaPanel, -1, u'行情参数')
       stock_para_sizer = wx.StaticBoxSizer(stock_para_box, wx.VERTICAL)

       # 行情参数——股票名称
       self.stock_name_list = ["浙大网新", "高鸿股份", "天威视讯", "北方导航"]
       self.stock_name_cbox = wx.ComboBox(self.ParaPanel, -1, "浙大网新", choices = self.stock_name_list,
                                          style = wx.CB_READONLY|wx.CB_DROPDOWN) #股票名称
       self.stock_name_text = wx.StaticText(self.ParaPanel, -1, u'股票名称')
       stock_para_sizer.Add(self.stock_name_text,proportion=0,flag=wx.EXPAND|wx.ALL,border=2)
       stock_para_sizer.Add(self.stock_name_cbox, 0, wx.EXPAND|wx.ALL|wx.CENTER, 2)

       # 行情参数——日历控件时间周期
       self.dpc_end_time = wx.adv.DatePickerCtrl(self.ParaPanel, -1,
                                                 style = wx.adv.DP_DROPDOWN|wx.adv.DP_SHOWCENTURY|wx.adv.DP_ALLOWNONE)#结束时间
       self.dpc_start_time = wx.adv.DatePickerCtrl(self.ParaPanel, -1,
                                                   style = wx.adv.DP_DROPDOWN|wx.adv.DP_SHOWCENTURY|wx.adv.DP_ALLOWNONE)#起始时间
       self.stock_data_text = wx.StaticText(self.ParaPanel, -1, u'日期(Start-End)')
       date_time_now = wx.DateTime.Now()  # wx.DateTime 格式"03/03/18 00:00:00"
       self.dpc_end_time.SetValue(date_time_now)
       self.dpc_start_time.SetValue(date_time_now.SetYear(date_time_now.year - 1))
       stock_para_sizer.Add(self.stock_data_text,proportion=0,flag=wx.EXPAND|wx.ALL,border=2)
       stock_para_sizer.Add(self.dpc_start_time, 0, wx.EXPAND|wx.ALL|wx.CENTER, 2)
       stock_para_sizer.Add(self.dpc_end_time, 0, wx.EXPAND|wx.ALL|wx.CENTER, 2)

       return stock_para_sizer

   def add_back_para_lay(self):

       # 回测参数
       back_para_box = wx.StaticBox(self.ParaPanel, -1, u'回测参数')
       back_para_sizer = wx.StaticBoxSizer(back_para_box, wx.VERTICAL)

       # 回测参数——策略选取
       self.strate_name_list = [u"双均线", u"阿尔法", u"布林带"]
       self.strate_name_cbox = wx.ComboBox(self.ParaPanel, -1, u"双均线", choices=self.strate_name_list,
                                           style=wx.CB_READONLY | wx.CB_DROPDOWN)  # 策略名称
       self.strate_name_text = wx.StaticText(self.ParaPanel, -1, u'策略名称')
       back_para_sizer.Add(self.strate_name_text,proportion=0,flag=wx.EXPAND|wx.ALL,border=2)
       back_para_sizer.Add(self.strate_name_cbox, 0, wx.EXPAND|wx.ALL|wx.CENTER, 2)

       # 回测参数——仓位策略
       self.position_name_list = [u"凯利公式", u"自定义 1", u"自定义 2"]
       self.position_name_cbox = wx.ComboBox(self.ParaPanel, -1, u"凯利公式", choices=self.position_name_list,
                                           style=wx.CB_READONLY | wx.CB_DROPDOWN)  # 策略名称
       self.position_name_text = wx.StaticText(self.ParaPanel, -1, u'仓位策略')
       back_para_sizer.Add(self.position_name_text,proportion=0,flag=wx.EXPAND|wx.ALL,border=2)
       back_para_sizer.Add(self.position_name_cbox, 0, wx.EXPAND|wx.ALL|wx.CENTER, 2)

       return back_para_sizer

   def add_pick_para_lay(self):

       # 选股参数
       pick_para_box = wx.StaticBox(self.ParaPanel, -1, u'选股参数')
       pick_para_sizer = wx.StaticBoxSizer(pick_para_box, wx.VERTICAL)

       # 选股参数——选股条件
       self.pick_name_list = [u"线性回归", u"自定义 1", u"自定义 2"]
       self.pick_name_cbox = wx.ComboBox(self.ParaPanel, -1, u"线性回归", choices=self.pick_name_list,
                                         style=wx.CB_READONLY | wx.CB_DROPDOWN)  # 选股条件
       self.pick_name_text = wx.StaticText(self.ParaPanel, -1, u'选股条件')
       pick_para_sizer.Add(self.pick_name_text,proportion=0,flag=wx.EXPAND|wx.ALL,border=2)
       pick_para_sizer.Add(self.pick_name_cbox, 0, wx.EXPAND|wx.ALL|wx.CENTER, 2)

       return pick_para_sizer

   def add_download_para_lay(self):

       # 下载参数
       download_para_box = wx.StaticBox(self.ParaPanel, -1, u'下载参数')
       download_para_sizer = wx.StaticBoxSizer(download_para_box, wx.VERTICAL)

       # 下载参数——股票池名称
       self.download_name_list = [u"人工智能", u"5G"]
       self.download_name_rbox = wx.RadioBox(self.ParaPanel, -1, label=u"", choices=self.download_name_list, majorDimension = 4, style = wx.RA_SPECIFY_ROWS)
       self.download_name_text = wx.StaticText(self.ParaPanel, -1, u'板块数据')
       download_para_sizer.Add(self.download_name_text, proportion=0, flag=wx.EXPAND | wx.ALL, border=2)
       download_para_sizer.Add(self.download_name_rbox, 0, wx.EXPAND | wx.ALL | wx.CENTER, 2)

       return download_para_sizer

   def add_buttons_lay(self):

       # 创建 FlexGridSizer 布局网格 vgap 定义垂直方向上行间距/hgap 定义水平方向上列间距
       FlexGridSizer=wx.FlexGridSizer(rows=2, cols=2, vgap=3, hgap=3)

       # 实盘按钮
       self.Firmoffer = wx.Button(self.CtrlPanel,-1,"行情")
       self.Firmoffer.Bind(wx.EVT_BUTTON, self.FirmEvent) # 绑定按钮事件
       # 下载按钮
       self.download = wx.Button(self.CtrlPanel,-1,"下载")
       self.download.Bind(wx.EVT_BUTTON, self.DownEvent)  # 绑定按钮事件
       # 选股按钮
       self.Stockpick = wx.Button(self.CtrlPanel,-1,"选股")
       # 回测按钮
       self.Backtrace = wx.Button(self.CtrlPanel,-1,"回测")

       # 加入 Sizer 中
       FlexGridSizer.Add(self.Firmoffer,proportion = 1, border = 5,flag = wx.ALL | wx.EXPAND)
       FlexGridSizer.Add(self.Stockpick,proportion = 1, border = 5,flag = wx.ALL | wx.EXPAND)
       FlexGridSizer.Add(self.Backtrace,proportion = 1, border = 5,flag = wx.ALL | wx.EXPAND)
       FlexGridSizer.Add(self.download, proportion=1, border=5, flag=wx.ALL | wx.EXPAND)
       FlexGridSizer.SetFlexibleDirection(wx.BOTH)

       return FlexGridSizer

   def add_progress_bar(self):
       self.count = 0
       self.gauge = wx.Gauge(self.ParaPanel, -1, range = 50)
       #self.gauge.SetBezelFace(1)
       #self.gauge.SetShadowWidth(1)
       self.Bind(wx.EVT_IDLE, self.GaugeEvent)
       return self.gauge

   def add_menu_bar(self):

       # 创建窗口面板
       menuBar = wx.MenuBar(style=wx.MB_DOCKABLE)
       toolmenu = wx.Menu()
       about = wx.MenuItem(toolmenu, wx.ID_ANY, '&关于量化小工具')
       # about.SetBitmap(wx.Bitmap("timy.png"))
       toolmenu.Append(about)
       toolmenu.AppendSeparator()
       toolmenu.Append(wx.ID_ANY, '&系统偏好设置')
       toolmenu.Append(wx.ID_ANY, '&服务偏好设置')
       toolmenu.AppendSeparator()
       toolmenu.Append(wx.ID_ANY, '&使用向导')
       menuBar.Append(toolmenu, '&小工具')
       fileMenu = wx.Menu()
       imp = wx.Menu()
       fileMenu.Append(wx.ID_NEW, "&新建工程\tCtrl+N")
       fileMenu.AppendSeparator()
       imp.Append(wx.ID_ANY, '导入自选股...')
       imp.Append(wx.ID_ANY, '导入策略...')
       imp.Append(wx.ID_ANY, '导入股票数据...')
       fileMenu.AppendSubMenu(imp, '&导入')
       fileMenu.AppendSeparator()
       fileMenu.Append(wx.ID_OPEN, '&打开工程\tCtrl+O')
       fileMenu.Append(wx.ID_SAVE, '&保存工程\tCtrl+S')
       fileMenu.AppendSeparator()

       qmi = wx.MenuItem(fileMenu, wx.ID_ANY, '&退出程序\tCtrl+W')
       self.Bind(wx.EVT_MENU, self.OnQuitEvent, qmi)
       fileMenu.Append(qmi)
       menuBar.Append(fileMenu, '&文件')
       self.SetMenuBar(menuBar)

   def ProcessPanelA(self):
       y_value = np.random.randn(200)
       x_value = np.arange(200)
       self.DispPanel.subplot.plot(x_value,y_value,label=u"随机误差",ls='-',c='r',lw=1)

   def ProcessPanelB(self):
       x_line=np.linspace(0,200,200)
       y_sin=np.sin(x_line)
       self.OptionPanel.subplot.plot(x_line,y_sin,label=u"sin",ls='dashed',c='k',lw=2)

   def FirmEvent(self, event):
       self.DispPanel.subplot.plot([1,2,3,4,5], [1,2,3,4,5], '#0f0ff0', linewidth=1.0)
       # 修改图形的任何属性后都必须更新 GUI 界面
       self.DispPanel.FigureCanvas.draw()

   def DownEvent(self, event):
       # 创建选项栏目面板
       self.OptionPanel = Panel_sw(self)
       # self.HBoxPanel.Add(self.OptionPanel,proportion = 1, border = 2,flag = wx.ALL | wx.EXPAND)
       # self.HBoxPanel.Remove(self.DispPanel)
       self.HBoxPanelSizer.Hide(self.DispPanel)
       self.HBoxPanelSizer.Replace(self.DispPanel, self.OptionPanel)
       self.SetSizer(self.HBoxPanelSizer)
       self.HBoxPanelSizer.Layout()
       self.ProcessPanelB()

   def OnQuitEvent(self, e):
       self.Close()

   def GaugeEvent(self, event):
       self.count = self.count + 1
       if self.count == 50:
           self.count = 0
       self.gauge.SetValue(self.count)


class App(wx.App):
   def OnInit(self):
       self.frame = Frame()
       self.frame.Show()
       self.frame.Center()
       self.frame.ProcessPanelA()
       self.SetTopWindow(self.frame)
       return True

if __name__ == '__main__':
   app = App()
   app.MainLoop()
