from PIL import Image  # 导入图像处理库
# 新建图像
newImage = Image.new('RGB', (800, 800), 'red')
# 保存新建图片
newImage.save('images\\newImage.jpg')