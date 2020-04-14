from flask import Flask, render_template, url_for, flash, redirect, request
from forms import RegForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# from flask_login import login_user, current_user, logout_user, login_required

app = Flask(__name__) # an instantiated Flask variable is contained in the application variable 

#region Configurations
app.config['SECRET_KEY'] = 'dd629e01302dd66fafae953bcc8f3902'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
#endregion

#region DB
db = SQLAlchemy(app) # this makes a db associated with this program

#this defines the structure of the DB and is called a model that inherits from Model
class User(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), unique=True, nullable=False, default='pic.jpg' )
    posts = db.relationship('Post', backref='author', lazy='True')

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"
        
#this defines the structure of the DB and is called a model that inherits from Model
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.String(20), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=false) #user (the model) is 

    def __repre__(self):
        return f"Post('{self.title}', '{self.date}')"

#endregion

#region Disctionaries practice ---> I will use this as source of feedback in a seperate page
tweets = [ 
{
    'author': '@maks',
    'title': 'Feedback 01',
    'content': 'I mean, 100%!',
    'date':'20 March 2020'
},
{
    'author': '@sange',
    'title': 'Feedback 02',
    'content': 'Weird design. Weak le app!',
    'date':'21 March 2020'
},
{
    'author': '@neo',
    'title': 'Feedback 03',
    'content': 'Uhm, could do better. I give it boma-4.5',
    'date':'22 March 2020'
}
]
#endregion

#region HTML - pages as templated
@app.route("/")
@app.route("/home")
def method():
    filename = "pic.jpg"
    return render_template('home.html', user_image = filename)

@app.route("/about")
@app.route("/contact-us")
def about():
    return render_template('about.html')

@app.route("/design")
def design():
    return render_template('design.html')

@app.route("/feedback")
def feedback():
    return render_template('feedback.html', tweets = tweets)

@app.route("/register", methods =['GET', 'POST'])
def register():
    form = RegForm()
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

@app.route("/handle_login")
def handle_logins():    
    return "Successful login."
#endregion


#region the driver method
if __name__ == "__main__":
    app.debug = True
    app.run() 
#endregion