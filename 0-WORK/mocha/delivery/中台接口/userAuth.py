import requests
from datetime import datetime
import hashlib
import uuid
import json

def get_access_token():
    host = '223.68.131.168'
    port = '18081'
    key = 'b2bTestMd5Key'
    img_url = 'http://183.207.195.123/platform/'
    auth_url = 'http://' + host + ':' + port + '/api/sso/userAuth'

    # 获取中台鉴权
    params = {
        'uid': str(uuid.uuid4()).replace('-', ''),
        'platformId': 'canteen',
        'userId': 'admin',
        'canteenNum': 'SZ0001',
    }

    sign_str = params['uid'] + "canteen" + params['userId'] + params['canteenNum'] + datetime.now().strftime('%Y%m%d') + key
    sign_md5_str = hashlib.md5(sign_str.encode()).hexdigest()
    params['sign'] = sign_md5_str
    res = requests.post(auth_url, json=params)
    response_json = res.json()
    # print(json.dumps(response_json, indent=2, ensure_ascii=False))
    with open('accessToken', 'w') as f:
        f.write(response_json['data']['accessToken'])
    with open('refreshToken', 'w') as f:
        f.write(response_json['data']['refreshToken'])

    return response_json['data']['accessToken']
