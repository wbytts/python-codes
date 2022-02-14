from datetime import datetime
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column
from sqlalchemy import Integer, Numeric, String, DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import PrimaryKeyConstraint, UniqueConstraint, CheckConstraint
from sqlalchemy import insert
from sqlalchemy.sql import select
from sqlalchemy import and_, or_, not_

# 创建一个 SQLAlchemy 引擎
engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/demo', echo=True, pool_recycle=3600)

# 打开数据库，得到一个数据库连接
connection = engine.connect()

# 元数据 MetaData
metadata = MetaData()


# 构建表模型
cookies = Table('cookies', metadata,
                Column('cookie_id', Integer(), primary_key=True),
                Column('cookie_name', String(50), index=True),
                Column('cookie_recipe_url', String(255)),
                Column('cookie_sku', String(55)),
                Column('quantity', Integer()),
                Column('unit_cost', Numeric(12, 2))
                )

users = Table('users', metadata,
              Column('user_id', Integer(), primary_key=True),
              Column('username', String(15), nullable=False, unique=True),
              Column('email_address', String(255), nullable=False),
              Column('phone', String(20), nullable=False),
              Column('password', String(25), nullable=False),
              Column('created_on', DateTime(), default=datetime.now),
              Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now)
              )

# 表的持久化
metadata.create_all(engine)

# 插入数据
ins = cookies.insert().values(
    cookie_name="chocolate chip",
    cookie_recipe_url="http://some.aweso.me/cookie/recipe.html",
    cookie_sku="CC01",
    quantity="12",
    unit_cost="0.50"
)
# 展示实际要执行的SQL语句我们提供的值，会被替换进去 :xxx
print('要执行的SQL语句 --> ' + str(ins))
# ins 的 compile() 方法返回一个 SQLCompiler对象，我们可以通过其 params 属性访问随查询一起发送的实际参数
print('实际传递的参数 --> ' + str(ins.compile().params))
# 使用 connection 的 execute() 方法把语句发送到数据库，数据库就会执行语句，并把记录插入到表中
result = connection.execute(ins)
# 可以通过 result 的 inserted_primary_key 属性获得刚才插入的记录的ID
print('数据插入成功 ID --> ' + str(result.inserted_primary_key))

# 独立使用 insert
ins = insert(cookies).values(
    cookie_name="chocolate chip",
    cookie_recipe_url="http://some.aweso.me/cookie/recipe.html",
    cookie_sku="CC01",
    quantity="12",
    unit_cost="0.50"
)


# execute() 方法，语句+参数
ins = cookies.insert()
result = connection.execute(
    ins,
    cookie_name="chocolate chip",
    cookie_recipe_url="http://some.aweso.me/cookie/recipe.html",
    cookie_sku="CC01",
    quantity="12",
    unit_cost="0.50"
)


s = select([cookies])
rp = connection.execute(s)
results = rp.fetchall()

for r in results:
    print(r)

# 或者使用 Table 对象的 select 方法
s = cookies.select()
rp = connection.execute(s)
results = rp.fetchall()

print('-' * 100)
for r in results:
    print(r)

# 关闭连接
connection.close()



