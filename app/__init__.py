# Import flask and template operators
from flask import Flask, render_template , request, redirect, flash
from wtforms import Form, BooleanField, TextField, PasswordField, validators
import re
# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')


@app.route('/')
@app.route('/login')
def home():
    return render_template('auth/login.html', page="home")


@app.route('/registration')
def register():
    return render_template('auth/registration.html', page="register")


@app.route('/registerForm', methods=['GET','POST'])
def registerForm():
    if request.method == 'POST':
        error = False
        password = request.form['password']
        confirmPass = request.form['confirmPass']
        email = request.form['email']
        fullName = request.form['full name']
        username = request.form['username']
        if password != confirmPass :
            flash("Passwords must be the same")
            error = True
        if len(password) < 6 or len(password) > 16 :
            flash("Password must contain more than 6 and less than 16 characters")
        if  re.search('\W',password):
            flash("Password cannot contain special characters")
            error = True
        if not re.search('[0-9]',password):
            flash("Password must contain atleast one number")
            error = True
        if not re.search("[a-z]",password):
            flash("Password must contain atleast one lowercase character")
            error = True
        if not re.search('[A-Z]',password):
            flash("Password must contain atleast one uppercase character")
            error =True
        if error :
            return redirect('/registration')
    else:
        return redirect('/login')

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404



class RegistrationForm(Form):
    username = TextField('Username', [validators.Length(min=6, max=25)])
    password = PasswordField('password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('confirmPass')
    accept_tos = BooleanField('I accept the TOS', [validators.Required()])
