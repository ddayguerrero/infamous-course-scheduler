from flask.ext.wtf import Form
from wtforms import BooleanField, TextField, PasswordField, validators


class RegistrationForm(Form):
    username = TextField('Username', [validators.Length(min=4, max=25)])
    email = TextField('Email Address', [validators.Email(), validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
    	validators.Required(),
    	validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the Terms of Service', [validators.Required()])


class LoginForm(Form):
	username = TextField('Username', [validators.Length(min=4, max=25)])
	password = PasswordField('Password', [validators.Length(min=1, max=25)])


class CourseSelection(Form):
    courseName = TextField('Course Name', [validators.Length(min=4, max=25)])   