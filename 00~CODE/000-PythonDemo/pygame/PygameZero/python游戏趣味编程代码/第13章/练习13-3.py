from PIL import Image  # 导入图像处理库
w = 300 # 设定最终长图的宽度

# 打开要添加到上面的图片文件
im_up = Image.open("images\\up.jpg")
w_up, h_up = im_up.size  # 图像尺寸
h_up = h_up*w//w_up  # 调整后图像高度
im_up = im_up.resize((w, h_up))  # 调整大小

# 打开要添加到下面的图片文件
im_down = Image.open("images\\down.jpg")
# 调整图像大小，上下图片的高度需要一样，这样九宫格缩略图才能在中间
im_down = im_down.resize((w, h_up))  # 调整大小

# 打开九宫格图片之一，添加在长图中间
im_mid = Image.open("images\\image2.jpg")
w_mid, h_mid = im_mid.size  # 九宫格小图片尺寸
h_mid = h_mid*w//w_mid  # 调整后图像高度
im_mid = im_mid.resize((w, h_mid))  # 调整大小

# 新建图像，三张图上下拼成一张长图
newImage = Image.new('RGB', (w, h_up+h_mid+h_up), 'black')
newImage.paste(im_up, (0, 0))
newImage.paste(im_mid, (0, h_up))
newImage.paste(im_down, (0, h_up+h_mid))

# 保存新建图片
newImage.save('images\\newImage1.jpg')