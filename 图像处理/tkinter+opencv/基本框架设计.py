import tkinter as tk
import cv2 as cv
from PIL import Image, ImageTk


def Showimage(imgCV_in, canva, layout="null"):
    """
    Showimage()是一个用于在tkinter的canvas控件中显示OpenCV图像的函数。
    使用前需要先导入库
    import cv2 as cv
    from PIL import Image,ImageTktkinter
    并注意由于响应函数的需要，本函数定义了一个全局变量 imgTK，请不要在其他地方使用这个变量名!
    参数：
    imgCV_in：待显示的OpenCV图像变量
    canva：用于显示的tkinter canvas画布变量
    layout：显示的格式。可选项为：
        "fill"：图像自动适应画布大小，并完全填充，可能会造成画面拉伸
        "fit"：根据画布大小，在不拉伸图像的情况下最大程度显示图像，可能会造成边缘空白
        给定其他参数或者不给参数将按原图像大小显示，可能会显示不全或者留空
    """
    global imgTK
    canvawidth = int(canva.winfo_reqwidth())
    canvaheight = int(canva.winfo_reqheight())
    sp = imgCV_in.shape
    cvheight = sp[0]  # height(rows) of image
    cvwidth = sp[1]  # width(colums) of image
    if (layout == "fill"):
        imgCV = cv.resize(imgCV_in, (canvawidth, canvaheight), interpolation=cv.INTER_AREA)
    elif (layout == "fit"):
        if (float(cvwidth / cvheight) > float(canvawidth / canvaheight)):
            imgCV = cv.resize(imgCV_in, (canvawidth, int(canvawidth * cvheight / cvwidth)), interpolation=cv.INTER_AREA)
        else:
            imgCV = cv.resize(imgCV_in, (int(canvaheight * cvwidth / cvheight), canvaheight),
                              interpolation=cv.INTER_AREA)
    else:
        imgCV = imgCV_in
    imgCV2 = cv.cvtColor(imgCV, cv.COLOR_BGR2RGBA)  # 转换颜色从BGR到RGBA
    current_image = Image.fromarray(imgCV2)  # 将图像转换成Image对象
    imgTK = ImageTk.PhotoImage(image=current_image)  # 将image对象转换为imageTK对象
    canva.create_image(0, 0, anchor=tk.NW, image=imgTK)


win = tk.Tk()
win.title('OpenCV + Tkinter 演示程序框架')



win.mainloop()