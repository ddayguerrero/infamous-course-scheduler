from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_Name = db.Column(db.String(30), unique = True)
    password = db.Column(db.String(20), index = True)
    email = db.Column(db.String(50), index = True)

    def __repr__(self):
        return '<User %r>' % (self.user_Name)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    full_name = db.Column(db.String(50), index = True)
    courseRegister = db.relationship('courseRegistered', backref = "registered", lazy = "dynamic")
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<User %r>' % (self.full_name)


