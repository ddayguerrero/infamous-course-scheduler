# Import flask and template operators
from flask import Flask, render_template, session

#Import session
from sqlalchemy.orm import sessionmaker, scoped_session

# Import SQLAlchemy
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base

# Import engine
from sqlalchemy import create_engine, MetaData

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Define the database object which is imported by modules and controllers
db = SQLAlchemy(app)

engine = create_engine('sqlite:///app.db')
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
metadata = MetaData()

Base = declarative_base()
Base.query = db_session.query_property()

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

# Import a module / component using its blueprint handler variable
from app.module_authentication.controllers import mod_auth
from app.module_schedule.controllers import mod_schedule

# Register blueprints
app.register_blueprint(mod_auth)
app.register_blueprint(mod_schedule)

# Create the database file using SQLAlchemy
from app.module_authentication import models
Base.metadata.create_all(bind=engine)
