# Import flask dependencies
from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for

# Import module forms
from app.module_authentication.forms import RegistrationForm, LoginForm

# Import the database object from the main app module
from app import db

# Import module models
from app.module_authentication.models import User

# Import decorators
from app.module_authentication.decorators import requires_login

# Define the blueprint: 'auth'
mod_auth = Blueprint('auth',__name__)


@mod_auth.before_request
def before_request():
	g.user = None
	if 'user_id' in session:
		g.user = User.query.get(session['user_id'])


@mod_auth.route('/', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user:
			session['user_id'] = user.id
			flash('Welcome %s' % user.username)
			return redirect(url_for('auth.home'))
		flash('Wrong username or password', 'error-message')
	return render_template('auth/login.html', form=form)


@mod_auth.route('/registration/', methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		user_exists = User.query.filter_by(username=form.username.data).scalar() is not None
		if(user_exists):
			flash('The username already exists.')	
		else:
			user = User(form.username.data, form.password.data, form.email.data)
			db.session.add(user)
			db.session.commit()
			session['user_id'] = user.id
			flash('Thank you for registering')
			return redirect(url_for('auth.login'))
	return render_template('auth/registration.html', form=form)


@mod_auth.route('/home/')
#@requires_login
def home():
    return render_template('auth/profile.html', page="home")


@mod_auth.route('/fall/')
#@requires_login
def fall():
    return render_template('auth/semesters/fall.html', page="fall")

	
@mod_auth.route('/winter/')
#@requires_login
def winter():
    return render_template('auth/semesters/winter.html', page="winter")
	
@mod_auth.route('/summer/')
#@requires_login
def summer():
    return render_template('auth/semesters/summer.html', page="summer")

