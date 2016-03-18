from app import Base, metadata
from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key = True)
    username = Column(String(30), unique = True)
    password = Column(String(20), index = True)
    email = Column(String(50), index = True)

    def __init__(self, username=None, password=None, email=None):
    	self.username = username
    	self.password = password
    	self.email = email

    def __repr__(self):
        return '<User %r>' % (self.username)

