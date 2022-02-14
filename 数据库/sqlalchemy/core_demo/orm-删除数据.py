from datetime import datetime
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column
from sqlalchemy import Integer, Numeric, String, DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import PrimaryKeyConstraint, UniqueConstraint, CheckConstraint
from sqlalchemy.sql import select, insert, desc
from sqlalchemy import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm import sessionmaker
from sqlalchemy import cast

engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/demo', echo=False, pool_recycle=3600)
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

    def __repr__(self):
        return f'《{self.name}》--- {self.author}'


# 模型的持久化
Base.metadata.create_all(engine)




session.commit()
