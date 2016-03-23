from app import db
from app.abstract_models import Abstract_Base, Abstract_ClassType, Abstract_Course
from app.module_authentication.models import User
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
    requisite_for = db.Column(db.Integer, db.ForeignKey('mappings.id'))
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


class AcademicRecord(Abstract_Base):
    __tablename__ = 'academic_records'
    user_id = db.Column(db.Integer)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))
    course_status = db.Column(db.String(50))

    def __init__(self, user_id=None, course_id=None, course_status=None):
        self.user_id = user_id
        self.course_id = course_id
        self.course_status = course_status

    def __repr__(self):
        return '<User %r>' % (self.id)


class Semester(Abstract_Base):
    __tablename__ = 'semesters'
    semester_id = db.Column(db.String(50))
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))

    def __init__(self, semester_id=None, course_id=None):
        self.semester_id = semester_id
        self.course_id = course_id

    def __repr__(self):
        return '<User %r>' % (self.id)


class Sequence(Abstract_Base):
    __tablename__ = 'sequences'
    option = db.Column(db.String(50))
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))

    def __init__(self, option=None, course_id=None):
        self.option = option
        self.course_id = course_id

    def __repr__(self):
        return '<User %r>' % (self.id)


class Mapping(Abstract_Base):
    __tablename__ = 'mappings'
    course_req_id = db.Column(db.Integer)
    course_req_type = db.Column(db.Integer)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))

    def __init__(self, course_req_id=None, course_req_type=None, course_id=None):
        self.course_req_id = course_req_id
        self.course_req_type = course_req_type
        self.course_id = course_id

    def __repr__(self):
        return '<User %r>' % (self.id)


class Elective(Abstract_Base):
    __tablename__ = 'electives'
    elective_type = db.Column(db.String(50))
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))

    def __init__(self, elective_type=None, course_id=None):
        self.elective_type = elective_type
        self.course_id = course_id

    def __repr__(self):
        return '<User %r>' % (self.id)


