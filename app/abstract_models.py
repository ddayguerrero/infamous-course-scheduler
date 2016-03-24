from app import db


# Abstract Models
class Abstract_Base(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    
class Abstract_ClassType(Abstract_Base):
    code = db.Column(db.String(10))
    start_time = db.Column(db.String(20), default=db.func.now())
    end_time = db.Column(db.String(20), default=db.func.now())
    day_one = db.Column(db.String(1))
    day_two = db.Column(db.String(1))
    
    def __init__(self, code=None, start_time=db.func.now(), end_time=db.func.now(), day_one=None, day_two=None):
		self.code = code
		self.start_time = start_time
		self.end_time = end_time
		self.day_one = day_one
		self.day_two = day_two


class Abstract_Course(Abstract_Base):
    program = db.Column(db.String(4))
    credits = db.Column(db.Float(4))
    number = db.Column(db.String(3))
    name = db.Column(db.String(50))
    
    def __init__(self, program=None, number=None, credits=None, name=None):
		self.program = program
		self.number = number
		self.credits = credits
		self.name = name
