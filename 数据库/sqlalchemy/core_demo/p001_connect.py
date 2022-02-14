from sqlalchemy import create_engine

# 创建一个 SQLAlchemy 引擎
engine = create_engine('mysql+pymysql://root:123qwe@127.0.0.1:3306/demo', echo=True, pool_recycle=3600)

# 打开数据库，得到一个数据库连接
connection = engine.connect()


# 关闭连接
connection.close()
