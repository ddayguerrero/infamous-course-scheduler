from app import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    full_name = db.Column(db.String(50), index = True)
    course_register = db.Column(db.Integer, db.ForeignKey('courseRegistered.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    sequence_id = db.Column(db.Integer, db.ForeignKey('sequence.id'))
    course_completed_id = db.Column(db.Integer, db.ForeignKey('courseCompleted.id'))

    def __repr__(self):
        return '<User %r>' % (self.full_name)


class CourseCompleted(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	course_id = db.Column(db.Integer, db.ForeignKey('course.id'))

	def __repr__(self):
        return '<CourseCompleted %r>' % (self.id)


class Semester(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	course_id = db.Column(db.Integer, db.ForeignKey('course.id'))

	def __repr__(self):
		return '<Term %r>' % (self.id)

class Sequence(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	course_id = db.Column(db.Integer, db.ForeignKey('course.id'))

	def __repr__(self):
        return '<Sequence %r>' % (self.id)

class Prerequisites(db.Model):
	id = db.Column(db.Integer, primary_key = True)

	def __repr__(self):
        return '<Prerequisite %r>' % (self.id)

class CourseRegistered(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	course_id = db.Column(db.Integer, db.ForeignKey('course.id'))

	def __repr__(self):
		return '<CourseRegistered %r>' % (self.id)