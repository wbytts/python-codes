from datetime import datetime
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column
from sqlalchemy import Integer, Numeric, String, DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import PrimaryKeyConstraint, UniqueConstraint, CheckConstraint
from sqlalchemy import insert
from sqlalchemy.sql import select
from sqlalchemy import desc

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

'''
Table 对象的 select 方法，构造查询SQL语句
也可以使用：from sqlalchemy.sql import select
select([user])
'''
from sqlalchemy.sql import select
s = select([user])
rp = connection.execute(s)
print('select结果条数:', rp.rowcount)
print(rp.fetchall())

s = user.select()
rp = connection.execute(s)
print('结果条数:', rp.rowcount)
print(rp.fetchall())

# 限制查询的列
print("限制查询的列")
s = select([user.c.username])
rp = connection.execute(s)
print(rp.keys())
print(rp.first())


# 排序
s = user.select().order_by(user.c.username)
rp = connection.execute(s)
print(rp.fetchall())
# 倒序排序（默认的升序也有一个对应的 asc 函数）
s = user.select().order_by(desc(user.c.username))
rp = connection.execute(s)
print(rp.fetchall())

# 限制返回的结果条数 linit(n)
s = user.select().order_by(user.c.username).limit(3)
rp = connection.execute(s)
print(rp.fetchall())
print('列名:', rp.keys())


# 关闭连接
connection.close()
