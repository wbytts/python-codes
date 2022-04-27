from PIL import Image  # 导入图像处理库

# 打开头像图片文件
pic = Image.open("images\image2.jpg")
w_pic, h_pic = pic.size  # 获得图像文件尺寸
# 拷贝一份原始图片，在其上进行修改
copyPic = pic.copy()

# 打开Python标志图片文件
py = Image.open("images\python.jpg")
w_py, h_py = py.size  # 获得图像文件尺寸

# 将py图片复制粘贴到copyPic图片的右下角
copyPic.paste(py, (w_pic-w_py, h_pic-h_py))

# 保存更改后的copyPic图片
copyPic.save("images\image2_python.jpg")