# app.py
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql://postgres:energia@localhost/spotrebaee'
db = SQLAlchemy(app)

#create class, class name = table name in database
class DomacnostUpdate(db.Model):
    #create columns in table
    id = db.Column(db.Integer, primary_key=True)
    domacnot = db.Column(db.String(80))
    spotreba_primer = db.Column(db.Integer)
    okres = db.Column(db.String(80))

    def __init__(self, domacnot, spotreba_primer,okres):
        self.domacnot = domacnot
        self.spotreba_primer = spotreba_primer
        self.okres = okres
    
@app.route('/')
def home():
    return render_template('add.html')


@app.route("/post_user", methods=['POST'])
def post_user():
    #create object
    domacnost = DomacnostUpdate(request.form['domacnost'], request.form['spotreba'], request.form['okres'])
    #add object in to database
    db.session.add(domacnost)
    #save object in to database
    db.session.commit()

    return redirect (url_for('home')) 

    
if __name__ == '__main__':
    app.run(debug=True)
