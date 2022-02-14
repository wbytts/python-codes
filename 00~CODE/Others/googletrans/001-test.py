import google_translate_util as gtu

# 获取用户输入的翻译内容
src = input('请输入你要翻译的内容:')

# 打印翻译结果的文本
print('翻译为英文的结果: ', end='')
print(gtu.google_trans(src))
