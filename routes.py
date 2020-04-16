#region IMPORT
import csv
from flask import render_template, url_for, flash, redirect, request
from application import app, db, bcrypt
from application.forms import LoginForm
from application.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required
#endregion

#region Disctionaries practice ---> I will use this as source of feedback in a seperate page
tweets = [ 
{
    'author': 'Makabongwe Jussie Nkabinde',
    'title': 'Feedback 01',
    'content': 'I mean, 100%!',
    'date':'20 March 2020'
},
{
    'author': 'Sange Maxaku',
    'title': 'Feedback 02',
    'content': 'Weird design. Weak le app!',
    'date':'21 March 2020'
},
{
    'author': 'Neo Mokono',
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

@app.route("/design", methods = ['POST', 'GET'])
def design():      
    # first things first ...
    
    return render_template('design.html')
    
@app.route("/design_handle", methods =['GET', 'POST'])
def design_handle(): 
    if request.method == 'GET':
        flash('You have been logged in!', 'sucesss')   
        try:
            print("reached 1")
            f = 'words.txt'
            path = '/home/botlhale/Desktop/Athi/Application/words.txt'
            readFile = open(path)
            doc = readFile.readline()
            # write to the the html
            return render_template('design.html', text_read=doc)
        except:
            doc = ""     
    return redirect(url_for('design'))
    
@app.route("/feedback")
def feedback():
    return render_template('feedback.html', tweets = tweets)

@app.route("/save", methods = ['POST', 'GET'])
def save():    
    if request.method == 'POST':
        text = request.form['text']
        # [code for saving the file to the db fits here]
        flash('Successfully saved', 'sucesss')
    return redirect(url_for('design'))


#@app.route("/register", methods =['GET', 'POST'])
#def register():
#    if current_user.is_authenticated:
#        return redirect(url_for('design'))
#    form = RegForm()
#    if form.validate_on_submit():
#        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
#        user = User(username=form.data, email=form.email.data, password=hashed_password)
#        db.session.add(user)
#        db.session.commit()
#        flash(f'Acount created for {form.username.data}. You can now log in!', 'sucesss') 
#        return redirect(url_for('login'))
#    flash('Ooops!')
#    return render_template('register.html', title='Register', form=form) */

@app.route("/login", methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return render_template(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('design'))
            #next_page = request.args.get('next')
            #return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Unsuccessful login. Please check your username and/or password', 'danger')      
    return render_template('login.html', title='Log In', form=form)
#endregion

@app.route("/logout")
def logout():
    #logout_user()
    return redirect(url_for('login'))

@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')
