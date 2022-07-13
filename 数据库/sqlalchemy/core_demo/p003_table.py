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
engine = create_engine('mysql+pymysql://root:root@127.0.0.1:3306/demo', echo=True, pool_recycle=3600)

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

# 关闭连接
connection.close()
