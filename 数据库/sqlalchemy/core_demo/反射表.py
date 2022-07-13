
from sqlalchemy import create_engine, MetaData
from sqlalchemy import Table
from sqlalchemy import select


engine = create_engine('mysql+pymysql://root:root@127.0.0.1:3306/demo', echo=False, pool_recycle=3600)
metadata = MetaData()

# 反射
# autoload 和 autoload_with 两个参数，会把模式信息反射到 metadata对象中
# 并在返回中保存对表对象的引用
user = Table('user', metadata, autoload=True, autoload_with=engine)

"""
注意：
    反射单表的时候，外键默认不会被反射（因为外键涉及两个表）
    为了不让外键处于半断状态，SQLAlchemy放弃了单向关系
    可以反射后再手动添加
"""

# connection = engine.connect()

s = select([user])
data = engine.execute(s).fetchall()
print(data)

print(metadata.tables['user'])

