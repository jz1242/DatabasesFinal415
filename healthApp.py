from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify
import configparser

app = Flask(__name__)
app.secret_key = "12345"
app.static_folder = 'static'
config = configparser.ConfigParser()
config.read('config.ini')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://'+config.get('database', 'db_user')+':'+ config.get('database', 'db_password')+'@localhost/' + config.get('database', 'db_dbname')
db = SQLAlchemy(app)
db.create_all()
from views import *

if __name__ == "__main__":
    app.run(debug=True)