from peewee import *

class UserModel(Model):
    login = CharField()
    password = CharField()
    pincode = CharField()
    confirm = BooleanField()

    def __init__(self, login, password, pincode, confirm):
        self.login = login
        self.password = password
        self.pincode = pincode
        self.confirm = confirm
