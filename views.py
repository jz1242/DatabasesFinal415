from healthApp import app, db
from models import User
from flask import Flask, render_template, request, redirect, url_for, session

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/signup")
def signup():
    return render_template('signup.html')


@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/search", methods=['POST'])
def search():
    #return render_template('home.html')
    return "here"

@app.route("/added", methods=['POST'])
def added():
    user = User(name=request.form['inputName'], email=request.form['inputEmail'], password=request.form['inputPassword'])
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('index'))

@app.route("/signin")
def signin():
    return render_template('signin.html')

@app.route("/login", methods=['POST'])
def login():
    if(db.session.query(User).filter_by(name=request.form['username'], password=request.form['password']).first() == None):
        return redirect(url_for('signin'))
    session['logged_in'] = True
    return redirect(url_for('home'))

@app.route("/logout")
def logout():
    if(session.get('logged_in') == True):
        session['logged_in'] = False
    return redirect(url_for('index'))

