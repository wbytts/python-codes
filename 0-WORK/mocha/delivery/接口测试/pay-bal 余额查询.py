import requests
import json

# 外卖后台服务地址
base_url = 'http://localhost:8080/delivery-api'

# 请求余额查询接口
params = {
    # 用户手机号
    'phone': '15052508052',
    # 餐厅ID（其实是canteenCode）
    'canteenId': 'SZ0001'
}
res = requests.post(base_url + '/pay/mochasoft-bal', json=params)

json_obj = json.loads(res.text)
# 增加缩进，美化json输出
print(json.dumps(json_obj, indent=2, ensure_ascii=False))
