from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = "user"

    Id = Column(Integer, primary_key=True)
    Login = Column(String(200))
    Password = Column(String(200))
    Pincode = Column(String(6))
    Confirm = Column(Boolean)

    def __repr__(self):
        return "<user(Login='%s', Password='%s', Pincode='%s', Confirm='%s')>" % (self.Login, self.Password, self.Pincode, self.Confirm)
