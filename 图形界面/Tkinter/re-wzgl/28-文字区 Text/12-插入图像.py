"""
Text可以插入图像，插入的图像会被视为一个字符进行处理
所呈现的大小是图像的实际大小

插入的方法：
    from PIL import Image, ImageTk
    img = Image.open("...")
    img_tk = ImageTk.PhotoImage(img)
    text.image_create(tk.END, image=img_tk)
"""

