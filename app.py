from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db'
db=SQLAlchemy(app)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    protocol=db.Column(db.String(64), nullable=False)
    path=db.Column(db.String(64), nullable=False)
    domen=db.Column(db.String(64), nullable=False)
    github=db.Column(db.Boolean, default=False)
    name_github=db.Column(db.String(64), default=None)

    def __repr__(self) -> str:
        return '<Article %r> % self.id'


@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/create-article', methods=['POST','GET'])
def create_aricle():
    if request.method=="POST":
        adress=request.form['adress']
    else:
        return render_template("create-article.html")


if __name__=='__main__':
    app.run(debug=True)
