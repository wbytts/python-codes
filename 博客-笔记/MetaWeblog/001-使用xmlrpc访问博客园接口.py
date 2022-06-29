from utils.metaweblog_utils import *
from datetime import datetime
import time

config = {
    'url': 'https://rpc.cnblogs.com/metaweblog/wbyixx',
    'username': 'wbytts',
    'password': 'wby.1415926'
}



metaWeblog = MetaWeblog(config['url'], config['username'], config['password'])
blogs = metaWeblog.get_recent_posts(1000, '11832613')
# print(blogs[0])

text = """> FLowUs邀请链接：https://flowus.cn/login?code=AXNU63
> FlowUs邀请码：AXNU63
---
"""

for blog in blogs:
    if len(blog['title']) >= 150: continue
    blog['description'] = blog['description'].replace(text, "")
    blog['description'] = text + blog['description']
    metaWeblog.edit_post(blog['postid'], blog, publish=True)
    print(f" 更新成功#\t{blog['title']}")
    # time.sleep(30)


# new_post = Post(description="Hello~~~", title="test-metaweblog", dateCreated=datetime.now())
# res = metaWeblog.new_post(new_post.get_struct())
# print(res)

