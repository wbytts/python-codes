from PIL import Image # 导入图像处理库

# 打开一个图像文件，注意是文件路径
im = Image.open('images\image1_crop.jpg')
w, h = im.size  # 获得图像文件尺寸
step = 250 # 小图片的宽、高均为250

for i in range(3):  # 对行循环
    for j in range(3):  # 对列循环
        box = (i*step, j*step, (i+1)*step, (j+1)*step)  # 利用box对图像进行剪裁
        index = j*3+i+1 # 裁剪出的小图像编号
        pic = im.crop(box) # 裁剪图像
        filename = "images\image_"+str(index)+".jpg" # 待保存的图像文件名
        pic.save(filename) # 保存裁剪好的小图像