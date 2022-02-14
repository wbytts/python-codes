from Databases.MySQL.pymysql.pymysql_helper import MysqlHelper

db_tools = MysqlHelper(host='39.96.162.54',
                       username='root',
                       password='qweqwe',
                       database='demo')

res = db_tools.insert('insert into user (id, name, pwd) value (%s, %s, %s)',
                      [1234, 'wbywby', 'qweqwe'])
print(res)
