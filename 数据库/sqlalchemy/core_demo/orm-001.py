from datetime import datetime
from sqlalchemy import create_engine, MetaData
from sqlalchemy import Table, Column
from sqlalchemy import Integer, Numeric, String, DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import PrimaryKeyConstraint, UniqueConstraint, CheckConstraint
from sqlalchemy.sql import select, insert
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/demo', echo=True, pool_recycle=3600)
connection = engine.connect()
metadata = MetaData()
Base = declarative_base()

# 创建会话
Session = sessionmaker(bind=engine)
session = Session()

class Book(Base):
    __tablename__ = 'book'
    __table_args__ = (  )  # 约束

    id = Column(Integer(), primary_key=True)
    name = Column(String(255))
    author = Column(String(255))

    create_date = Column(DateTime(), default=datetime.now)
    update_date = Column(DateTime(), default=datetime.now, onupdate=datetime.now)


# 模型的持久化
Base.metadata.create_all(engine)

# 插入数据
book = Book(name='Java编程思想', author='大佬')
session.add(book)

# 也可以一次性插入多条
"""
这种虽然速度会快一些，但是是以牺牲了正常添加和提交中可以使用的一些特性为代价的：
* 关系设置和操作得不到遵守或触发
* 对象没有连接到会话
* 默认情况下，不获取主键
* 不会触发任何事件
"""
b1 = Book(name='asdasd', author='大佬')
b2 = Book(name='qweqweqwe', author='大佬')
session.bulk_save_objects([b1, b2])


# flush 与 commit 相似，但是 flush 不会执行数据库提交并结束事务
# session.flush()

session.commit()
