#Import flask dependencies
from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for

#Import password / encryption helper tools
from werkzeug import check_password_hash, generate_password_hash

#Import the database object from the main app module
from app import db

#Import module forms
from app.module_authentication.forms import RegistrationForm

#Import module models
from app.module_authentication.models import User

#Define the blueprint: 'auth'
mod_auth = Blueprint('auth',__name__)


@mod_auth.route('/')
def home():
    return render_template('auth/login.html', page="home")


@mod_auth.route('/registration/', methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if request.method == 'POST' and form.validate_on_submit():
		user = User(form.username.data, form.email.data, form.password.data)
		db.session.add(user)
		db.session.commit()
		session['user_id'] = user.id
		flash('Thanks for registering')
		return redirect(url_for('auth.login'))
	return render_template('auth/registration.html', page="register", form=form)

@mod_auth.route('/home/')
def studentHome():
    return render_template('auth/home.html', page="portal")


