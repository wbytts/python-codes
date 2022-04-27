from PIL import Image  # 导入图像处理库

# 新建图像
newImage = Image.new('RGB', (400, 400), 'red')
# 打开Python标志图片文件，大小为80*80
py = Image.open("images\python.jpg") 

# 生成用Python图标平铺的图片
for i in range(5):
    for j in range(5):
        newImage.paste(py, (i*80, j*80))

# 保存新建图片
newImage.save('images\\newImage.jpg')