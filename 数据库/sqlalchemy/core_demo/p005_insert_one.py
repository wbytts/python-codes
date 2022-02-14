from datetime import datetime
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column
from sqlalchemy import Integer, Numeric, String, DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import PrimaryKeyConstraint, UniqueConstraint, CheckConstraint
from sqlalchemy import insert
from sqlalchemy.sql import select

# 创建一个 SQLAlchemy 引擎
engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/demo', echo=False, pool_recycle=3600)

# 打开数据库，得到一个数据库连接
connection = engine.connect()

# 元数据 MetaData
metadata = MetaData()

# 定义一个用户表
user = Table('user', metadata,
             Column('id', Integer(), primary_key=True),
             Column('username', String(20), nullable=False),
             Column('password', String(100), nullable=False)
             )
# 创建所有表
metadata.create_all(engine)

# 插入数据1：使用Table对象的 insert 方法生成sql语句
print(user.insert())
s = user.insert().values(username="wangby", password="123456")
print('要执行的SQL --> ' + str(s))
print('实际传递的参数 --> ' + str(s.compile().params))
rp = connection.execute(s)
# 获取插入完成后的主键
print('插入成功的主键 --> ' + str(rp.inserted_primary_key))

# 插入数据2：使用 insert方法
s = insert(user).values(username="wangby111", password="123456qwe")
print('要执行的SQL --> ' + str(s))
print('实际传递的参数 --> ' + str(s.compile().params))
rp = connection.execute(s)
print('插入成功的主键 --> ' + str(rp.inserted_primary_key))

# 关闭连接
connection.close()
