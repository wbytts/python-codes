import redis

r = redis.Redis(host='wang-bing-yi.redis.rds.aliyuncs.com', port=6379, username='wby', password='Bingyi@1314')
r.set('name', 'wangby')
print(r.get('name'))


