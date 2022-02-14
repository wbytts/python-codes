import pickle
import redis


class MyRedisClient(redis.Redis):
    """拓展Redis客户端的，增加一些其他的方法"""

    def __init__(self, host='127.0.0.1', port=6379, db=0, charset='utf8'):
        """初始化Redis客户端"""
        super().__init__(host=host, port=port, db=db, charset=charset)

    def pickle_set(self, key, value):
        """将value序列化为pickle字符串然后以key为键，字符串值的形式保存到Redis中"""
        pickle_obj_str = pickle.dumps(value)
        self.set(key, pickle_obj_str)
        # 写操作都进行一次快照操作，防止数据丢失
        self.bgsave()

    def pickle_get(self, key):
        """根据key值从Redis中获取保存的pickle字符串"""
        pickle_obj_str = self.get(key)
        value = pickle.loads(pickle_obj_str)
        return value


rc = MyRedisClient()
L = rc.pickle_get('apickle')
print(L)
