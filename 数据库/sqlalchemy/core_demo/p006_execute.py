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

'''
execute() 方法：
    使用传入的语句和其他参数，通过适当的数据库方言的编辑器编译语句
    编译器通过遍历树状结构构建一个普通的参数化SQL语句，而后该语句被返回给execute方法，
    execute再通过调用该方法的连接把SQL语句发送到数据库，然后数据库执行语句并返回操作结果
'''

ins = user.insert()
result = connection.execute(
    ins,  # SQL语句，下面是对应的参数
    username="zhangsan",
    password="333333"
)

# 关闭连接
connection.close()
