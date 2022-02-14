"""
pip install pymysql
"""
import pymysql


class MysqlHelper(object):
    """
    PyMySQL 工具类
    """

    def __init__(self, host: str, username: str, password: str, database: str, port: int = 3306, charset: str = 'utf8'):
        """
        初始化数据库配置信息
        """
        self.host = host
        self.username = username
        self.password = password
        self.database = database
        self.port = port
        self.charset = charset

    def open_connection(self):
        """
        获取数据库连接
        """
        # 获取数据库的连接
        self.conn = pymysql.connect(
            host=self.host,  # 主机
            user=self.username,  # 用户名
            password=self.password,  # 密码
            port=self.port,  # 端口
            database=self.database,  # 数据库
            unix_socket=None,
            charset=self.charset,  # 编码
            sql_mode=None,
            read_default_file=None,
            conv=None,
            use_unicode=None,
            client_flag=0,
            cursorclass=pymysql.cursors.Cursor,
            init_command=None,
            connect_timeout=10,
            ssl=None,
            read_default_group=None,
            compress=None,
            named_pipe=None,
            autocommit=False,
            db=None,
            passwd=None,
            local_infile=False,
            max_allowed_packet=16 * 1024 * 1024,
            defer_connect=False,
            auth_plugin_map=None,
            read_timeout=None,
            write_timeout=None,
            bind_address=None,
            binary_prefix=False,
            program_name=None,
            server_public_key=None
        )
        self.cursor = self.conn.cursor()

    def close(self):
        """
        关闭数据库游标、关闭数据库连接
        """
        self.cursor.close()
        self.conn.close()

    def get_db_version(self):
        sql = "SELECT VERSION()"
        try:
            self.open_connection()
            self.cursor.execute(sql)
            return self.cursor.fetchone()
        except Exception as error:
            print(error)
        finally:
            self.close()

    def update(self, sql, params):
        """
        插入、更新、删除 操作封装
        :param sql: 要执行的SQL语句
        :param params: 要传递的参数，对应 SQL 语句中的 %xxx xxx是类型
        :return: 受影响的行数
        """
        try:
            self.open_connection()
            # insert, update, delete 返回的都是受影响的函数
            res = self.cursor.execute(sql, params)
            self.conn.commit()  # 注意提交事务
            return res
        except Exception as error:
            print(error)
        finally:
            self.close()

    def query(self, sql, params=None):
        """
        查询函数
        :param sql: 执行的SQL语句
        :param params: SQL语句的参数
        :return: 查询返回的结果集
        """
        # params=[] 这种默认参数，有问题，最好写成 None，然后下面判断
        if params == None:
            params = []
        try:
            self.open_connection()
            self.cursor.execute(sql, params)
            return self.cursor.fetchall()
        except Exception as error:
            print(error)
        finally:
            self.close()

    def query_page(self, sql, params=None, current_page=1, page_size=5):
        """
        分页查询
        :param sql: SQL语句
        :param params: SQL参数
        :param current_page: 当前页码
        :param page_size: 每页的大小
        :return: 查询的结果集
        """
        if params == None:
            params = []
        try:
            query_page_sql = sql + ' limit %s, %s'
            self.open_connection()
            self.cursor.execute(query_page_sql, params +
                                [(current_page - 1) * page_size, page_size])
            return self.cursor.fetchall()
        except Exception as error:
            print(error)
        finally:
            self.close()
