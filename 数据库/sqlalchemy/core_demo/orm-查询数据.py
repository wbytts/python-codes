from datetime import datetime
from sqlalchemy.engine import create_engine
from sqlalchemy.schema import MetaData
from sqlalchemy.sql.schema import Table, Column, ForeignKey, PrimaryKeyConstraint, UniqueConstraint, CheckConstraint
from sqlalchemy.sql.sqltypes import Integer, Numeric, String, DateTime
from sqlalchemy.sql.expression import select, insert, desc, cast
from sqlalchemy.sql.functions import func
from sqlalchemy.ext.declarative.api import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm.session import sessionmaker

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

# 查询所有数据
data = session.query(Book).all()
print(data)

# 将查询作为可迭代对象的时候，可以不调用all
for book in session.query(Book):
    print(book)


# 限制查询的列数
print(session.query(Book.name, Book.update_date).all())

# 排序
print(session.query(Book.name).order_by(Book.name).all()) # 升序
print(session.query(Book.name).order_by(desc(Book.name)).all()) # 降序
print(session.query(Book.name).order_by(Book.name.desc()).all()) # 降序

# 限制条数
print(session.query(Book.name).order_by(Book.name).limit(3).all()) # 升序

# 内置函数
print(session.query(func.sum(Book.id)).scalar())
print(session.query(func.count(Book.id)).scalar())

# 标签
res = session.query(func.count(Book.id).label('个数')).first()
print(res.keys())

# 过滤
# ==、!=、<、>、<=、>= 的功能和Python中一样
# 在与None比较的时候，== 运算符被重载为 IS NULL 语句
# 算术运算符可以用来对独立于数据库的字符串做连接处理
# SQL 中的 AND、OR、NOT，使用位运算符 &、|、~ 来表示 （注意 & 比 < 优先级高）
# 连接词：and_()、or_()、not_()
print(session.query(Book).filter(Book.name == 'Java编程思想').all()) # 判断列是否等于某个值
print(session.query(Book).filter_by(name='Java编程思想').all())
print(session.query(Book).filter(Book.name.like('%思想%')).all())  # 使用 ClauseElement 的方法
