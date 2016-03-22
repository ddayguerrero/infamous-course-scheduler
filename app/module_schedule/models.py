from app import db
from app.abstract_models import Abstract_Base, Abstract_ClassType, Abstract_Course
from sqlalchemy.orm import relationship


# Concrete Models
class Student(Abstract_Base):
    __tablename__ = 'students'
    full_name = db.Column(db.String(50), index = True)
    academic_record = db.Column(db.Integer, db.ForeignKey('academic_records.id'))
    sequence = db.Column(db.Integer, db.ForeignKey('sequences.id'))
    user = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, full_name=None, academic_record=None, sequence=None, user=None):
    	self.full_name = full_name
    	self.academic_record = academic_record
    	self.sequence = sequence
    	self.user = user

    def __repr__(self):
		return '<User %r>' % (self.full_name)


class Course(Abstract_Course):
    __tablename__ = 'courses'
    type = db.Column(db.String(30))
    requisite_for = db.Column(db.Integer, db.ForeignKey('req_mappings.id'))
    lectures = relationship("Lecture")

    def __init__(self, program=None, credits=None, number=None, name=None):
    	self.program = program
    	self.credits = credits
    	self.number = number
    	self.name = name

    def __repr__(self):
        return '<Course %r>' % (self.name)


class Lab(Abstract_ClassType):
    __tablename__ = 'labs'
    lecture_id = db.Column(db.Integer, db.ForeignKey('lectures.id'))

    def __init__(self, lecture_id=None, section_code=None, start_time=None, end_time=None, day_one=None):
    	self.lecture_id = lecture_id
    	self.section_code = section_code
    	self.start_time = start_time
    	self.end_time = end_time
    	self.day_one = day_one

    def __repr__(self):
        return '<Lab %r>' % (self.code)
		

class Tutorial(Abstract_ClassType):
    __tablename__ = 'tutorials'
    lecture_id = db.Column(db.Integer, db.ForeignKey('lectures.id'))

    def __init__(self, lecture_id=None, section_code=None, start_time=None, end_time=None, day_one=None, day_two=None):
    	self.lecture_id = lecture_id
    	self.section_code = section_code
    	self.start_time = start_time
    	self.end_time = end_time
    	self.day_one = day_one
    	self.day_two = day_two

    def __repr__(self):
        return '<Tutorial %r>' % (self.section_id)


class Lecture(Abstract_ClassType):
	__tablename__ = 'lectures'
	instructor = db.Column(db.String(50))
	course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))
	semester_id = db.Column(db.Integer, db.ForeignKey('semesters.id'))
	tutorial = relationship("Tutorial")
	lab = relationship("Lab")

	def __init__(self, instructor=None, course_id=None, semester_id=None, start_time=None, end_time=None, day_one=None, day_two=None):
		self.instructor = instructor
		self.course_id = course_id
		self.semester_id = semester_id
		self.start_time = start_time
		self.end_time = end_time
		self.day_one = day_one
		self.day_two = day_two

	def __repr__(self):
		return '<Lecture %r>' % (self.section_id)

# Tables
academic_records = db.Table('academic_records',
	db.Column('id', db.Integer, primary_key = True),
	db.Column('course_status', db.String(20)),
	db.Column('student_id', db.Integer, db.ForeignKey('students.id')),
	db.Column('course_id', db.Integer, db.ForeignKey('courses.id'))
)


semesters = db.Table('semesters',
	db.Column('id', db.Integer, primary_key = True),
	db.Column('semester_id', db.Integer),
	db.Column('course_id', db.Integer, db.ForeignKey('courses.id'))
)


sequences = db.Table('sequences',
	db.Column('id', db.Integer, primary_key = True),
	db.Column('option', db.String(50)), # Web, Avionics, Games, General
	db.Column('course_id', db.Integer, db.ForeignKey('courses.id'))
)


req_mappings = db.Table('req_mappings',
	db.Column('id', db.Integer, primary_key = True),
	db.Column('course_req_id', db.Integer),
	db.Column('course_req_type', db.Integer),
	db.Column('course_id', db.Integer, db.ForeignKey('courses.id'))
)


electives = db.Table('elective',
	db.Column('id', db.Integer, primary_key = True),
	db.Column('elective_type', db.String(50)), # Tech, BasicScience, General
	db.Column('course_id', db.Integer, db.ForeignKey('courses.id'))
)

