"""
如果你想要在图片周围生成边框，类似于相框，你可以使用cv2.copyMakeBorder()函数。但是它还能用于卷积，0内边距等。这个函数有下面这些参数：

·src - 输入图片
·top, bottom, left, right - 各个方向的边框像素宽度
·borderType - 标志位，定义要加什么样的边框，可以是下列类型：
        ·cv2.BORDER_CONSTANT - 添加固定的彩色边。值需要在后面的参数提供。
        ·cv2.BORDER_REFLECT - 边框是镜像的，像这样：fedcba/abcdefgh/hgfedcb
        ·cv2.BORDER_REFLECT_101或cv2.BORDER_DEFAULT - 和上面一样，但是有点变化，像这样：gfedcb/abcdefgh/gfedcba
        ·cv2.BORDER_REPLICATE - 最后的元素是重复的，像这样：aaaaaa/abcdefgh/hhhhhhh
        ·cv2.BORDER_WRAP - 没法解释，看上去是这样: cdefgh/abcdefgh/abcdefg

·value - 如果边的类型是cv2.BORDER_CONSTANT 这个值就是边的颜色。

"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

BLUE = [255, 0, 0]

img1 = cv2.imread('../images/opencv_logo.png')

replicate = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_WRAP)
constant = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=BLUE)

plt.subplot(231), plt.imshow(img1, 'gray'), plt.title('ORIGINAL')
plt.subplot(232), plt.imshow(replicate, 'gray'), plt.title('REPLICATE')
plt.subplot(233), plt.imshow(reflect, 'gray'), plt.title('REFLECT')
plt.subplot(234), plt.imshow(reflect101, 'gray'), plt.title('REFLECT_101')
plt.subplot(235), plt.imshow(wrap, 'gray'), plt.title('WRAP')
plt.subplot(236), plt.imshow(constant, 'gray'), plt.title('CONSTANT')

plt.show()
