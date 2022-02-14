import redis

R = redis.Redis(host='127.0.0.1', port=6379)

R.delete('OrderCacheKeySZ0001202108191533120005')
