# Import flask dependencies
from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for

# Import password / encryption helper tools
from werkzeug import check_password_hash, generate_password_hash

#Import module forms
from app.module_authentication.forms import RegistrationForm, LoginForm

# Import the database object from the main app module
from app import db

#import sessions
import database

# Import module models
from app.module_authentication.models import User

#Define the blueprint: 'auth'
mod_auth = Blueprint('auth',__name__)

@mod_auth.route('/', methods=['GET', 'POST'])
def home():
	form = LoginForm()
	if(form.validate_on_submit):
		session = database.start_session()
		user = session.query(User).filter_by(username=form.username.data).first()
		session.remove()
		if(user == None):
			flash('Log in below')
			#return redirect(url_for('auth.home'))
		elif(user.password == form.password.data):
			flash('You successfully logged in')
			return render_template('auth/home.html', page="home", form=form)
		else:
			flash('The password was incorrect. Try again')
			#return redirect(url_for('auth.home'))

	return render_template('auth/login.html', page="home", form=form)


@mod_auth.route('/registration/', methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		session = database.start_session()
		user = User(form.username.data, form.password.data, form.email.data)
		user_exists = session.query(User).filter_by(username=form.username.data).first()

		session.remove()
		if(user_exists == None):	
			session.add(user)
			session.commit()
			flash('Thanks for registering')
			return redirect(url_for('auth.home'))
		else:
			flash('The username already exists')
	return render_template('auth/registration.html', form=form)


@mod_auth.route('/home/')
def studentHome():
    return render_template('auth/home.html', page="portal")


