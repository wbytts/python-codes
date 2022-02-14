# SQLAlchemy
# 核心
from sqlalchemy import create_engine, MetaData
from sqlalchemy import Table, Column
# 列类型
from sqlalchemy import Integer, Numeric, String, DateTime
# 约束、键
from sqlalchemy import PrimaryKeyConstraint, UniqueConstraint, CheckConstraint, ForeignKey
# sql
from sqlalchemy import sql
# 连接词
from sqlalchemy import and_, or_, not_
from sqlalchemy.ext.declarative import declarative_base
# other
from datetime import datetime


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


s = user.select().where(
    and_(
        user.c.username.like('%wang%'),
        user.c.password == 'asdfgh'
    )
)
rp = connection.execute(s)
print(rp.fetchall())


connection.close()
