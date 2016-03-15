
from flask import Flask, render_template , request, redirect, flash
from wtforms import Form, BooleanField, TextField, PasswordField, validators
import re

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

#Define the database object which is imported by modules and controllers
db = SQLAlchemy(app)

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
            flash("Password was accepted")
            return redirect('/login')    
    else:
        return redirect('/registration')

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

<<<<<<< HEAD
#Import a module / component using its blueprint handler variable
from app.module_authentication.controllers import mod_auth
from app.module_schedule.controllers import mod_schedule

#Register blueprints
app.register_blueprint(mod_auth)
app.register_blueprint(mod_schedule)

#Create the database file using SQLAlchemy
db.create_all()

=======


class RegistrationForm(Form):
    username = TextField('Username', [validators.Length(min=6, max=25)])
    password = PasswordField('password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('confirmPass')
    accept_tos = BooleanField('I accept the TOS', [validators.Required()])
>>>>>>> origin
