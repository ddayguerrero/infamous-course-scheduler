from app import app
from flask import render_template

@app.route("/")
@app.route("/home")
def login():
    return render_template('home.html')
