import xmlrpc.client as xmlrpclib


metaweblog_url = "https://rpc.cnblogs.com/metaweblog/wbyixx"
appkey = "https://www.cnblogs.com/wbyixx"
username = "wbytts"
password = "wby.1415926"

server = xmlrpclib.ServerProxy(metaweblog_url)
#blog_info = server.blogger.getUsersBlogs(appkey, username, password)

post = server.metaWeblog.getPost("12129054", username, password)

print(post)