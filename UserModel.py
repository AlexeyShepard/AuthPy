from sqlalchemy import *

metadata = MetaData()

user = Table('user', metadata,
    Column('Id', Integer, primary_key=True),
    Column('Login', String(200), nullable=False),
    Column('Password', String(200), nullable=False),
    Column('Pincode', String(6), nullable=False),
    Column('Confirm', Boolean, nullable=False)
    )
