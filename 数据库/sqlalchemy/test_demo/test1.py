import unittest
from sqlalchemy import create_engine, MetaData
from sqlalchemy import Table, Column, Integer, String


class MyTest(unittest.TestCase):

    engine = None
    connection = None
    metadata = None

    @classmethod
    def setUpClass(cls) -> None:  # 在整个测试类中，setUpClass 方法只执行一次
        cls.engine = create_engine('mysql+pymysql://root:root@127.0.0.1:3306/demo', echo=False, pool_recycle=3600)
        cls.connection = cls.engine.connect()
        cls.metadata = MetaData()
        cls.init_table()
        cls.reset_db()

    @classmethod
    def tearDownClass(cls) -> None: # 在整个测试类中，tearDownClass 方法只执行一次
        cls.connection.close()

    @classmethod
    def init_table(cls) -> None:
        cls.t_user = Table('user', cls.metadata,
                         Column('id', Integer(), primary_key=True),
                         Column('username', String(20), nullable=False),
                         Column('password', String(100), nullable=False)
                     )

    @classmethod
    def reset_db(cls) -> None:
        cls.metadata.drop_all(cls.engine)
        cls.metadata.create_all(cls.engine)


    def setUp(self) -> None: # setUp 在每个测试方法执行之前执行
        pass

    def tearDown(self) -> None: # tearDown 在每个测试方法执行之后执行
        pass


    def test_001(self):
        """测试SQL的生成"""
        sql_str = self.t_user.select()
        print(sql_str)


if __name__ == '__main__':
    unittest.main()
