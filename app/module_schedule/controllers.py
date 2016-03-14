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
mod_schedule = Blueprint('schedule',__name__)


@mod_auth.route('/')
def home():


@mod_auth.route('', methods=['GET', 'POST'])
def register():
	

@mod_auth.route('')
def studentHome():
    


