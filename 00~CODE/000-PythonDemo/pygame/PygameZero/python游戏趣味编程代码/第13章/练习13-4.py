from PIL import Image  # 导入图像处理库
# 新建图像，设置宽高，初始化为黑色
im = Image.new('RGB', (580, 460), (0, 0, 0))
px = im.load()  # 导入图片像素

# 假设黑色方块高100，白色长条高20，交替出现
# 对横坐标而言，i取余120，余数范围在100-119之间的是白色，其他为黑色
# 纵坐标对j同样处理填色
for i in range(580):
    for j in range(460):
        x = i % 120
        y = j % 120 
        if 100 <= x <= 119 or 100 <= y <= 119:
            px[i, j] = 255, 255, 255  # 将像素设为白色

im.save('images\\跳动的点.jpg')