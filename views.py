from healthApp import app, db
from models import User
from flask import Flask, render_template, request, redirect, url_for

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/signup")
def signup():
    return render_template('signup.html')

@app.route("/added", methods=['POST'])
def added():
    user = User(name=request.form['inputName'], email=request.form['inputEmail'], password=request.form['inputPassword'])
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('index'))

