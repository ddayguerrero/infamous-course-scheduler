# Import flask and template operators
from flask import Flask, render_template, session

# Import SQLAlchemy
from flask.ext.sqlalchemy import SQLAlchemy

# Import engine
from sqlalchemy import create_engine

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Define the database object which is imported by modules and controllers
db = SQLAlchemy(app)

engine = create_engine('sqlite:///app.db')

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Import a module / component using its blueprint handler variable
from app.module_authentication.controllers import mod_auth
from app.module_schedule.controllers import mod_schedule

# Register blueprints
app.register_blueprint(mod_auth)
app.register_blueprint(mod_schedule)

# Create the database file using SQLAlchemy
from app.module_authentication import models
from app.module_schedule import models
Base.metadata.create_all(bind=engine)
