from MyQR import myqr  # 导入二维码生成库
# 根据字符串、背景图片，生成个性化二维码
myqr.run(words='https://www.epubit.com/',
         picture='images\\image2.jpg', colorized=True)
