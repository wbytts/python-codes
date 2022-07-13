from sqlalchemy import create_engine, MetaData
from sqlalchemy import Table
from sqlalchemy import select
import sqlacodegen

# engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/ry', echo=False, pool_recycle=3600)
# 操作Oracle的话需要安装 cx_Oracle
engine = create_engine("oracle://admduty:admduty@172.23.22.101:1521/orcl", encoding='utf-8', echo=True)
metadata = MetaData()

"""
sqlalchemy根据表名来反射表
注：区分表名的大小写，在某些数据库中可能会发生错误
"""

# 反射整个数据库
metadata.reflect(bind=engine)

# 获得数据库中的所有表的表名（表名是否区分大小写，具体的数据库不一样）
table_name_list = metadata.tables.keys()
print(table_name_list)

# s = select([metadata.tables['sys_menu']])
# data = engine.execute(s).fetchall()
# for d in data:
#     print(d)
