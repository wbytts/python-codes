
# C:\Users\wbytts\AppData\Local\
import json
import getpass
import pickle

username = getpass.getuser()
bms_path = f"C:\\Users\\{username}\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default\\Bookmarks"
print(bms_path)

# 将json文件的内容加载为字典对象
f = open(bms_path, encoding='utf8')
bmp_json = json.load(f)
f.close()

# print(bmp_json)
pickle.dump(bmp_json, open(r'00~CODE\Chrome书签解析\bmp_json.pickle', 'wb'))

# 获取书签栏
bookmark_bar = bmp_json['roots']['bookmark_bar']
# 其他书签
bookmark_other = bmp_json['roots']['other']

'''
child的属性说明：
    children: 如果type是folder，则会有这个属性
    date_added: 添加日期
    date_modified: 修改日期
    guid: 唯一标识
    id: 编号
    name: 名称
    type: py类型检查
    url: 如果是网址，则会有这个属性，标识书签的地址
'''

out_file = open('bookmark_list', 'w', encoding='utf8')

def iter_bmp(obj):
    for item in obj:
        if item.get('type') == 'url':
            print(item['name'], file=out_file)
            print(item['url'], file=out_file)
            item['name'] += '?'
            print('-' * 100, file=out_file)
        elif item.get('type') == 'folder':
            iter_bmp(item['children'])


iter_bmp(bookmark_bar['children'])


