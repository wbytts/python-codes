import xmlrpc.client as xmlrpclib
import pickle

metaweblog_url = "https://rpc.cnblogs.com/metaweblog/wbyixx"
appkey = "https://www.cnblogs.com/wbyixx"
username = "wbytts"
password = "wby.1415926"

server = xmlrpclib.ServerProxy(metaweblog_url)
blog_info = server.blogger.getUsersBlogs(appkey, username, password)

posts = server.metaWeblog.getRecentPosts("445714", username, password, 99999)

postid_list = []

for post in posts:
    postid_list.append(post['postid'])

with open('postid_list', 'wb') as f:
    pickle.dump(postid_list, f)

with open('posts', 'wb') as f:
    pickle.dump(posts, f)


