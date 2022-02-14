import tkinter, win32api, win32con, pywintypes


def get_replicate_text(text):
    i, space, str1, str2 = 0, 20, "", ""
    while (i <= 40):
        str1 = str1 + text + " " * space
        i = i + 1
    str2 = " " * space + str1 + "\n\n"
    str1 = str1 + "\n"
    str1 = (str1 + str2) * 40
    return str1


mytext = get_replicate_text('水印没啦')
root = tkinter.Tk()
width = win32api.GetSystemMetrics(0)
height = win32api.GetSystemMetrics(1)
root.overrideredirect(True)  # 隐藏显示框
root.geometry("+0+0")  # 设置窗口位置或大小
root.lift()  # 置顶层
root.wm_attributes("-topmost", True)  # 始终置顶层
root.wm_attributes("-disabled", True)
root.wm_attributes("-transparentcolor", "white")  # 白色背景透明
hWindow = pywintypes.HANDLE(int(root.frame(), 16))
exStyle = win32con.WS_EX_COMPOSITED | win32con.WS_EX_LAYERED | win32con.WS_EX_NOACTIVATE | win32con.WS_EX_TOPMOST | win32con.WS_EX_TRANSPARENT
win32api.SetWindowLong(hWindow, win32con.GWL_EXSTYLE, exStyle)
label = tkinter.Label(text=mytext, compound='left', font=('Times New Roman', '15'), fg='#dfdfdf', bg='white')
label.pack()  # 显示
root.mainloop()  # 循环
