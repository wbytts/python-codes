from utils.metaweblog_utils import *
from datetime import datetime

config = {
    'url': 'https://rpc.cnblogs.com/metaweblog/wbytts',
    'username': '1041493283@qq.com',
    'password': 'wby.1415926'
}



metaWeblog = MetaWeblog(config['url'], config['username'], config['password'])

new_post = Post(description="Hello~~~", title="test-metaweblog", dateCreated=datetime.now())
res = metaWeblog.new_post(new_post.get_struct())
print(res)

