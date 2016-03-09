
from flask.ext.wtf import Form
# Login and Register forms should be here
from wtforms import BooleanField, TextField, PasswordField, validators

class RegistrationForm(Form):
    username = TextField('Username')
    email = TextField('Email Address')
    password = PasswordField('New Password')
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS')