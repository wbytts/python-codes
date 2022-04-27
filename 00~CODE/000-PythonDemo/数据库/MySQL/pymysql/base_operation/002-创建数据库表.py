import pymysql

# 打开数据库连接
db = pymysql.connect(
    host="39.96.162.54",            # 主机
    user="root",                    # 用户名
    password="Bingyi@1314",              # 密码
    port=3306,                      # 端口
    database="demo",                # 数据库
    #unix_socket=None,
    charset="utf8")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute() 方法执行 SQL，如果表存在则删除
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# 使用预处理语句创建表
sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,
         SEX CHAR(1),
         INCOME FLOAT )"""

cursor.execute(sql)

# 关闭数据库连接
db.close()
