from app import db


# Abstract Models
class Abstract_Base(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key = True)


class Abstract_ClassType(Abstract_Base):
	__abstract__= True
	code = db.Column(db.String(3))
	start_time = db.Column(db.DateTime, default=db.func.now())
	end_time = db.Column(db.DateTime, default=db.func.now())
	day_one = db.Column(db.String(1))
	day_two = db.Column(db.String(1), default='X')


class Abstract_Course(Abstract_Base):
	__abstract__ = True
	dept = db.Column(db.String(4))
	credits = db.Column(db.Float(4))
	number = db.Column(db.String(3))
	name = db.Column(db.String(50))
