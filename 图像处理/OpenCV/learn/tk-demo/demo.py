import tkinter as tk
from tkinter import Tk
import cv2 as cv

root = Tk()
root.title('opencv 基本操作')


def read_image():
    img = cv.imread('f:/images/reba.jpg')
    cv.imshow('img', img)
    cv.waitKey(0)
    cv.destroyAllWindows()


read_image_btn = tk.Button(root, text='读取图片', command=read_image)
read_image_btn.pack()

root.mainloop()
