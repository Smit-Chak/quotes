from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:smit1303@localhost/quotes'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://bwswehxloohuhr:361853d8ff30269152e985d8dc8daec4d2b293ff30a74164aaa9e46edd49f37d@ec2-54-216-90-155.eu-west-1.compute.amazonaws.com:5432/de7v8sak90dh7e'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Favquotes(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    author = db.Column(db.String(30))
    quote = db.Column(db.String(2000))

@app.route('/')
def index():
    result = Favquotes.query.all()
    return render_template('index.html', result = result)



@app.route('/quotes')
def quotes():
    return render_template('quotes.html')

@app.route('/process', methods = ['POST'])
def process():
    author = request.form['author']
    quote = request.form['quote']
    quotedata = Favquotes(author = author , quote = quote)
    db.session.add(quotedata)
    db.session.commit()
    return redirect(url_for('index'))