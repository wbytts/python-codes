from MySQL.pymysql.pymysql_helper import MysqlHelper

db_tools = MysqlHelper(host='39.96.162.54', username='root', password='qweqwe', database='demo')

version = db_tools.get_db_version()
print('数据库的版本: {version}'.format(version=version[0]))

