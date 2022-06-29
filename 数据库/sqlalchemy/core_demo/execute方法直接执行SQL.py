from sqlalchemy import create_engine

# 创建一个 SQLAlchemy 引擎
engine = create_engine('mysql+pymysql://root:root@127.0.0.1:3306/demo', pool_recycle=3600)

# 打开数据库，得到一个数据库连接
connection = engine.connect()

rp = connection.execute('select * from user')
print(rp.fetchall())

# 关闭连接
connection.close()
