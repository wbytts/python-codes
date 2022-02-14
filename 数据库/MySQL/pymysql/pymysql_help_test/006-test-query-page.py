from Databases.MySQL.pymysql.pymysql_helper import MysqlHelper

db_tools = MysqlHelper(host='39.96.162.54', username='root', password='Bingyi@1314', database='demo')

# 注意，如果变动的数据就是数据库的数据的话，是不会影响数据库的，受影响的行数会返回0
res = db_tools.query_page('select * from user', current_page=1, page_size=2)
print(res)
