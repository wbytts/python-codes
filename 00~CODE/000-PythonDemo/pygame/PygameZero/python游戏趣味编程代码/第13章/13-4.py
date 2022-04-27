from PIL import Image  # 导入图像处理库
# 新建图像，宽高都为800，初始化为白色
im = Image.new('RGB', (800, 800), (255, 255, 255))
px = im.load()  # 导入图片像素

for i in range(800):
    for j in range(800):
        if (i//80 + j//80) %2==1:
            px[i,j] = 0,0,0 # 将像素设为黑色

im.save('images\\国际象棋棋盘.jpg')
