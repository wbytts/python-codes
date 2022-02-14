import pymysql

# 获取数据库连接
db = pymysql.connect(
    host="39.96.162.54",            # 主机
    user="root",                    # 用户名
    password="Bingyi@1314",              # 密码
    port=3306,                      # 端口
    database="demo",                # 数据库
    #unix_socket=None,
    charset="utf8",                # 编码
    # sql_mode=None,
    # read_default_file=None,
    # conv=None,
    # use_unicode=None,
    # client_flag=0,
    # cursorclass=pymysql.cursors.Cursor,
    # init_command=None,
    # connect_timeout=10,
    # ssl=None,
    # read_default_group=None,
    # compress=None,
    # named_pipe=None,
    # autocommit=False,
    # db=None,
    # passwd=None,
    # local_infile=False,
    # max_allowed_packet=16*1024*1024,
    # defer_connect=False,
    # auth_plugin_map=None,
    # read_timeout=None,
    # write_timeout=None,
    # bind_address=None,
    # binary_prefix=False,
    # program_name=None,
    # server_public_key=None
)

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()

print("Database version : %s " % data)

# 关闭 cursor
cursor.close()
# 关闭数据库连接
db.close()
