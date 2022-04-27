import pymysql

# 打开数据库连接
db = pymysql.connect("39.96.162.54", "root", "qweqwe", "demo")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 插入语句
sql = "insert into tg (id, text) values (2, 'qwe')"
try:
    # 执行sql语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
except:
    # 如果发生错误则回滚
    db.rollback()

# 关闭数据库连接
db.close()
