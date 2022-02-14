from sqlalchemy import create_engine, MetaData
from sqlalchemy import Table, Column
from sqlalchemy import Integer, String

class DataAccessLayer:
    connection = None
    engine = None
    conn_string = None
    metadata = MetaData()

    users = Table('users', metadata
                  ,Column('id', Integer(), primary_key=True)
                  ,Column('name', String(200))
                  ,Column('age', Integer())
                  )

    def db_init(self, conn_string):
        self.engine = create_engine(conn_string or self.conn_string)
        self.metadata.create_all(self.engine)
        self.connection = self.engine.connect()


dal = DataAccessLayer()
dal.db_init('mysql+pymysql://root:123456@127.0.0.1:3306/demo')

data = dal.connection.execute(dal.users.select()).fetchall()
print(data)

