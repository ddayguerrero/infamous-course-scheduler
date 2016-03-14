from app import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    full_name = db.Column(db.String(50), index = True)
    courseRegister = db.relationship('courseRegistered', backref = "registered", lazy = "dynamic")
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<User %r>' % (self.full_name)
