from app import db


class Student(db.Model):
	__tablename__ = 'student'
    id = db.Column(db.Integer, primary_key = True)
    full_name = db.Column(db.String(50), index = True)

    courses_registered = relationship("CourseRegistered")
   	courses_completed = relationship("CourseCompleted")
   	sequence = relationship("Sequence")

    def __repr__(self):
        return '<User %r>' % (self.full_name)


class CourseCompleted(db.Model):
	__tablename__ = 'courseCompleted'
	id = db.Column(db.Integer, primary_key = True)
	student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
	course_id = db.Column(db.Integer, db.ForeignKey('course.id'))

	def __repr__(self):
        return '<CourseCompleted %r>' % (self.id)


class Semester(db.Model):
	__tablename__ = 'semester'
	id = db.Column(db.Integer, primary_key = True)
	course_id = db.Column(db.Integer, db.ForeignKey('course.id'))

	def __repr__(self):
		return '<Term %r>' % (self.id)


class Sequence(db.Model):
	__tablename__ = 'sequence'
	id = db.Column(db.Integer, primary_key = True)
	student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
	course_id = db.Column(db.Integer, db.ForeignKey('course.id'))

	def __repr__(self):
        return '<Sequence %r>' % (self.id)


class Prerequisites(db.Model):
	__tablename__ = 'prerequisites'
	id = db.Column(db.Integer, primary_key = True)

	def __repr__(self):
        return '<Prerequisite %r>' % (self.id)


class CourseRegistered(db.Model):
	__tablename__ = 'courseRegistered'
	id = db.Column(db.Integer, primary_key = True)
	student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
	course_id = db.Column(db.Integer, db.ForeignKey('course.id'))

	def __repr__(self):
		return '<CourseRegistered %r>' % (self.id)


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(4))
    credits = db.Column(db.Double(4))
    number = db.Column(db.String(3))
    name = db.Column(db.String(50))


class Lab(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
    start_time = db.Colum(db.DateTime, default=db.func.now())
    end_time = db.Colum(db.DateTime, default=db.func.now())
    days = db.Column(db.String(25))
    

class Section(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
    code = db.Column(db.String(3))
    start_time = db.Colum(db.DateTime, default=db.func.now())
    end_time = db.Colum(db.DateTime, default=db.func.now())
    professor = db.Column(db.Integer(50))
    days = db.Column(db.String(25))
    semester = db.Column(db.Integer, db.ForeignKey('semester.id'))
    

class Tutorial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
    start_time = db.Colum(db.DateTime, default=db.func.now())
    end_time = db.Colum(db.DateTime, default=db.func.now())
    days = db.Column(db.String(25))
