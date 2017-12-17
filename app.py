from flask import Flask, render_template
from flaskext.mysql import MySQL
from flask import jsonify
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = config.get('database', 'db_user')
app.config['MYSQL_DATABASE_PASSWORD'] = config.get('database', 'db_password')
app.config['MYSQL_DATABASE_DB'] = config.get('database', 'db_dbname')
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql = MySQL()
mysql.init_app(app)
cur = mysql.connect().cursor()


#test query connecting to old database and displaying the query
@app.route("/")
def main():
    cur.execute("SELECT FName FROM Rawscores ")
    return jsonify(data=cur.fetchall())
    #return render_template('index.html')

if __name__ == "__main__":
    app.run()