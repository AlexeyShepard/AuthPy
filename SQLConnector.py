from sqlalchemy import *
from UserModel import *

class SQLConnector:
    user = 'root'
    password = 'root'
    db_name = 'AuthPy'
    host = 'localhost'
    sqlEngine = create_engine("mysql://root:root@localhost/AuthPy");

    def __init__(self, user, password, db_name, host):
        self.user = user
        self.password = password
        self.db_name = db_name
        self.host = host

        self.sqlEngine = create_engine("mysql://" + self.user + ":" + self.password + "@" + host + "/" + db_name)

    def connect(self):
        try:
            self.sqlEngine.connect()
            print('Подключение установлено!')
        except exc.InternalError as ex:
            print(str(ex))

    def insertUser(self, login, password, pincode, confirm):
        ins = user.insert().values(Login=login, Password=password, Pincode=pincode, Confirm=confirm)
        result = self.sqlEngine.execute(ins)
        print(result)
