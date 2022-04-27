from PIL import Image  # 导入图像处理库
# 打开头像图片文件
pic = Image.open("images\image1.jpg")
w_pic, h_pic = pic.size  # 获得图像文件尺寸
px = pic.load()  # 导入图片像素

num = 10 # 小方格的长宽
for i in range(w_pic):
    for j in range(h_pic):
        # 每个格子内取一个代表像素
        I = i - (i%num)/2
        J = j - (j%num)/2
        # 格子内所有像素的颜色都设为代表像素的颜色
        px[i, j] = px[I, J]

for i in range(w_pic):
    for j in range(h_pic):
        # 每个小格子间加一条白色线
        if i % num == 0 or j % num == 0:
            px[i, j] = 255, 255, 255

pic.save('images\\image1_像素化.jpg')