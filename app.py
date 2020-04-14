from flask import Flask, render_template, url_for, flash, redirect, request
from forms import RegForm, LoginForm
# from flask_login import login_user, current_user, logout_user, login_required

app = Flask(__name__) # an instantiated Flask variable is contained in the application variable 

app.config['SECRET_KEY'] = 'dd629e01302dd66fafae953bcc8f3902'

# disctionaries practice --- I will use this as source of feedback in a seperate page
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

# html - pages
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

if __name__ == "__main__":
    app.debug = True
    app.run() 