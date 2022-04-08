import redis

r = redis.Redis(host='127.0.0.1', port=6379)

r.set('name', '啦啦啦')
x = r.get('name')

print(x.decode('utf8'))
