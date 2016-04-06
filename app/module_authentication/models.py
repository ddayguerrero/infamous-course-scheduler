from app import db
from app.abstract_models import Abstract_Base
from sqlalchemy.orm import relationship, backref

class User(Abstract_Base):
    __tablename__ = 'users'
    username = db.Column(db.String(30), unique = True)
    password = db.Column(db.String(20), index = True)
    email = db.Column(db.String(50), index = True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))
    #student = db.relationship('students', backref=backref('users', uselist=False))
    
    def __init__(self, username=None, password=None, email=None, student_id=None):
    	self.username = username
    	self.password = password
    	self.email = email
    	self.student_id = student_id

    def __repr__(self):
        return '<User %r>' % (self.username)

