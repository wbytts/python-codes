
from sqlalchemy import create_engine, MetaData
from sqlalchemy import Table
from sqlalchemy import select


engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/ry', echo=False, pool_recycle=3600)
metadata = MetaData()

# 反射
sys_user = Table('sys_user', metadata, autoload=True, autoload_with=engine)

# connection = engine.connect()

s = select([sys_user])
data = engine.execute(s).fetchall()
print(data)

print(metadata.tables['sys_user'])

