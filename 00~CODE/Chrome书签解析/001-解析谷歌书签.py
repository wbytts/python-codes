import json
import getpass
import pickle

username = getpass.getuser()
# Chrome浏览器会把书签的内容保存在这个文件里面（json的形式）。
# 每台电脑的路径有区别，主要是用户名不一样
bms_path = f"C:\\Users\\{username}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Bookmarks"
print(bms_path)

# 将json文件的内容加载为字典对象
f = open(bms_path, encoding='utf8')
bmp_json = json.load(f)
f.close()

# print(bmp_json)
pickle.dump(bmp_json, open(r'./chrome-bookmark.pickle', 'wb'))

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

def iter_bmp(obj):
    """
    递归遍历书签信息
    """
    for item in obj:
        if item.get('type') == 'url':
            print(item['name'])
            print(item['url'])
            item['name'] += '?'
            print('-' * 100)
        elif item.get('type') == 'folder':
            iter_bmp(item['children'])


iter_bmp(bookmark_bar['children'])


