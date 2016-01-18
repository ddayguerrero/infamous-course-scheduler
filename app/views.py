from flask import render_template
from app import app


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',page="home")


@app.route('/login')
def login():
    return render_template('login.html',page="login")
