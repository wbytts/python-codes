"""
使用函数cv2.imread()来打开图片，图片要么在当前工作目录，要么是全路径。

第二个参数是一个标志位，用来指定打开的方式。

·cv2.IMREAD_COLOR:加载一个彩色图片。图片的透明度会被忽略，这个是默认标志
·cv2.IMREAD_GRAYSCALE:用灰度模式加载图片
·cv2.IMREAD_UNCHANGED:包含alpha通道的方式加载图片

除了这三种标志外，也可以传对应的整数参数1,0,或者-1

        import cv2

        # Load an color image in grayscale
        img = cv2.imread('messi5.jpg', 0)

!!!!!! 即便图片路径是错的，也不会报错，但是print img会给你None

======

使用函数cv2.imshow() 来在窗口里显示图片，窗口自动适配图片大小。

第一个参数是窗口名称，是字符串。第二个参数是我们的图片，你想创建多少窗口都可以，但是得给不同的窗口不同的名字。

        cv2.imshow('image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

======

cv2.waitKey()是一个键盘绑定函数。
它的参数是毫秒数，这个函数会等待任意键盘事件指定的毫秒时间。
如果你点了任意键，这个程序继续。如果传入0，它会一直等待按键。
它也可以设置成检测指定键，比如如果a被按了

如果你使用64位的机器，你需要把k = cv2.waitKey(0) 这行换成： k = cv2.waitKey(0) & 0xFF

======

cv2.destroyAllWindows()销毁所有的我们创建的窗口，如果你想销毁指定的窗口，
使用函数cv2.destroyWindow()你可以传指定窗口的名字作为参数。

    cv2.namedWindow('image',cv2.WINDOW_NORMAL)
    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

======

使用函数cv2.imwrite()来写入图片。

第一个参数是文件名，第二个参数是你要保存的图片。这会在工作目录存一个png格式的图片

    cv2.imwrite('messigray.png', img)

======

有种特殊情况你可以先创建窗口，再把图片加载到里面。
在这种情况下，你可以指定窗口是否可以改变大小。
这是通过函数cv2.namedWindow()完成的。
默认情况下，标志位是cv2.WINDOW_AUTOSIZE。
但是如果你指定标志位为cv2.WINDOW_NORMAL，你可以改变窗口大小。
她可以在图片太大的时候在窗口上加上滚动条。
    cv2.namedWindow('image',cv2.WINDOW_NORMAL)
    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


"""
