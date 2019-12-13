from peewee import *

class SQLConnector:
    user = 'root'
    password = 'root'
    db_name = 'AuthPy'
    host = 'localhost'
    dbhandle = MySQLDatabase(db_name)

    def __init__(self, user, password, db_name, host):
        self.user = user
        self.password = password
        self.db_name = db_name
        self.host = host

        self.dbhandle = MySQLDatabase(
            db_name,
            user=user,
            password=password,
            host=host
        )

    def connect(self):
        try:
            self.dbhandle.connect()
            print('Подключение установлено!')
        except InternalError as ex:
            print(str(ex))
