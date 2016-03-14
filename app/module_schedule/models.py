from app import db


class Student(db.Model):
	__tablename__ = 'student'
    id = db.Column(db.Integer, primary_key = True)
    full_name = db.Column(db.String(50), index = True)

    courses_registered = relationship("CourseRegistered")
   	courses_completed = relationship("CourseCompleted")
   	sequence = relationship("Sequence", back_populates="student")

    def __repr__(self):
        return '<User %r>' % (self.full_name)


class CourseCompleted(db.Model):
	__tablename__ = 'courseCompleted'
	id = db.Column(db.Integer, primary_key = True)
	student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
	course_id = db.Column(db.Integer, db.ForeignKey('course.id'))

	course = relationship("Course", back_populates="courseCompleted")

	def __repr__(self):
        return '<CourseCompleted %r>' % (self.id)


class Semester(db.Model):
	__tablename__ = 'semester'
	id = db.Column(db.Integer, primary_key = True)
	courses = relationship("Course")

	def __repr__(self):
		return '<Term %r>' % (self.id)


class Sequence(db.Model):
	__tablename__ = 'sequence'
	id = db.Column(db.Integer, primary_key = True)
	student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
	course_id = db.Column(db.Integer, db.ForeignKey('course.id'))

	student = relationship("Student", back_populates="sequence")
	courses = relationship("Course")

	def __repr__(self):
        return '<Sequence %r>' % (self.id)


class Prerequisites(db.Model):
	__tablename__ = 'prerequisites'
	id = db.Column(db.Integer, primary_key = True)
	course_id = db.Column(db.Integer, db.ForeignKey('course.id'))

	def __repr__(self):
        return '<Prerequisite %r>' % (self.id)


class CourseRegistered(db.Model):
	__tablename__ = 'courseRegistered'
	id = db.Column(db.Integer, primary_key = True)
	student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
	course_id = db.Column(db.Integer, db.ForeignKey('course.id'))

	course = relationship("Course", back_populates = "courseRegistered")

	def __repr__(self):
		return '<CourseRegistered %r>' % (self.id)

class Course(db.Model):
	__tablename__ = 'course'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(4))
    credits = db.Column(db.Double(4))
    number = db.Column(db.String(3))
    name = db.Column(db.String(50))
    semester = db.Column(db.Integer, db.ForeignKey('semester.id'))

    courses_registered = relationship("CourseRegistered", back_populates="course")
    courses_completed = relationship("CourseCompleted", back_populates="course")
    courses_prerequisites = relationship("Prerequisites")

    sections = relationship("Section")

    def __repr__(self):
		return '<Course %r>' % (self.name)
    
class Section(db.Model):
	__tablename__ = 'section'
	id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
    code = db.Column(db.String(3))

    lecture = relationship("Lecture", back_populates="section")
    tutorial = relationship("Tutorial")
    lab = relationship("Lab") 

    def __repr__(self):
		return '<Section %r>' % (self.code)

class Lab(db.Model):
	__tablename__ = 'lab'
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
    code = db.Column(db.String(3))

    section_id = db.Column(db.Integer, db.ForeignKey('section.id'))

    def __repr__(self):
		return '<Lab %r>' % (self.code)

class Tutorial(db.Model):
	__tablename__ = 'tutorial'
    id = db.Column(db.Integer, primary_key=True)
    section_id = db.Column(db.Integer, db.ForeignKey('section.id'))
    start_time = db.Colum(db.DateTime, default=db.func.now())
    end_time = db.Colum(db.DateTime, default=db.func.now())
    days = db.Column(db.String(25))

    section_id = db.Column(db.Integer, db.ForeignKey('section.id'))

    def __repr__(self):
		return '<Tutorial %r>' % (self.section_id)

class Lecture(db.Model):
	__tablename__ = 'lecture'
    id = db.Column(db.Integer, primary_key=True)
    section_id = db.Column(db.Integer, db.ForeignKey('section.id'))
    start_time = db.Colum(db.DateTime, default=db.func.now())
    end_time = db.Colum(db.DateTime, default=db.func.now())
    days = db.Column(db.String(25))

    section = relationship("Section", back_populates="lecture")

    def __repr__(self):
		return '<Lecture %r>' % (self.section_id)

