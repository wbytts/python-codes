import requests
import json

# 外卖后台服务地址
base_url = 'http://localhost:8080/delivery-api'


params = {
    # # 用户手机号
    # 'phone': '15052508051',
    # # 餐厅ID（其实是canteenCode）
    # 'canteenId': 'SZ0001',
    # 订单编号 SZ0001202104272058540006 (最后一位 1~目前的6)
    'orderCode': 'SZ0001202104281824320001',
    # 订单总价（单位 分）
    # 'totalOrderPrice': 0.01,
}
res = requests.post(base_url + '/pay/mochasoft-refund', json=params)

json_obj = json.loads(res.text)
#json_obj['data'] = json.loads(json_obj['data'])
# 增加缩进，美化json输出
print(json.dumps(json_obj, indent=4, ensure_ascii=False))
