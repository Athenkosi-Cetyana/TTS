#region IMPORT
from flask import  render_template, url_for, flash, redirect, request
from app.formsforms import RegForm, LoginForm
from app.models import User, Post
from app import app
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

@app.route("/handle_save", methods =['GET', 'POST'])
def handle_save():    
    return "Successfully saved."
#endregion