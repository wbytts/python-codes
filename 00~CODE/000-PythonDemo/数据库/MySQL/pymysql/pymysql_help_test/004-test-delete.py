from MySQL.pymysql.pymysql_helper import MysqlHelper

db_tools = MysqlHelper(host='39.96.162.54', username='root', password='qweqwe', database='demo')

# 注意，如果变动的数据就是数据库的数据的话，是不会影响数据库的，受影响的行数会返回0
res = db_tools.update('delete from user where id=%s', [1234])
print(res)
