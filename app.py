from flask import Flask, render_template
import requests
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///movie.db'
db=SQLAlchemy(app)

class myfavmovies(db.Model):
    favmoviename=db.Column(db.Integer,primary_key=True)

@app.route('/')
def home():
    return render_template('index.html')


if __name__=="__main__":
    app.run(debug=True)