#Import flask dependencies
from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for

#Import password / encryption helper tools
from werkzeug import check_password_hash, generate_password_hash

#Import the database object from the main app module
from app import db

#Import module forms
#from app.module_authentication.forms import LoginForm

#Import module models
#from app.module_authentication.models import User

#Define the blueprint: 'auth'
mod_auth = Blueprint('auth',__name__)


@mod_auth.route('/')
def home():
    return render_template('auth/login.html', page="home")


@mod_auth.route('/registration/')
def register():
    return render_template('auth/registration.html', page="register")


@mod_auth.route('/home')
def studentHome():
    return render_template('auth/home.html', page="portal")
