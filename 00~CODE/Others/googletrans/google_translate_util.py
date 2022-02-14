from googletrans import Translator

# 创建谷歌翻译客户端
translate = Translator()


def google_trans(src):
    try:
        # 请求谷歌翻译进行翻译
        result = translate.translate(src)
        # 等待返回结果
        while not result and not result.text and result.text != '':
            print('.', end='')
        print()
        return result.text
    except:  # 如果请求失败，则重新请求（递归）
        print('请求失败哦.', end='')
        return google_trans(src)
