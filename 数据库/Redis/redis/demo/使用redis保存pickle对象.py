import pickle
import redis
R = redis.Redis(host='wang-bing-yi.redis.rds.aliyuncs.com', port=6379, username='wby', password='Bingyi@1314')

# arr = [1, 2, 3, 4, 5]
# r.set('arr', pickle.dumps(arr))

arr = pickle.loads(R.get('arr'))
print(type(arr))
print(arr)
