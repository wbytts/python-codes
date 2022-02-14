import json

'''
json序列化只支持部分Python数据结构：dict,list,tuple,str,int, float,True,False,None

和字符串有关的 都有 s
和文件有关的 没有 s

dumps(obj): 将对象转换（序列化）成字符串
loads(string): 将字符串转换（反序列化）成对象

json.dump(对象，文件句柄): 将对象转换（序列化）成字符串写入文件；
json.load(文件句柄): 将文件的字符串读取转换（反序列化）成对象。
'''

data = '[{"k1":"v1"},{"k2":"v2"}]'
list_data = json.loads(data)
print(list_data)

dd = {
    'name': 'wby',
    'age': 24,
    'sex': '男子'
}

print(json.dumps(dd))

# json.dump(list_data, open("list.json", "w"))
