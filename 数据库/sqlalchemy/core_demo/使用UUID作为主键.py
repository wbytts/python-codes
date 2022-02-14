from datetime import datetime
from sqlalchemy import create_engine, MetaData
from sqlalchemy import Column
from sqlalchemy import String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import uuid

engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/demo', echo=True, pool_recycle=3600)
connection = engine.connect()
metadata = MetaData()
Base = declarative_base()

# 创建会话
Session = sessionmaker(bind=engine)
session = Session()


class Book(Base):
    __tablename__ = 'book_uuid'
    __table_args__ = (  )  # 约束

    id = Column(String(32), primary_key=True, default=lambda: uuid.uuid4().hex)
    name = Column(String(255))
    author = Column(String(255))

    create_date = Column(DateTime(), default=datetime.now)
    update_date = Column(DateTime(), default=datetime.now, onupdate=datetime.now)


# 模型的持久化
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# 插入数据
book = Book(name='Java编程思想', author='大佬1')
session.add(book)

# 也可以一次性插入多条
b1 = Book(name='asdasd', author='大佬2')
b2 = Book(name='qweqweqwe', author='大佬3')
session.bulk_save_objects([b1, b2])

session.commit()
