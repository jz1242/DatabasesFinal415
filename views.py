from healthApp import app, db
from models import User

@app.route("/")
def main():
    db.create_all()
    return 'Hello'
    #return render_template('index.html')
