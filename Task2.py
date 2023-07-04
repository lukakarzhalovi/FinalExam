from flask import Flask, request,render_template,redirect
from flask_sqlalchemy import SQLAlchemy,session




app = Flask(__name__)
app.config['SECRET_KEY'] = 'LUKAKARZHALOVI'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Titanic.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
app.app_context().push()



class Passengers(db.Model):

    PassengerId = db.Column(db.Integer, primary_key = True)
    Survived = db.Column(db.Integer)
    Pclass = db.Column(db.Integer)
    Name = db.Column(db.String)
    Sex = db.Column(db.Integer)
    Age = db.Column(db.Integer)
    SibSp = db.Column(db.Integer)
    Parch = db.Column(db.Integer)
    Ticket = db.Column(db.String)
    Fare = db.Column(db.Integer)
    Cabin = db.Column(db.String)
    Embarked = db.Column(db.String)

    def __str__(self):
        return f"სახელი: {self.Name}, გადარჩა/ვეგ გადარჩა: {self.Survived}, სქესი : {self.Sex}, რომელი პორტიდან მოხვდა გემზე {self.Embarked}"




@app.route('/', methods = ['POST', 'GET'])
def search():
    if request.method == 'POST':
        input = request.form['input']
        try:
            age = int(input)
            users = Passengers.query.filter_by(Age = age).all()
            print(users)
            return render_template("home.html", passengers = users)
        except:
            gender = str(input)
            users = Passengers.query.filter_by(Sex = gender).all()
            return render_template('Sex.html' , passengers = users )
    return render_template('search.html')


@app.route('/result')
def result():
    return render_template('search.html')
    

if __name__ == "__main__":
    app.run(debug=True)
    db.create_all()
