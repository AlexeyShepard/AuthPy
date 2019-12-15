from sqlalchemy.orm import sessionmaker
from sqlalchemy import *
from sqlalchemy.exc import *
from UserModel import *

class SQLConnector:
    user = 'root'
    password = 'root'
    db_name = 'AuthPy'
    host = 'localhost'
    sqlEngine = create_engine("mysql://mysql:mysql@localhost/AuthPy");
    session = None

    def __init__(self, user, password, db_name, host):
        self.user = user
        self.password = password
        self.db_name = db_name
        self.host = host

        self.sqlEngine = create_engine("mysql://" + self.user + ":" + self.password + "@" + host + "/" + db_name)

    def connect(self):
        try:
            Session = sessionmaker()
            Session.configure(bind=self.sqlEngine)
            self.session = Session()
            print('Подключение установлено!')
        except Exception as ex:
            print("Произошла ошибка " + str(ex))

    def insertUser(self, login, password, pincode, confirm):
        self.connect()
        userToAdd = User(Login=login, Password=password, Pincode=pincode, Confirm=confirm)
        self.session.add(userToAdd)
        self.session.commit()
        print('Регистрация прошла успешно!')

    def selectUser(self, login, password, pincode):
        self.connect()
        selectedUser = self.session.query(User).filter(User.Login == login).filter(User.Password == password).filter(User.Pincode == pincode).first()
        print(selectedUser)
        return selectedUser
