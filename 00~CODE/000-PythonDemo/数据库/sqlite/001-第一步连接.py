import sqlite3

# 数据库文件
db_file = 'd:/sqlites/test.db'

# 获取数据库连接
conn = sqlite3.connect(db_file)

# 编写SQL语句
sql = 'select * from user'

# 执行SQL语句
cur = conn.cursor()
cur.execute(sql)

# 查询结果
print(cur.fetchall())

# 关闭连接
conn.close()
