from app import db
from abstract_models import Abstract_Base


class User(Abstract_Base):
    __tablename__ = 'users'
    username = db.Column(db.String(30), unique = True)
    password = db.Column(db.String(20), index = True)
    email = db.Column(db.String(50), index = True)

    def __init__(self, username=None, password=None, email=None):
    	self.username = username
    	self.password = password
    	self.email = email

    def __repr__(self):
        return '<User %r>' % (self.username)

