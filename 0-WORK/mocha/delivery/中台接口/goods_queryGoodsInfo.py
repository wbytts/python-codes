import requests
from datetime import datetime
import hashlib
import uuid
import json
from userAuth import get_access_token

host = '223.68.131.168'
port = '18081'
img_url = 'http://183.207.195.123/platform/'
query_goods_url = 'http://' + host + ':' + port + '/api/canteen/goods/queryListGoodsInfo'

# print('ACCESS-TOKEN = ', access_token)


while True:
    print('-' * 100)
    canteen_num = 'SZ0001' # canteen_num = input('输入搜索的食堂编号:')
    goods_name = input('输入搜索的餐品名称:')
    headers = {
        'ACCESS-TOKEN': get_access_token(),
    }
    params = {
        'canteenNum': canteen_num,
        'goodsType': 'cp',
        'queryExts': None,
        'goodsName': goods_name
    }
    res = requests.post(query_goods_url, headers=headers, json=params)
    response = res.json()
    # print(json.dumps(response, indent=2, ensure_ascii=False))

    for good in response['data']['list']:
        print(good['goodsName'], end=", ")
    print()
